# Maintenance Balance Lemma for the CDT

**Status:** partial OP-16 closure. This note supplies sufficient dynamical
conditions under which Lemma 4.14's survivorship-selection pressure upgrades to
monotone reinforcement load or maintained net entropy-reducing pressure. It does
not prove that those conditions hold in every ACP system.

**Companion documents:** `paper/acp_main_v10.md` Section 4.4,
`proofs/crystallization_drift_theorem.md`, `OPEN_PROBLEMS.md` OP-16.

---

## 1. The Gap

Lemma 4.14 says that self-reinforcing patterns have a survivorship advantage.
Under fixed-composition or ordered birth-death assumptions, it gives monotone
growth of the expected self-reinforcing fraction

$$
f_{\mathrm{SR}}(t)=|\mathcal R(t)|/|A(t)|.
$$

The repertoire-geometry layer of the CDT needs more:

1. monotone non-decrease of the active self-reinforcing load
   $|\mathcal R(t)|$; or
2. monotone non-decrease of the net entropy-reducing pressure
   $\Pi(t)$.

Fraction growth does not imply either statement. A system can shed patterns
overall while becoming more dominated by self-reinforcing survivors. The missing
lemma is therefore a maintenance or replenishment condition, not another
selection-fraction argument.

## 2. Step Accounting

Work in discrete operational steps $t \mapsto t+h$ at a fixed coarse-graining
scale. Let $\mathcal F_t$ be the history available at time $t$.

Let

- $\mathcal R_t$ be the active entropy-contracting self-reinforcing repertoire;
- $L_t \subseteq \mathcal R_t$ be the mechanisms lost over the step;
- $B_t$ be the newly stabilized entropy-contracting self-reinforcing mechanisms
  over the step;
- $S_t=\mathcal R_t\setminus L_t$ be the surviving mechanisms.

Then

$$
\mathcal R_{t+h}=S_t\cup B_t,
\qquad
|\mathcal R_{t+h}|-|\mathcal R_t|=|B_t|-|L_t|.
$$

For pressure, use the decomposition from Definition 4.11a:

$$
\Pi(t)=\sum_{R\in\mathcal R_t}\pi(R,t)+\Xi(t),
$$

where $\pi(R,t)\geq 0$ is the one-step entropy-reduction contribution of
mechanism $R$ and $\Xi(t)\geq 0$ is the coherent excess from compatible
interactions. The pressure increment decomposes exactly as

$$
\begin{aligned}
\Pi(t+h)-\Pi(t)
&=
\sum_{R\in S_t}\bigl(\pi(R,t+h)-\pi(R,t)\bigr)\\
&\quad + \sum_{R\in B_t}\pi(R,t+h)
- \sum_{R\in L_t}\pi(R,t)
+ \bigl(\Xi(t+h)-\Xi(t)\bigr).
\end{aligned}
$$

This identity is the useful bookkeeping object. It separates four effects:
surviving mechanisms strengthen or weaken, new mechanisms enter, old mechanisms
are lost, and coherent excess changes.

## 3. Maintenance Balance Lemma

***Lemma OP-16.1 (maintenance balance).*** In the setup above:

1. If
   $$
   \mathbb E[|B_t|-|L_t|\mid\mathcal F_t]\geq 0
   $$
   for each step, then the active reinforcement load
   $|\mathcal R_t|$ is a submartingale. If the inequality holds pathwise, then
   $|\mathcal R_t|$ is monotonically non-decreasing pathwise.

2. If
   $$
   \mathbb E[\Pi(t+h)-\Pi(t)\mid\mathcal F_t]\geq 0
   $$
   for each step, then the net entropy-reducing pressure $\Pi(t)$ is a
   submartingale. If the inequality holds pathwise, then $\Pi(t)$ is
   monotonically non-decreasing pathwise.

3. In particular, the pressure condition is implied by the explicit balance
   inequality
   $$
   \mathbb E\!\left[
   \sum_{R\in B_t}\pi(R,t+h)
   +\sum_{R\in S_t}\bigl(\pi(R,t+h)-\pi(R,t)\bigr)
   +\Xi(t+h)-\Xi(t)
   \,\middle|\,\mathcal F_t
   \right]
   \geq
   \mathbb E\!\left[
   \sum_{R\in L_t}\pi(R,t)
   \,\middle|\,\mathcal F_t
   \right].
   $$

*Proof.* The load identity gives
$|\mathcal R_{t+h}|-|\mathcal R_t|=|B_t|-|L_t|$. Taking conditional expectation
proves the submartingale statement, and the pathwise statement is immediate.

For pressure, substitute the exact decomposition of
$\Pi(t+h)-\Pi(t)$ and take conditional expectation. The displayed balance
inequality is precisely the condition that expected incoming pressure, survivor
strengthening, and change in coherent excess compensate for expected pressure
lost through shed mechanisms. The pathwise version is again immediate. ■

## 4. Consequences for Theorem 4.17

***Corollary OP-16.2 (sufficient condition for the CDT core hypothesis).*** If
the pressure balance inequality in Lemma OP-16.1 holds pathwise along an
unperturbed trajectory, then the maintained-pressure hypothesis in Theorem
4.17(a) is satisfied. Consequently the conditional macrostate entropy
$H(m(t+h)\mid m(t))$ is monotonically non-increasing along that trajectory.

***Corollary OP-16.3 (sufficient condition for repertoire contraction).*** If
the load balance inequality $|B_t|\geq |L_t|$ holds pathwise and every newly
stabilized mechanism contributes an additional compatible intersection
constraint, then the compound reinforcement basin

$$
\bar R(t)=\bigcap_{R\in\mathcal R_t}R
$$

is monotonically non-increasing in the set-inclusion ordering.

## 5. What Remains Open

This note narrows OP-16 but does not erase it.

Closed here:

- the hidden inference from fraction enrichment to load growth is replaced by an
  explicit balance condition;
- the pressure version of the CDT is reduced to a checkable gain-loss
  inequality;
- domain models now have a concrete target: identify $B_t$, $L_t$, survivor
  strengthening, and coherent-excess change.

Still open:

- derive the balance inequality from primitive ACP assumptions in useful system
  classes;
- characterize when maintenance away from dissolution forces replenishment of
  entropy-contracting mechanisms rather than merely preserving an already narrow
  repertoire;
- quantify the pressure contributions $\pi(R,t)$ and $\Xi(t)$ outside the
  Gaussian and explicitly reduced domains.

Thus OP-16 is now partial: the missing theorem has a precise sufficient form,
but the generic dynamical derivation remains the live problem.
