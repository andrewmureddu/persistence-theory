# ACP Agent Handler MVP

This directory contains a small, runnable starter for an in-house agent handler
that uses the Adaptive Coherence Principle (ACP) as an operating rule.

The goal is not to make a single perfect agent. The goal is to keep the
handler inside a productive interval:

- `dissolution`: the system loses coherence
- `crystallization`: the system overconverges on one route, one memory, or one
  framing

The ACP claim is that the same mechanisms that keep the system coherent also
push it toward rigidity. In operational terms, the handler must keep paying a
"Prigogine tax": it must spend some throughput on re-grounding, route decay,
memory decay, and independent review.

The research workflow adds one more tax: generativity. A completed theory-building
task should identify the questions, observables, or falsification paths it opens,
not only the answer it closes. In ACP terms, the handler should treat
`successor_questions`, `new_observables`, or `new_tests` as first-class expected
fields for non-routine research tasks.

## What is in here

- `models.py`: typed runtime objects
- `policy.py`: ACP thresholds and scoring
- `memory.py`: bounded memory with decay and TTL
- `router.py`: mode selection and route registry
- `executor.py`: execution adapter and a deterministic demo adapter
- `executor.py`: execution adapter factory, demo adapter, and OpenAI adapter
- `critic.py`: independent review pass
- `runtime.py`: coordinator loop
- `operator.py`: breathing operator (`inhale -> hold_in -> release -> hold_out`)
- `demo.py`: runnable walkthrough

## ACP to implementation

- `dissolution_score`
  - rises when schema validity, evidence, or consistency break down
  - response: `ground`
- `crystallization_score`
  - rises when the same route dominates, memory concentration gets too high,
    and critic disagreement collapses
  - response: `diversify`
- `risk`
  - if the task remains unresolved and risky, the handler can `escalate`

## The Prigogine tax in code

The handler pays for adaptability in four concrete ways:

1. `Route decay`
   Successful routes do not get to dominate forever. Historical route scores are
   decayed on every update.

2. `Memory decay + TTL`
   Useful memories age out unless they keep proving useful. Contradicted memories
   get penalized.

3. `Exploration pressure`
   If route entropy falls and dominance rises, the handler is pushed into
   `diversify` mode.

4. `Independent critique`
   The executor can be confident while the critic stays skeptical. That gap is
   treated as signal, not noise.

## Breathing operator

The handler now has an explicit breathing cycle:

1. `inhale`
   Constrain the task by synthesis, research, and what-if generation.

2. `hold_in`
   Ponder without finalizing. Keep multiple hypotheses alive.

3. `release`
   Let competing predictions contend and allow a provisional winner to emerge.

4. `hold_out`
   Consolidate what survived release before the next inhale.

Boundary pressure can snap the system out of the nominal cycle:

- high `dissolution_score` forces an `inhale`
- high `crystallization_score` forces a `release`
- high unresolved `risk` can force `escalate`

## Quick start

From the repository root:

```bash
python3 -m agent_handler.demo
```

The demo runs a short sequence of tasks:

- routine work that trains up a dominant route
- a medium-novelty task that walks the breathing cycle
- a novel task that triggers diversification
- a high-risk task that eventually escalates

## Service quick start

The service core uses only the Python standard library plus the existing handler
code, so you can use it immediately.

Smoke-run the persisted service directly:

```bash
python3 -m agent_handler.service
```

That creates a local SQLite database at `agent_handler/agent_handler.db` and
runs one task through the breathing loop.

## Codex-native CLI

If you want to keep working from Codex without opening a separate UI, use the
CLI wrapper:

```bash
python3 -m agent_handler.cli runtime
```

The CLI defaults to the `demo` backend. To use the real OpenAI backend, either
set:

```bash
export AGENT_HANDLER_BACKEND=openai
```

or pass:

```bash
python3 -m agent_handler.cli --backend openai runtime
```

Create and run a task:

```bash
python3 -m agent_handler.cli submit \
  --description "Explore a new internal research workflow." \
  --novelty 0.7 \
  --risk 0.4 \
  --tags research workflow \
  --fields options tradeoffs recommendation successor_questions \
  --run-now
```

Inspect it later:

```bash
python3 -m agent_handler.cli list
python3 -m agent_handler.cli show <task-id>
```

Approve an escalated task:

```bash
python3 -m agent_handler.cli approve <task-id> --approver codex --notes "approved after review"
```

## OpenAI backend

The real OpenAI-backed executor lives in `executor.py` as
`OpenAIExecutionAdapter`.

Required environment:

```bash
export OPENAI_API_KEY=your_api_key_here
```

The local dependencies are installed in:

```bash
agent_handler/.venv
```

So the fastest way to run the real backend from this repo is:

```bash
source agent_handler/.venv/bin/activate
export AGENT_HANDLER_BACKEND=openai
export OPENAI_API_KEY=your_api_key_here
python -m agent_handler.cli runtime
```

Recommended backend selection:

```bash
export AGENT_HANDLER_BACKEND=openai
```

Optional tuning:

```bash
export OPENAI_MODEL=gpt-5.4-mini
export OPENAI_REASONING_EFFORT=medium
export OPENAI_MAX_OUTPUT_TOKENS=800
export OPENAI_TIMEOUT_SECONDS=60
```

The adapter uses the Responses API through the official Python client and asks
the model to return a JSON object that maps into the handler's `ActionResult`.
`OPENAI_MODEL` is configurable because the best model depends on whether you
prefer stronger reasoning or lower latency and cost.

## FastAPI layer

The HTTP layer is implemented in `api.py`, but `fastapi` and `uvicorn` are not
vendored into this repo. Install them first:

```bash
python3 -m pip install -r agent_handler/requirements.txt
```

Then start the API:

```bash
python3 -m agent_handler.api
```

Or:

```bash
AGENT_HANDLER_BACKEND=openai \
uvicorn agent_handler.api:app --host 127.0.0.1 --port 8000
```

Available endpoints:

- `GET /health`
- `GET /runtime`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `POST /tasks/{task_id}/run`
- `POST /tasks/{task_id}/approve`

Example task submission body:

```json
{
  "description": "Explore a new internal research workflow.",
  "novelty": 0.7,
  "risk": 0.4,
  "tags": ["research", "workflow"],
  "expected_fields": ["options", "tradeoffs", "recommendation", "successor_questions"],
  "run_now": true
}
```

## How to extend it

Replace `DemoExecutionAdapter` in `executor.py` with your real model and tool
adapter. The rest of the loop is already shaped around:

- ACP state estimation
- bounded memory reinforcement
- route diversification
- critic separation
- escalation hooks

If you wire this into a production stack, the first real integrations are
usually:

- ingress API
- persistent task / episode store
- telemetry for dissolution and crystallization metrics
- policy config from database or feature flags
