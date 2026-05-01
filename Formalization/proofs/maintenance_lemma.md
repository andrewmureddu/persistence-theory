# Maintenance Balance Lemma for the CDT

**Status:** partial OP-16 closure. This note supplies the maintenance-balance
condition under which Lemma 4.14's survivorship-selection pressure upgrades to
monotone reinforcement load or maintained net entropy-reducing pressure, and it
derives that condition for deficit-responsive renewal systems. It does not prove
that renewal dominance holds in every ACP system.

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

## 4. A First Model-Class Closure: Deficit-Responsive Renewal

The balance inequality in Lemma OP-16.1 becomes theorem-level, rather than a
stipulated hypothesis, in systems whose maintenance away from dissolution is
coupled to a detectable renewal channel. This does not close OP-16 in full, but
it gives a first broad class where the missing step follows from lower-level
birth-death dynamics.

Let

$$
D_t=\sum_{R\in L_t}\pi(R,t)
$$

be the pressure lost through shed mechanisms, and let

$$
U_t=
\sum_{R\in S_t}\bigl(\pi(R,t+h)-\pi(R,t)\bigr)
+\Xi(t+h)-\Xi(t)
$$

be the survivor-strengthening plus coherent-excess increment. The incoming
pressure is

$$
I_t=\sum_{R\in B_t}\pi(R,t+h).
$$

***Definition OP-16.2 (deficit-responsive renewal system).*** A maintained
birth-death mechanism system is *deficit-responsive* at time $t$ if, conditional
on $\mathcal F_t$:

1. each lost mechanism $R\in\mathcal R_t$ has a loss hazard
   $\ell_t(R)=P(R\in L_t\mid\mathcal F_t)$;
2. the loss of $R$ generates a renewal signal whose accounting assigns a
   non-overlapping entropy-contracting replacement contribution to that loss
   with probability $q_t(R)$ and expected incoming pressure $y_t(R)$, where
   $$
   y_t(R)=
   \mathbb E[\pi(B,t+h)\mid \mathcal F_t,\ R\in L_t,\ B
   \text{ is the stabilized replacement of }R];
   $$
3. survivor strengthening and coherent-excess change have conditional floor
   $\gamma_t$, meaning
   $$
   \mathbb E[U_t\mid\mathcal F_t]
   \geq
   \gamma_t
   \sum_{R\in\mathcal R_t}\ell_t(R)\pi(R,t).
   $$

The system is *renewal-dominant* at time $t$ if

$$
\sum_{R\in\mathcal R_t}\ell_t(R)q_t(R)y_t(R)
+
\mathbb E[U_t\mid\mathcal F_t]
\geq
\sum_{R\in\mathcal R_t}\ell_t(R)\pi(R,t).
$$

Using the conditional floor $\gamma_t$, a checkable sufficient form is

$$
\sum_{R\in\mathcal R_t}\ell_t(R)q_t(R)y_t(R)
\geq
(1-\gamma_t)
\sum_{R\in\mathcal R_t}\ell_t(R)\pi(R,t),
$$

which guarantees that renewal dominates expected pressure loss.

***Theorem OP-16.3 (renewal-dominant maintenance).*** In a deficit-responsive
renewal system, if renewal dominance holds at every unperturbed step
$t\mapsto t+h$, then the net entropy-reducing pressure $\Pi(t)$ is a
submartingale. If the renewal-dominance inequality holds pathwise, then
$\Pi(t)$ is monotonically non-decreasing pathwise.

*Proof.* By the hazard definition,

$$
\mathbb E[D_t\mid\mathcal F_t]
=
\sum_{R\in\mathcal R_t}\ell_t(R)\pi(R,t).
$$

The deficit-response channel gives

$$
\mathbb E[I_t\mid\mathcal F_t]
\geq
\sum_{R\in\mathcal R_t}\ell_t(R)q_t(R)y_t(R),
$$

because the right-hand side counts only the non-overlapping replacement pressure
assigned to loss events and ignores any additional spontaneous stabilizations. Renewal
dominance therefore implies

$$
\mathbb E[I_t+U_t\mid\mathcal F_t]
\geq
\mathbb E[D_t\mid\mathcal F_t].
$$

But $I_t+U_t-D_t$ is exactly $\Pi(t+h)-\Pi(t)$ by the bookkeeping identity in
Section 2. Hence

$$
\mathbb E[\Pi(t+h)-\Pi(t)\mid\mathcal F_t]\geq 0,
$$

so $\Pi(t)$ is a submartingale. The pathwise version is the same argument
without conditional expectation. ■

***Corollary OP-16.4 (unit replacement case).*** If every shed mechanism is
replaced by a new entropy-contracting mechanism whose pressure is at least the
shed pressure in conditional expectation, and if survivor/coherent excess is
non-negative in conditional expectation, then the maintained-pressure
hypothesis of the CDT core holds.

*Proof.* In Definition OP-16.2, this is the special case $q_t(R)=1$,
$y_t(R)\geq\pi(R,t)$, and $\gamma_t\geq0$ for every $R$. Therefore renewal
dominance holds and Theorem OP-16.3 applies. ■

***Corollary OP-16.5 (load renewal).*** If each shed mechanism generates at
least one newly stabilized entropy-contracting mechanism in conditional
expectation, then $|\mathcal R_t|$ is a submartingale. If the replacement count
is at least one pathwise for every shed mechanism, then the reinforcement load is
monotonically non-decreasing pathwise.

*Proof.* Replace the pressure weights in the previous argument by unit weights.
The incoming count dominates the lost count, so
$\mathbb E[|B_t|-|L_t|\mid\mathcal F_t]\geq0$. Lemma OP-16.1 gives the result.
■

This model class captures systems where maintenance is not merely preservation
of an already narrow repertoire, but active replacement of lost
entropy-contracting capacity: learned controllers that schedule a new envelope
when the old one fails, ecological or organizational routines that create
successor stabilizers after a shock, and evolving populations where selection
plus variation replenishes stabilizing traits. The condition is also falsifiable:
one can estimate loss hazards $\ell_t(R)$, replacement probabilities $q_t(R)$,
replacement pressures $y_t(R)$, and survivor/coherent increment $U_t$.

Failure of renewal dominance is informative rather than fatal. It describes a
different regime: the system may still remain away from dissolution by shrinking
to a smaller set of high-pressure mechanisms, by importing non-repertoire work,
or by accepting a lower pressure level. In those cases the CDT core can still be
applied if $\Pi(t)$ is observed or proved to be maintained, but the
deficit-responsive renewal theorem no longer supplies that fact.

## 5. Consequences for Theorem 4.17

***Corollary OP-16.6 (sufficient condition for the CDT core hypothesis).*** If
the pressure balance inequality in Lemma OP-16.1 holds pathwise along an
unperturbed trajectory, then the maintained-pressure hypothesis in Theorem
4.17(a) is satisfied. Consequently the conditional macrostate entropy
$H(m(t+h)\mid m(t))$ is monotonically non-increasing along that trajectory.

***Corollary OP-16.7 (sufficient condition for repertoire contraction).*** If
the load balance inequality $|B_t|\geq |L_t|$ holds pathwise and every newly
stabilized mechanism contributes an additional compatible intersection
constraint, then the compound reinforcement basin

$$
\bar R(t)=\bigcap_{R\in\mathcal R_t}R
$$

is monotonically non-increasing in the set-inclusion ordering.

## 6. What Remains Open

This note narrows OP-16 but does not erase it.

Closed here:

- the hidden inference from fraction enrichment to load growth is replaced by an
  explicit balance condition;
- the pressure version of the CDT is reduced to a checkable gain-loss
  inequality;
- deficit-responsive renewal systems now provide a first model class where the
  balance condition follows from explicit lower-level birth-death and
  replacement quantities;
- domain models now have a concrete target: identify $B_t$, $L_t$, survivor
  strengthening, and coherent-excess change.

Still open:

- classify which ACP systems have a deficit-response channel strong enough to be
  renewal-dominant;
- characterize when maintenance away from dissolution forces replenishment of
  entropy-contracting mechanisms rather than merely preserving an already narrow
  repertoire;
- quantify the pressure contributions $\pi(R,t)$ and $\Xi(t)$ outside the
  Gaussian and explicitly reduced domains.

Thus OP-16 is now partial: the missing theorem has a precise sufficient form and
a first renewal-dominant model-class derivation, but the generic dynamical
classification remains the live problem.
