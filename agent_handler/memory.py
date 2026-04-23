from __future__ import annotations

from typing import Iterable, List

from .models import Episode, MemoryRecord, Mode, Task


class MemoryGovernor:
    def __init__(self, ttl_ticks: int, decay: float) -> None:
        self.ttl_ticks = ttl_ticks
        self.decay = decay
        self.tick = 0
        self.records: dict[str, MemoryRecord] = {}

    def advance_tick(self) -> None:
        self.tick += 1
        expired: list[str] = []
        for key, record in self.records.items():
            record.reinforcement *= self.decay
            if record.expires_at_tick <= self.tick or record.reinforcement < 0.05:
                expired.append(key)
        for key in expired:
            del self.records[key]

    def retrieve(self, task: Task, mode: Mode) -> List[MemoryRecord]:
        candidates: list[tuple[float, MemoryRecord]] = []
        blocked_keys = set()
        if mode is Mode.DIVERSIFY:
            blocked_keys.update(self.dominant_keys(limit=1))

        for key, record in self.records.items():
            if key in blocked_keys:
                continue
            overlap = self._tag_overlap(task.tags, record.tags)
            if overlap == 0.0:
                continue
            freshness = 1.0 / (1 + max(0, self.tick - record.last_used_tick))
            score = overlap * (0.5 + (0.5 * freshness)) * record.reinforcement
            candidates.append((score, record))

        candidates.sort(key=lambda item: item[0], reverse=True)
        selected = [record for _, record in candidates[:3]]
        for record in selected:
            record.last_used_tick = self.tick
        return selected

    def remember(self, task: Task, episode: Episode) -> None:
        reinforcement = 1.0 if episode.review.approved else 0.55
        if episode.review.contradiction:
            reinforcement *= 0.3
        key = f"{task.task_id}:{episode.step.route}:{self.tick}"
        self.records[key] = MemoryRecord(
            key=key,
            tags=tuple(sorted(set(task.tags + (episode.step.route,)))),
            summary=episode.result.summary,
            reinforcement=reinforcement,
            expires_at_tick=self.tick + self.ttl_ticks,
            last_used_tick=self.tick,
        )

    def dominant_share(self) -> float:
        if len(self.records) < 2:
            return 0.0
        total = sum(record.reinforcement for record in self.records.values())
        if total <= 0:
            return 0.0
        dominant = max(record.reinforcement for record in self.records.values())
        return dominant / total

    def dominant_keys(self, limit: int = 1) -> list[str]:
        ranked = sorted(
            self.records.values(),
            key=lambda record: record.reinforcement,
            reverse=True,
        )
        return [record.key for record in ranked[:limit]]

    def snapshot_records(self) -> list[MemoryRecord]:
        return [
            MemoryRecord(
                key=record.key,
                tags=record.tags,
                summary=record.summary,
                reinforcement=record.reinforcement,
                expires_at_tick=record.expires_at_tick,
                last_used_tick=record.last_used_tick,
            )
            for record in self.records.values()
        ]

    def load_snapshot(
        self,
        records: Iterable[MemoryRecord],
        *,
        tick: int = 0,
    ) -> None:
        self.records = {record.key: record for record in records}
        self.tick = tick

    @staticmethod
    def _tag_overlap(left: Iterable[str], right: Iterable[str]) -> float:
        left_set = set(left)
        right_set = set(right)
        if not left_set or not right_set:
            return 0.0
        return len(left_set & right_set) / len(left_set | right_set)
