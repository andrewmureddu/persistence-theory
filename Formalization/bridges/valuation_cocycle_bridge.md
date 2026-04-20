# Valuations, Ratio Operators, and the Arithmetic Shadow of Coordination-Neutrality

*Working bridge draft - April 2026*

---

## 1. Purpose

The operator-algebra program opened by A.20 and the coordination-neutrality addendum has reached the point where a number-theoretic entry is natural. The goal of this note is to make that entry in the most conservative possible way: not by forcing the ACP into analytic number theory prematurely, but by identifying a dyadic coordination operator whose structure is already exactly arithmetic.

The candidate is the ratio operator

$$
B_{\mathrm{rat}}(x,y) = x/y
$$

on the multiplicative group of positive rationals. This operator is coordination-neutral in the strongest possible sense, and its logarithmic lift admits a fully discrete arithmetic form through prime valuations.

The core claim of this note is modest and exact:

1. On $\mathbb{Q}_{>0}^{\times}$, the ratio operator has a canonical lift to the prime-valuation lattice $\bigoplus_p \mathbb{Z}$.
2. In that lattice, the dyadic operator becomes a swap-antisymmetric additive cocycle.
3. Tree-compositions of the ratio operator linearize exactly: the output valuation is a signed sum of the leaf valuations.

This gives an arithmetic toy model of coordination-neutral composition with no approximation and no appeal to continuum analysis. In ACP language, it is the zero-synergy baseline: a coordination-neutral operator whose multi-party composition is completely transparent. Any genuinely nonlinear coordination-neutral family should be understood relative to this arithmetic model.

What is **not** claimed here: that the ACP has already been reduced to a theorem in analytic number theory, or that A.20 has yet reached automorphic, adelic, or spectral form. This document is a bridge, not a grand unification.

---

## 2. Setup

We work on the multiplicative group of positive rationals

$$
\mathbb{Q}_{>0}^{\times}.
$$

Restricting to positive rationals avoids sign bookkeeping and keeps every valuation integer-valued with finite support.

### 2.1 The ratio operator

***Definition 2.1 (Ratio operator).*** Define

$$
B_{\mathrm{rat}} : \mathbb{Q}_{>0}^{\times} \times \mathbb{Q}_{>0}^{\times} \to \mathbb{Q}_{>0}^{\times},
\qquad
B_{\mathrm{rat}}(x,y) = x/y.
$$

This is the simplest coordination-neutral operator:

$$
B_{\mathrm{rat}}(y,x) = y/x = \frac{1}{x/y} = \frac{1}{B_{\mathrm{rat}}(x,y)}.
$$

So $B_{\mathrm{rat}}$ satisfies Definition A.20.33 of coordination-neutrality exactly.

### 2.2 Prime valuations

For each prime $p$, let

$$
v_p : \mathbb{Q}_{>0}^{\times} \to \mathbb{Z}
$$

denote the standard $p$-adic valuation:

$$
v_p\!\left(\prod_q q^{a_q}\right) = a_p,
$$

where only finitely many $a_q$ are nonzero.

***Definition 2.2 (Valuation vector).*** Define the valuation-vector map

$$
\nu : \mathbb{Q}_{>0}^{\times} \to \bigoplus_p \mathbb{Z},
\qquad
\nu(x) = (v_p(x))_p.
$$

The direct sum is crucial: every positive rational has finite prime support, so $\nu(x)$ has only finitely many nonzero coordinates.

***Proposition 2.3 (Fundamental arithmetic coordinates).*** The map $\nu$ is a group isomorphism from $\mathbb{Q}_{>0}^{\times}$ onto $\bigoplus_p \mathbb{Z}$.

*Proof.* Every $x \in \mathbb{Q}_{>0}^{\times}$ has a unique prime factorization

$$
x = \prod_p p^{a_p},
$$

with $a_p \in \mathbb{Z}$ and finite support. This identifies $x$ uniquely with the integer vector $(a_p)_p$. Multiplication of rationals adds exponents, so

$$
\nu(xy) = \nu(x) + \nu(y).
$$

Injectivity and surjectivity are both immediate from unique factorization. $\square$

*Remark 2.4 (The arithmetic pre-logarithm).* The valuation vector is the discrete arithmetic precursor of the usual real logarithm. Writing $x = \prod_p p^{a_p}$,

$$
\log x = \sum_p a_p \log p = \langle \nu(x), (\log p)_p \rangle.
$$

So the usual logarithm is obtained by weighting the valuation coordinates by $\log p$. The valuation lift therefore captures the integer arithmetic skeleton of the log-lift before any analytic weighting is applied.

---

## 3. The Arithmetic Log-Lift

The coordination-neutrality addendum studies the real log-lift

$$
L(x,y) = \log |B(x,y)|.
$$

For the ratio operator on positive rationals, there is a stronger object available.

***Definition 3.1 (Arithmetic log-lift).*** Define

$$
\Lambda_{\mathrm{rat}}(x,y) := \nu(B_{\mathrm{rat}}(x,y)) = \nu(x/y).
$$

By Proposition 2.3 this takes values in the prime-valuation lattice $\bigoplus_p \mathbb{Z}$.

***Proposition 3.2 (Difference form).*** For all $x,y \in \mathbb{Q}_{>0}^{\times}$,

$$
\Lambda_{\mathrm{rat}}(x,y) = \nu(x) - \nu(y).
$$

*Proof.* Since $\nu$ is a group homomorphism,

$$
\nu(x/y) = \nu(x) + \nu(y^{-1}) = \nu(x) - \nu(y).
$$

$\square$

***Corollary 3.3 (Swap antisymmetry).*** The arithmetic log-lift is swap-antisymmetric:

$$
\Lambda_{\mathrm{rat}}(y,x) = -\Lambda_{\mathrm{rat}}(x,y).
$$

*Proof.* Immediate from Proposition 3.2. $\square$

***Corollary 3.4 (Cocycle identity).*** For all $x,y,z \in \mathbb{Q}_{>0}^{\times}$,

$$
\Lambda_{\mathrm{rat}}(x,z) = \Lambda_{\mathrm{rat}}(x,y) + \Lambda_{\mathrm{rat}}(y,z).
$$

*Proof.* Using Proposition 3.2,

$$
\Lambda_{\mathrm{rat}}(x,y) + \Lambda_{\mathrm{rat}}(y,z)
= (\nu(x)-\nu(y)) + (\nu(y)-\nu(z))
= \nu(x)-\nu(z)
= \Lambda_{\mathrm{rat}}(x,z).
$$

$\square$

Thus the ratio operator is not merely coordination-neutral; its arithmetic lift is an exact additive cocycle on the prime lattice.

*Remark 3.5.* This is the first clean reason the ratio operator behaves differently from the exp-log bridge family of `coordination_neutrality.md`. For the ratio operator, coordination-neutrality is backed by a full linearization. For the bridge family, pairwise coordination-neutrality holds, but no corresponding exact additive arithmetic shadow has yet been identified.

---

## 4. Tree Composition Linearizes Exactly

The central obstruction in `coordination_neutrality.md` is that pairwise coordination-neutrality does not generally survive tree composition. The ratio operator is the clean baseline because its tree-compositions can be written in closed form.

Consider a full binary tree $\tau$ whose internal nodes are all labeled by $B_{\mathrm{rat}}$ and whose leaves are labeled by variables $x_1,\dots,x_n \in \mathbb{Q}_{>0}^{\times}$. Let the resulting $n$-ary output be denoted

$$
T_{\tau}(x_1,\dots,x_n).
$$

***Proposition 4.1 (Monomial normal form).*** For every such tree $\tau$, there exist signs $\varepsilon_i(\tau) \in \{+1,-1\}$ such that

$$
T_{\tau}(x_1,\dots,x_n) = \prod_{i=1}^n x_i^{\varepsilon_i(\tau)}.
$$

More precisely, if $r_i(\tau)$ is the number of right edges on the path from the root of $\tau$ to the leaf $x_i$, then

$$
\varepsilon_i(\tau) = (-1)^{r_i(\tau)}.
$$

*Proof.* Induct on the depth of the tree.

For a single leaf, the claim is trivial. Suppose $\tau$ has left and right subtrees $\tau_L,\tau_R$. By the induction hypothesis,

$$
T_{\tau_L} = \prod_{i \in L} x_i^{\varepsilon_i^L},
\qquad
T_{\tau_R} = \prod_{j \in R} x_j^{\varepsilon_j^R}.
$$

Then

$$
T_{\tau} = \frac{T_{\tau_L}}{T_{\tau_R}}
= \left(\prod_{i \in L} x_i^{\varepsilon_i^L}\right)
   \left(\prod_{j \in R} x_j^{-\varepsilon_j^R}\right),
$$

which is again of the required form. Passing through a right edge flips the sign of every exponent beneath that edge, so the path formula $\varepsilon_i(\tau)=(-1)^{r_i(\tau)}$ follows. $\square$

***Corollary 4.2 (Valuation linearization).*** For every ratio tree $\tau$,

$$
\nu(T_{\tau}(x_1,\dots,x_n)) = \sum_{i=1}^n \varepsilon_i(\tau)\,\nu(x_i).
$$

*Proof.* Apply $\nu$ to Proposition 4.1 and use Proposition 2.3. $\square$

So the entire multi-party composition problem collapses to signed vector addition in $\bigoplus_p \mathbb{Z}$.

### 4.1 The depth-2 example

For the balanced depth-2 tree,

$$
T(a,b,c,d) = B_{\mathrm{rat}}(B_{\mathrm{rat}}(a,b), B_{\mathrm{rat}}(c,d))
= \frac{a/b}{c/d}
= \frac{ad}{bc}.
$$

Hence

$$
\nu(T(a,b,c,d)) = \nu(a) - \nu(b) - \nu(c) + \nu(d).
$$

Under reversal $(a,b,c,d) \mapsto (d,c,b,a)$ this expression is unchanged, so

$$
T(d,c,b,a) = T(a,b,c,d).
$$

This matches the preliminary observation in `coordination_neutrality.md`: tree composition turns pairwise coordination-neutrality into a different symmetry class. For the ratio operator, that new symmetry is not mysterious; it is the invariance of a signed valuation sum under reversal of a symmetric sign pattern.

---

## 5. ACP Reading

The results above are purely arithmetic. Their ACP relevance is interpretive, not yet reduction-theoretic.

### 5.1 What the arithmetic model gives us

The valuation lattice provides an exact discrete model of dyadic coordination with three useful features:

1. **No hidden nonlinearity.** The dyadic operator becomes subtraction in a free abelian group.
2. **Exact compositional transparency.** Multi-party trees become signed sums, so every composed output can be read coordinate-by-coordinate prime by prime.
3. **A clean baseline for compounding.** Since the composed operator remains linear in valuation space, the ratio model exhibits no superadditive interaction term. Any future coordination-neutral family that does generate such a term will be detectable as a genuine deformation away from valuation linearity rather than as an artifact of notation.

This makes the ratio model the right arithmetic control case for the operator program.

### 5.2 A disciplined ACP interpretation

In ACP language, one may read the valuation coordinates as discrete internal modes and the ratio operator as a pure transfer law between them. The arithmetic lift then says:

- pairwise coordination is antisymmetric;
- composition preserves a signed conservation ledger;
- no new interaction information is generated by composition alone.

That last point matters. The compounding lemma in the main ACP proof chain identifies superadditive excess as the interaction information generated when coupled mechanisms constrain one another. The valuation-ratio model gives the opposite extreme: a coordination-neutral composition whose arithmetic shadow is exactly additive. It is therefore a useful baseline against which nontrivial operator families can be measured.

One plausible long-term reading is:

- **ratio / valuation model:** conservative, zero-synergy coordination;
- **nonlinear CN families:** deformations that may generate genuine interaction information;
- **A.20 / operator-algebra regime:** the noncommutative analog in which the floor is no longer additive and the Heisenberg-type obstruction appears.

That is a research program, not a theorem.

---

## 6. Rigidity of One-Dimensional Arithmetic Shadows

The ratio operator is the motivating example, but the natural mathematical question is whether it is essentially forced whenever the arithmetic shadow is one-dimensional.

In this section we give a partial answer. The result does **not** solve OP-15 in full because OP-15 allows arbitrary abelian target groups. What it does solve is the real-valued case: when the shadow can be coordinatized by a single real parameter, the operator is ratio-like up to reparameterization.

Throughout this section let $I \subseteq \mathbb{R}$ be an open interval, and let

$$
B : I \times I \to \mathbb{R}_{>0}
$$

be a $C^2$ function satisfying:

1. $B(x,x) = 1$ for all $x \in I$;
2. $B_x$ and $B_y$ are nowhere zero on $I \times I$.

The diagonal condition is the positive-branch version of Proposition A.20.37(c); the nonvanishing condition excludes stationary degeneracies and is the natural local regularity hypothesis for an additive shadow.

***Definition 6.1 (One-dimensional arithmetic shadow).*** We say that $B$ admits a **one-dimensional arithmetic shadow** if there exist:

- an injective $C^2$ map $\eta : \operatorname{im}(B) \to \mathbb{R}$ with $\eta'(b) \neq 0$ on $\operatorname{im}(B)$,
- a $C^1$ map $\psi : I \to \mathbb{R}$,

such that

$$
\eta(B(x,y)) = \psi(x) - \psi(y)
$$

for all $(x,y) \in I \times I$.

This is the real-coordinate specialization of OP-15.

***Theorem 6.2 (Mixed-derivative criterion).*** Under the hypotheses above, the following are equivalent:

**(a)** $B$ admits a one-dimensional arithmetic shadow.

**(b)** There exists a continuous function

$$
q : \operatorname{im}(B) \to \mathbb{R}
$$

such that

$$
B_{xy}(x,y) = q(B(x,y))\,B_x(x,y)\,B_y(x,y)
$$

for all $(x,y) \in I \times I$.

*Proof.*

**(a) ⇒ (b).** Let

$$
L(x,y) := \eta(B(x,y)) = \psi(x) - \psi(y).
$$

Since $L$ is a pure difference, its mixed derivative vanishes:

$$
L_{xy}(x,y) = 0.
$$

Applying the chain rule gives

$$
0 = L_{xy}
= \eta''(B)\,B_x B_y + \eta'(B)\,B_{xy}.
$$

Since $\eta'$ is nowhere zero by hypothesis, we may rearrange:

$$
B_{xy}
= -\frac{\eta''(B)}{\eta'(B)}\,B_x B_y.
$$

Hence (b) holds with

$$
q(b) = -\eta''(b)/\eta'(b).
$$

**(b) ⇒ (a).** Assume (b). Solve the scalar ODE

$$
\eta''(b) + q(b)\eta'(b) = 0
$$

on the interval $\operatorname{im}(B)$, with initial conditions chosen so that $\eta'(b) \neq 0$ everywhere and $\eta(1)=0$. Standard ODE theory gives a $C^2$ solution; explicitly,

$$
\eta'(b) = C \exp\!\left(-\int_{b_0}^b q(s)\,ds\right),
$$

so $\eta'$ never vanishes when $C \neq 0$.

Now define

$$
L(x,y) := \eta(B(x,y)).
$$

Using (b) and the ODE for $\eta$,

$$
L_{xy}
= \eta''(B)\,B_x B_y + \eta'(B)\,B_{xy}
= \bigl(\eta''(B) + q(B)\eta'(B)\bigr) B_x B_y
= 0.
$$

Therefore $L$ has vanishing mixed derivative on the rectangle $I \times I$, so

$$
L(x,y) = f(x) + g(y)
$$

for some $C^1$ functions $f,g$.

The diagonal condition $B(x,x)=1$ and the normalization $\eta(1)=0$ imply

$$
0 = L(x,x) = f(x) + g(x)
$$

for all $x$, hence $g=-f$. Setting $\psi=f$, we obtain

$$
\eta(B(x,y)) = \psi(x) - \psi(y),
$$

which is exactly (a). $\square$

***Corollary 6.3 (Ratio rigidity up to reparameterization).*** If $B$ admits a one-dimensional arithmetic shadow, then there exist:

- a positive coordinate function $r : I \to \mathbb{R}_{>0}$,
- an injective output reparameterization $\Phi$ on a positive interval,

such that

$$
B(x,y) = \Phi\!\left(\frac{r(x)}{r(y)}\right).
$$

*Proof.* By Definition 6.1,

$$
\eta(B(x,y)) = \psi(x) - \psi(y).
$$

Set

$$
r(x) := e^{\psi(x)}.
$$

Then

$$
\frac{r(x)}{r(y)} = e^{\psi(x)-\psi(y)} = e^{\eta(B(x,y))}.
$$

Define $\Phi$ on the interval $J := \exp(\eta(\operatorname{im}(B)))$ by

$$
\Phi(t) := \eta^{-1}(\log t).
$$

Since $\eta$ is injective, $\Phi$ is well-defined and injective. Substituting,

$$
B(x,y) = \Phi(r(x)/r(y)).
$$

$\square$

*Remark 6.4 (Meaning of the rigidity result).* Corollary 6.3 says that in one real shadow-coordinate there is no genuinely new dyadic geometry: every such operator is the ratio operator after changing coordinates on the inputs and outputs. The ratio operator is therefore not just an example but the normal form for the entire one-dimensional smooth theory.

*Remark 6.5 (CN in the rigid coordinates).* If $B$ is additionally coordination-neutral, then in the shadow coordinate $\eta$ inversion becomes sign reversal:

$$
\eta(1/u) = -\eta(u)
$$

for all $u \in \operatorname{im}(B)$.

Indeed, if $u = B(x,y)$ then by CN,

$$
\eta(1/u) = \eta(B(y,x)) = \psi(y)-\psi(x) = -\eta(B(x,y)) = -\eta(u).
$$

So the arithmetic shadow identifies CN with the standard additive involution $a \mapsto -a$.

*Remark 6.6 (A practical obstruction test).* Theorem 6.2 provides a usable diagnostic. Given a smooth positive operator $B$, compute

$$
Q_B(x,y) := \frac{B_{xy}(x,y)}{B_x(x,y)\,B_y(x,y)}.
$$

If $Q_B$ does not factor through $B$ alone, then no one-dimensional arithmetic shadow exists. This does not settle the full abelian-group version of OP-15, but it rules out the entire real-coordinate class immediately.

---

## 7. Finite-Dimensional Real Targets Collapse to the Scalar Case

The next question is whether allowing a higher-rank smooth real target produces genuinely new shadows. The answer is no.

Let $V$ be a finite-dimensional real vector space. Equip $V$ with any fixed linear coordinate system, so derivatives of maps into $V$ are taken componentwise.

***Definition 7.1 ($V$-valued arithmetic shadow).*** Under the standing hypotheses of Section 6, we say that $B$ admits a **$V$-valued arithmetic shadow** if there exist:

- an injective $C^2$ map $\eta : \operatorname{im}(B) \to V$ with $\eta'(b) \neq 0$ on $\operatorname{im}(B)$,
- a $C^1$ map $\psi : I \to V$,

such that

$$
\eta(B(x,y)) = \psi(x) - \psi(y)
$$

for all $(x,y) \in I \times I$.

***Theorem 7.2 (Finite-dimensional collapse).*** If $B$ admits a $V$-valued arithmetic shadow for some finite-dimensional real vector space $V$, then $\eta(\operatorname{im}(B))$ lies in an affine line in $V$.

Equivalently: every smooth finite-dimensional real-valued shadow is secretly one-dimensional.

*Proof.* Let

$$
L(x,y) := \eta(B(x,y)) = \psi(x) - \psi(y).
$$

Then $L_{xy}=0$ componentwise. By the vector-valued chain rule,

$$
0 = L_{xy}
= \eta''(B)\,B_x B_y + \eta'(B)\,B_{xy},
$$

where $\eta'(B),\eta''(B)\in V$.

Fix $b \in \operatorname{im}(B)$ and choose $(x,y)$ with $B(x,y)=b$. Since $B_x$ and $B_y$ are nonzero, define

$$
q(x,y) := -\frac{B_{xy}(x,y)}{B_x(x,y)\,B_y(x,y)}.
$$

Then the equation above reads

$$
\eta''(b) = q(x,y)\,\eta'(b).
$$

If $(x_1,y_1)$ and $(x_2,y_2)$ are two points with $B(x_i,y_i)=b$, we obtain

$$
q(x_1,y_1)\,\eta'(b) = \eta''(b) = q(x_2,y_2)\,\eta'(b).
$$

Because $\eta'(b)\neq 0$, the scalars agree. Hence $q(x,y)$ depends only on $b$; write the common value as $q(b)$. Therefore

$$
\eta''(b) = q(b)\,\eta'(b)
$$

for all $b \in \operatorname{im}(B)$.

This is a first-order scalar ODE for the vector field $\eta'$. Writing $s$ for the scalar solution of

$$
s'(b) = q(b)\,s(b),
$$

we have

$$
\eta'(b) = v\,s(b)
$$

for some fixed nonzero vector $v \in V$: indeed each component of $\eta'$ solves the same scalar ODE, so every component is a constant multiple of the same function $s$.

Integrating once,

$$
\eta(b) = \eta(b_0) + v \int_{b_0}^b s(t)\,dt.
$$

So $\eta(\operatorname{im}(B))$ is contained in the affine line

$$
\eta(b_0) + \mathbb{R}v.
$$

$\square$

***Corollary 7.3 (Reduction to the scalar normal form).*** If $B$ admits a $V$-valued arithmetic shadow for some finite-dimensional real vector space $V$, then $B$ admits a one-dimensional arithmetic shadow in the sense of Definition 6.1. Consequently,

$$
B(x,y) = \Phi\!\left(\frac{r(x)}{r(y)}\right)
$$

for suitable positive coordinate function $r$ and injective output reparameterization $\Phi$.

*Proof.* By Theorem 7.2, the image of $\eta$ lies in an affine line $\eta(b_0)+\mathbb{R}v$ with $v\neq 0$. Choose a linear functional $\ell : V \to \mathbb{R}$ such that $\ell(v)\neq 0$. Then

$$
\tilde{\eta} := \ell \circ \eta,
\qquad
\tilde{\psi} := \ell \circ \psi
$$

yield a one-dimensional arithmetic shadow:

$$
\tilde{\eta}(B(x,y)) = \tilde{\psi}(x) - \tilde{\psi}(y).
$$

Now apply Corollary 6.3. $\square$

*Remark 7.4 (Why the valuation example survives).* Theorem 7.2 kills only the smooth finite-dimensional real-target case. The prime-valuation lattice

$$
\bigoplus_p \mathbb{Z}
$$

escapes the collapse for two independent reasons:

1. it is discrete rather than smooth;
2. it has countably infinite rank rather than finite real dimension.

This is exactly why the valuation construction remains a genuinely arithmetic phenomenon rather than collapsing back into ordinary real log-coordinates.

*Remark 7.5 (What the higher-rank frontier now means).* After Theorem 7.2, the phrase "higher-rank arithmetic shadow" should no longer be read as "take values in $\mathbb{R}^m$ with $m>1$." That case is empty modulo reparameterization. The only plausible sources of genuinely new behavior are:

- discrete abelian groups;
- infinite-rank abelian groups;
- singular / non-smooth targets;
- possibly finite-dimensional abelian Lie groups with nontrivial global topology, though that extension is not treated here.

So the frontier has sharpened. The interesting higher-rank case is not differential-geometric; it is genuinely arithmetic.

---

## 8. General Abelian-Shadow Linearization

The ratio / valuation model is important not only because it is arithmetic, but because it exhibits the universal combinatorics of every additive shadow.

Let $X$ be a set, let $A$ be an abelian group, let $D \subseteq X \times X$, and let

$$
B : D \to Y
$$

be a two-slot operator. Suppose there exist maps

$$
\eta : Y \to A,
\qquad
\psi : X \to A
$$

with $\eta$ injective such that

$$
\eta(B(x,y)) = \psi(x) - \psi(y)
$$

for every $(x,y) \in D$.

This is the purely algebraic core of OP-15, stripped of smoothness assumptions and real coordinates.

***Theorem 8.1 (Tree linearization in any abelian shadow).*** Let $\tau$ be a full binary tree whose internal nodes are all labeled by $B$ and whose leaves are labeled by $x_1,\dots,x_n \in X$. Assume every intermediate composition required to evaluate the tree is defined. Then

$$
\eta(T_{\tau}(x_1,\dots,x_n)) = \sum_{i=1}^n \varepsilon_i(\tau)\,\psi(x_i),
$$

where

$$
\varepsilon_i(\tau) = (-1)^{r_i(\tau)}
$$

and $r_i(\tau)$ is the number of right edges on the path from the root to the leaf $x_i$.

*Proof.* Induct on tree depth.

For a single leaf the statement is tautological up to the choice $\varepsilon_1=+1$. Suppose $\tau$ has left and right subtrees $\tau_L,\tau_R$. By the induction hypothesis,

$$
\eta(T_{\tau_L}) = \sum_{i \in L} \varepsilon_i^L \psi(x_i),
\qquad
\eta(T_{\tau_R}) = \sum_{j \in R} \varepsilon_j^R \psi(x_j).
$$

Applying the additive-shadow identity at the root,

$$
\eta(T_{\tau})
= \eta\!\bigl(B(T_{\tau_L},T_{\tau_R})\bigr)
= \eta(T_{\tau_L}) - \eta(T_{\tau_R}).
$$

Therefore

$$
\eta(T_{\tau})
= \sum_{i \in L} \varepsilon_i^L \psi(x_i)
 - \sum_{j \in R} \varepsilon_j^R \psi(x_j),
$$

which is exactly the required sign rule: every time a leaf passes through a right edge, its sign flips. $\square$

***Corollary 8.2 (Ratio / valuation as the arithmetic normal example).*** The ratio-tree linearization of Section 4 is the specialization of Theorem 8.1 to

$$
X = Y = \mathbb{Q}_{>0}^{\times},
\qquad
A = \bigoplus_p \mathbb{Z},
\qquad
\eta = \psi = \nu.
$$

*Remark 8.3 (Why this matters for ACP).* Theorem 8.1 isolates the exact algebraic meaning of "zero-synergy coordination." Any operator with an additive abelian shadow linearizes under arbitrary binary tree composition. No new group-theoretic interaction term can appear; all structure is already present at the leaves as a signed sum. This is the abstract backdrop against which ACP-style superadditive compounding must be measured.

*Remark 8.4 (Where genuine novelty can enter).* Since Theorem 8.1 is purely algebraic, the only ways to escape its linearization are:

- the operator has no additive shadow at all;
- the shadow exists only after singular or partially defined encoding;
- the composition law forces one out of the shadow's regular domain;
- or the relevant target is nonabelian / nonadditive.

These are precisely the places where a true interaction-information geometry can begin.

---

## 9. The Discrete Arithmetic Frontier: Valuation-Type Shadows

The preceding sections show that the smooth real-target regime is exhausted and that any additive abelian shadow linearizes tree composition. What remains is to state the genuinely arithmetic case in a form number theorists will recognize immediately.

The right setting is a free commutative arithmetic state space indexed by primes.

### 9.1 Free arithmetic state spaces

Let $P$ be a countable index set, thought of as a prime system. Define:

$$
M(P) := \bigoplus_{p \in P} \mathbb{N},
\qquad
K(P) := \bigoplus_{p \in P} \mathbb{Z}.
$$

We write elements multiplicatively:

$$
x = \prod_{p \in P} p^{a_p},
\qquad
a_p \in \mathbb{N} \text{ or } \mathbb{Z},
$$

with finite support in either case. Then $M(P)$ is the free commutative monoid on $P$, and $K(P)$ is its Grothendieck group completion.

For the ordinary prime system $P = \{\text{rational primes}\}$:

- $M(P)$ is the multiplicative monoid $\mathbb{N}_{>0}^{\times}$ of positive integers;
- $K(P)$ is the multiplicative group $\mathbb{Q}_{>0}^{\times}$ of positive rationals.

The canonical valuation map is simply the identity under this coordinatization:

$$
\nu_P : K(P) \to \bigoplus_{p \in P} \mathbb{Z},
\qquad
\nu_P\!\left(\prod_p p^{a_p}\right) = (a_p)_p.
$$

### 9.2 Weighted valuation differences

Let $A$ be an abelian group.

***Proposition 9.1 (Support-finite weight decomposition).*** Every group homomorphism

$$
\chi : K(P) \to A
$$

is uniquely determined by the weight family

$$
w_p := \chi(p) \in A,
\qquad p \in P,
$$

and satisfies

$$
\chi\!\left(\prod_p p^{a_p}\right) = \sum_p a_p w_p
$$

for all $(a_p)_p \in \bigoplus_{p \in P} \mathbb{Z}$. Conversely, every choice of weights $\{w_p\}_{p \in P}$ defines a unique group homomorphism in this way.

*Proof.* Since $K(P)$ is the free abelian group on the basis $P$, this is exactly its universal property. Finite support ensures the sum is finite. $\square$

***Definition 9.2 (Valuation-type shadow).*** Let $B$ be a two-slot operator on a domain contained in $K(P)\times K(P)$. We say that $B$ admits a **valuation-type shadow** if there exist:

- an abelian group $A$,
- an injective encoding $\eta : \operatorname{im}(B) \to A$,
- a group homomorphism $\chi : K(P) \to A$,

such that

$$
\eta(B(x,y)) = \chi(x) - \chi(y)
$$

for all $(x,y)$ in the regular domain.

This is the number-theoretically natural discrete subclass of OP-15: the coordinate map is additive on the arithmetic state space itself.

***Theorem 9.3 (Classification of valuation-type shadows).*** Every valuation-type shadow on $K(P)$ is a weighted valuation-difference shadow. Explicitly: there exists a unique family of weights $\{w_p\}_{p \in P} \subseteq A$ such that

$$
\eta(B(x,y)) = \sum_{p \in P} \bigl(v_p(x) - v_p(y)\bigr)\,w_p
$$

for all $(x,y)$ in the regular domain.

*Proof.* By Definition 9.2 the shadow is determined by a group homomorphism $\chi : K(P) \to A$. Proposition 9.1 gives unique weights $w_p = \chi(p)$ with

$$
\chi(x) = \sum_p v_p(x)\,w_p.
$$

Therefore

$$
\eta(B(x,y))
= \chi(x) - \chi(y)
= \sum_p \bigl(v_p(x)-v_p(y)\bigr)\,w_p.
$$

$\square$

So the discrete additive arithmetic frontier already has a clean normal form: any valuation-type shadow is just a weighted prime ledger.

### 9.3 Primitive rigidity

The weighted valuation shadow still permits compressive or oblique coordinates. The primitive case removes that ambiguity.

***Definition 9.4 (Primitive valuation-type shadow).*** A valuation-type shadow is **primitive** if the weight family $\{w_p\}_{p \in P}$ forms a basis of a free abelian subgroup

$$
H := \langle w_p : p \in P \rangle \leq A.
$$

***Corollary 9.5 (Primitive discrete rigidity).*** Every primitive valuation-type shadow is equivalent to the canonical valuation shadow up to a target-group isomorphism. More precisely: there is a unique group isomorphism

$$
T : H \xrightarrow{\sim} \bigoplus_{p \in P} \mathbb{Z}
$$

satisfying $T(w_p)=e_p$ for every $p \in P$, and under this isomorphism

$$
T(\eta(B(x,y))) = \nu_P(x) - \nu_P(y).
$$

*Proof.* Since $\{w_p\}_{p \in P}$ is by hypothesis a basis of the free abelian group $H$, there is a unique isomorphism $T$ carrying $w_p$ to the standard basis vector $e_p$. Applying $T$ to Theorem 9.3 gives

$$
T(\eta(B(x,y)))
= \sum_p \bigl(v_p(x)-v_p(y)\bigr)e_p
= \nu_P(x)-\nu_P(y).
$$

$\square$

*Remark 9.6 (What has and has not been classified).* Theorem 9.3 and Corollary 9.5 do **not** solve the entire discrete/infinite-rank problem. They solve the valuation-type subproblem: once the coordinate map is required to be additive on the arithmetic state space, every shadow is weighted valuation difference, and the primitive case is canonically the usual prime-valuation picture. What remains open is whether there exist genuinely non-valuation additive shadows in discrete/infinite-rank settings, or whether the only surviving examples are of weighted-valuation type.

*Remark 9.7 (Why this is number-theoretic rather than merely algebraic).* On free arithmetic state spaces, the additive coordinates are not abstract labels; they are exactly prime-exponent ledgers. The primitive rigidity corollary says that the canonical valuation map is not an arbitrary choice of coordinates but the universal normal form for primitive discrete additive shadows. This is the discrete analog of the ratio normal form proved in Sections 6–7.

### 9.4 Factor-respecting rigidity

The valuation-type hypothesis in Definition 9.2 is strong: it requires the one-variable coordinate map on the arithmetic state space to be a group homomorphism from the start. The next question is whether that hypothesis is forced by weaker number-theoretic regularity.

The answer is yes for the most natural unique-factorization compatibility conditions.

***Definition 9.8 (Factor-respecting arithmetic coordinate).*** Let $A$ be an abelian group, and let

$$
\psi : K(P) \to A
$$

be any map. We say that $\psi$ is **factor-respecting** if:

1. (**orthogonal-support additivity**) whenever $x,y \in K(P)$ have disjoint prime supports,
   $$
   \operatorname{supp}(x) \cap \operatorname{supp}(y) = \varnothing,
   $$
   one has
   $$
   \psi(xy) = \psi(x) + \psi(y);
   $$
2. (**prime-ray additivity**) for every prime $p \in P$ and every $m,n \in \mathbb{Z}$,
   $$
   \psi(p^{m+n}) = \psi(p^m) + \psi(p^n).
   $$

Condition (1) says the coordinate map does not create interaction terms between distinct prime sectors. Condition (2) says that along each single-prime ray, exponent composition is already additive.

***Theorem 9.9 (Unique-factorization rigidity).*** Let $B$ be a two-slot operator on a regular domain contained in $K(P)\times K(P)$. Assume there exist:

- an abelian group $A$,
- an injective encoding $\eta : \operatorname{im}(B) \to A$,
- a factor-respecting map $\psi : K(P) \to A$,

such that

$$
\eta(B(x,y)) = \psi(x) - \psi(y)
$$

for all $(x,y)$ in the regular domain. Then $\psi$ is automatically a group homomorphism. Equivalently: there exists a unique weight family $\{w_p\}_{p \in P} \subseteq A$ such that

$$
\psi(x) = \sum_{p \in P} v_p(x)\,w_p
$$

for all $x \in K(P)$, and hence

$$
\eta(B(x,y)) = \sum_{p \in P} \bigl(v_p(x)-v_p(y)\bigr)\,w_p.
$$

In particular, every additive shadow whose one-variable coordinate respects unique factorization is valuation-type.

*Proof.* Fix $p \in P$, and write

$$
w_p := \psi(p).
$$

By prime-ray additivity with $m=n=0$,

$$
\psi(1)=\psi(p^0)=\psi(p^0)+\psi(p^0)=2\psi(1),
$$

so $\psi(1)=0$.

Again by prime-ray additivity, the map $n \mapsto \psi(p^n)$ is a group homomorphism $\mathbb{Z}\to A$. Indeed, for $n \geq 1$ an induction gives

$$
\psi(p^n)=n\,w_p,
$$

and for $n<0$ one has

$$
0=\psi(1)=\psi(p^n p^{-n})=\psi(p^n)+\psi(p^{-n}),
$$

so $\psi(p^{-n})=-\psi(p^n)=(-n)w_p$ as well. Therefore

$$
\psi(p^n)=n\,w_p
$$

for every $n \in \mathbb{Z}$.

Now let

$$
x=\prod_{p \in P} p^{a_p} \in K(P)
$$

with finite support. Repeated use of orthogonal-support additivity across the distinct prime factors gives

$$
\psi(x)=\sum_{p \in P} \psi(p^{a_p}).
$$

Substituting the prime-ray formula,

$$
\psi(x)=\sum_{p \in P} a_p w_p
= \sum_{p \in P} v_p(x)\,w_p.
$$

This is exactly the weighted valuation form, and it is unique because the weights are determined by $w_p=\psi(p)$. The displayed formula shows that $\psi$ is a group homomorphism $K(P)\to A$. Substituting into the shadow identity gives the final formula for $\eta(B(x,y))$. $\square$

***Corollary 9.10 (Where exotic shadows must break arithmetic structure).*** Any additive shadow on $K(P)$ that is **not** valuation-type must fail at least one of the two factor-respecting conditions of Definition 9.8. Concretely: every genuinely non-valuation shadow must either

- mix disjoint prime sectors in a way that violates orthogonal-support additivity, or
- distort at least one single-prime exponent ray so that $\psi(p^{m+n}) \neq \psi(p^m)+\psi(p^n)$ for some $m,n$.

*Proof.* Immediate contrapositive of Theorem 9.9. $\square$

*Remark 9.11 (What this sharpens).* Theorem 9.9 does not close OP-15, because OP-15 does not assume any arithmetic regularity on $\psi$. What it does do is identify the exact symmetry an exotic example must violate. Any non-valuation additive shadow on a free arithmetic state space must already abandon unique-factorization separability at the one-variable level; novelty can no longer hide inside a factor-respecting coordinate map.

### 9.5 First exclusion: the exp-log bridge family

Theorem 9.9 becomes more informative once it is converted into an operator-level test. The key observation is that valuation-type shadows force the operator to be constant on ratio classes.

***Proposition 9.12 (Valuation-type shadows are ratio-class constant).*** Let $B$ be a two-slot operator on a regular domain $D \subseteq K(P)\times K(P)$. Assume $B$ admits a valuation-type shadow

$$
\eta(B(x,y)) = \chi(x) - \chi(y)
$$

with $\eta$ injective and $\chi : K(P)\to A$ a group homomorphism. If $(x_1,y_1),(x_2,y_2)\in D$ satisfy

$$
x_1/y_1 = x_2/y_2,
$$

then

$$
B(x_1,y_1)=B(x_2,y_2).
$$

*Proof.* Since $\chi$ is a homomorphism,

$$
\eta(B(x,y))=\chi(x)-\chi(y)=\chi(x/y).
$$

So if $x_1/y_1=x_2/y_2$, then

$$
\eta(B(x_1,y_1))=\chi(x_1/y_1)=\chi(x_2/y_2)=\eta(B(x_2,y_2)).
$$

Injectivity of $\eta$ gives the claim. $\square$

***Corollary 9.13 (Factor-respecting shadows are ratio-class constant).*** Under the hypotheses of Theorem 9.9, the operator $B$ is ratio-class constant on its regular domain.

*Proof.* Combine Theorem 9.9 with Proposition 9.12. $\square$

This gives a direct obstruction test: to rule out factor-respecting arithmetic shadows, it is enough to exhibit two regular input pairs with the same ratio but different operator output.

We can now apply this to the bridge family from `coordination_neutrality.md`.

***Proposition 9.14 (Bridge-family obstruction under factor-respecting shadows).*** Fix $\alpha,\lambda>0$ and consider the coordination-neutral bridge family

$$
B_{\alpha,\lambda}(x,y)
=
\frac{e^{\alpha x}-\lambda \ln y}{e^{\alpha y}-\lambda \ln x}
$$

on its regular positive domain

$$
R_{\alpha,\lambda}
:=
\left\{
(x,y)\in \mathbb{R}_{>0}^2 :
e^{\alpha x}-\lambda \ln y >0,\;
e^{\alpha y}-\lambda \ln x >0
\right\}.
$$

For every $r\neq 1$, the function

$$
f_r(y):=B_{\alpha,\lambda}(ry,y)
$$

is non-constant on every interval on which it is defined. Consequently, the restriction of $B_{\alpha,\lambda}$ to the full arithmetic regular domain

$$
R_{\alpha,\lambda}\cap (\mathbb{Q}_{>0}^{\times})^2
$$

cannot admit a factor-respecting arithmetic shadow.

*Proof.* Fix $r\neq 1$. Suppose for contradiction that $f_r(y)\equiv C$ on a nontrivial interval $I$ where it is defined. Then for every $y\in I$,

$$
e^{\alpha r y}-\lambda \ln y
=
C\bigl(e^{\alpha y}-\lambda \ln(ry)\bigr)
=
C e^{\alpha y} - C\lambda \ln r - C\lambda \ln y.
$$

Rearranging,

$$
e^{\alpha r y} - C e^{\alpha y} + \lambda(C-1)\ln y + C\lambda \ln r = 0
$$

for all $y\in I$.

But for $r\neq 1$ the four functions

$$
e^{\alpha r y}, \qquad e^{\alpha y}, \qquad \ln y, \qquad 1
$$

are linearly independent on every interval in $(0,\infty)$, so the displayed identity is impossible. Therefore $f_r$ is non-constant on every interval of definition.

Because $R_{\alpha,\lambda}$ is open and contains the diagonal point $(1,1)$, there exists a rational $r\neq 1$ sufficiently close to $1$ such that the ratio ray

$$
y \longmapsto (ry,y)
$$

meets $R_{\alpha,\lambda}$ in a nontrivial open interval $I_r$. By the first part, $f_r$ is non-constant on $I_r$. Since $\mathbb{Q}$ is dense in $\mathbb{R}$, there exist distinct rationals $y_1,y_2\in I_r$ with

$$
f_r(y_1)\neq f_r(y_2).
$$

Then $(ry_1,y_1)$ and $(ry_2,y_2)$ are two rational regular pairs with the same ratio $r$ but different bridge-family outputs. Corollary 9.13 says this is impossible for any factor-respecting arithmetic shadow. Therefore no such shadow exists on

$$
R_{\alpha,\lambda}\cap (\mathbb{Q}_{>0}^{\times})^2.
$$

$\square$

*Remark 9.15 (What has been ruled out).* Proposition 9.14 does **not** show that the bridge family has no additive shadow whatsoever. It rules out the factor-respecting arithmetic subclass singled out by Theorem 9.9. So if the bridge family has any arithmetic shadow at all, it must already violate unique-factorization separability by coupling prime sectors or distorting at least one prime ray.

### 9.6 Canonical defect decomposition

The preceding results tell us what must fail in any genuinely exotic arithmetic shadow. The next step is to package that failure canonically.

Let

$$
\psi : K(P)\to A
$$

be any map into an abelian group. Since additive shadows only depend on differences $\psi(x)-\psi(y)$, a constant shift of $\psi$ is irrelevant. So there is no loss in imposing the normalization

$$
\psi(1)=0.
$$

With that normalization, every arithmetic coordinate map admits a canonical decomposition into:

1. a valuation-type baseline determined by the prime weights $\psi(p)$;
2. a sum of single-prime ray defects; and
3. a cross-prime mixing defect.

***Definition 9.16 (Prime weights, ray defects, and mixing defect).*** Let $\psi : K(P)\to A$ satisfy $\psi(1)=0$.

For each prime $p\in P$, define the **prime weight**

$$
w_p := \psi(p).
$$

For each $p\in P$ and $n\in\mathbb{Z}$, define the **ray defect**

$$
R_{\psi,p}(n) := \psi(p^n) - n\,w_p.
$$

For each

$$
x=\prod_{p\in P} p^{a_p}\in K(P),
\qquad \operatorname{supp}(x)=\{p:a_p\neq 0\},
$$

define the **mixing defect**

$$
M_\psi(x)
:=
\psi(x)-\sum_{p\in \operatorname{supp}(x)} \psi\!\left(p^{v_p(x)}\right).
$$

Here $n\,w_p$ denotes repeated addition in the abelian group $A$ for $n>0$, its inverse for $n<0$, and $0$ for $n=0$.

***Theorem 9.17 (Exact defect decomposition).*** Every normalized map $\psi : K(P)\to A$ satisfies

$$
\psi(x)
=
\sum_{p\in \operatorname{supp}(x)} v_p(x)\,w_p
\;+\;
\sum_{p\in \operatorname{supp}(x)} R_{\psi,p}\!\bigl(v_p(x)\bigr)
\;+\;
M_\psi(x)
$$

for every $x\in K(P)$.

Equivalently: every arithmetic coordinate is exactly

$$
\text{valuation ledger} + \text{ray distortion} + \text{prime mixing}.
$$

*Proof.* By Definition 9.16,

$$
\psi(x)
=
\sum_{p\in \operatorname{supp}(x)} \psi\!\left(p^{v_p(x)}\right)
\;+\;
M_\psi(x).
$$

For each prime in the support,

$$
\psi\!\left(p^{v_p(x)}\right)
=
v_p(x)\,w_p + R_{\psi,p}\!\bigl(v_p(x)\bigr).
$$

Substituting this into the first display yields the claimed formula. $\square$

***Corollary 9.18 (Factor-respecting iff defects vanish).*** A normalized map $\psi : K(P)\to A$ is factor-respecting in the sense of Definition 9.8 if and only if both of the following hold:

1. $R_{\psi,p}(n)=0$ for every prime $p$ and every $n\in\mathbb{Z}$;
2. $M_\psi(x)=0$ for every $x\in K(P)$.

*Proof.* If $\psi$ is factor-respecting, then prime-ray additivity gives

$$
\psi(p^n)=n\,\psi(p)=n\,w_p,
$$

so every ray defect vanishes. Orthogonal-support additivity, applied recursively across the finite prime support of $x$, gives

$$
\psi(x)=\sum_{p\in \operatorname{supp}(x)} \psi\!\left(p^{v_p(x)}\right),
$$

so every mixing defect vanishes.

Conversely, if all ray defects and all mixing defects vanish, then

$$
\psi(p^n)=n\,w_p
$$

for every prime $p$ and integer $n$, which is exactly prime-ray additivity. If $x$ and $y$ have disjoint prime supports, then using vanishing of the mixing defect on $x$, $y$, and $xy$,

$$
\psi(xy)
=
\sum_{p\in \operatorname{supp}(xy)} \psi\!\left(p^{v_p(xy)}\right)
=
\sum_{p\in \operatorname{supp}(x)} \psi\!\left(p^{v_p(x)}\right)

+\sum_{p\in \operatorname{supp}(y)} \psi\!\left(p^{v_p(y)}\right)
=
\psi(x)+\psi(y).
$$

So $\psi$ is factor-respecting. $\square$

***Proposition 9.19 (Shadow = valuation baseline + defect coboundary).*** Let

$$
\eta(B(x,y)) = \psi(x)-\psi(y)
$$

be any additive shadow on a regular domain contained in $K(P)\times K(P)$, with $\psi(1)=0$. Define the **total defect**

$$
\Delta_\psi(x)
:=
\sum_{p\in \operatorname{supp}(x)} R_{\psi,p}\!\bigl(v_p(x)\bigr)
\;+\;
M_\psi(x).
$$

Then

$$
\eta(B(x,y))
=
\sum_{p\in P}\bigl(v_p(x)-v_p(y)\bigr)\,w_p
\;+\;
\Delta_\psi(x)-\Delta_\psi(y),
$$

where $w_p=\psi(p)$ and the sum over $P$ is finite because $x$ and $y$ have finite support.

*Proof.* Apply Theorem 9.17 to $\psi(x)$ and $\psi(y)$ separately and subtract. $\square$

*Remark 9.20 (Meaning of the decomposition).* Proposition 9.19 says that every additive arithmetic shadow splits exactly into:

- a canonical weighted-valuation ledger, and
- a defect coboundary measuring how the coordinate map fails to respect unique factorization.

So the remaining OP-15 frontier is no longer amorphous. Any exotic additive shadow must be detected by a nonzero defect term $\Delta_\psi$.

*Remark 9.21 (Bridge-family consequence).* Proposition 9.14 now has a sharper reading. If the exp-log bridge family admits any additive arithmetic shadow on its rational regular domain, then in every such shadow the defect term $\Delta_\psi$ is nonzero somewhere. Equivalently: the bridge family's only possible arithmetic shadows are those with genuine ray distortion or prime mixing.

---

## 10. Open Problem

The obvious next question is whether the ratio operator is exceptional or merely the first member of a larger arithmetic class.

**Open problem (arithmetic shadows of coordination-neutral operators).** Characterize the coordination-neutral operators

$$
B : D \subseteq \mathbb{R}_{>0}^2 \to \mathbb{R}_{>0}
$$

for which there exist:

1. an abelian group $G$,
2. an injective encoding $\eta : \operatorname{im}(B) \to G$,
3. a coordinate map $\psi$ on the one-variable input space,

such that

$$
\eta(B(x,y)) = \psi(x) - \psi(y)
$$

on the regular domain.

For the ratio operator, one may take

$$
G = \bigoplus_p \mathbb{Z},
\qquad
\eta = \nu,
\qquad
\psi = \nu.
$$

Sections 9.2-9.6 show that a large natural subclass is already rigid: valuation-type shadows are weighted prime ledgers, primitive ones are canonically the usual valuation picture, any shadow whose one-variable coordinate respects unique factorization is automatically valuation-type, the exp-log bridge family is ruled out from that factor-respecting subclass, and every additive shadow decomposes exactly into a valuation baseline plus a defect coboundary. So the remaining frontier is now more specific than before. A genuinely exotic example, if one exists at all, must violate unique-factorization separability by mixing prime sectors or by distorting the additive structure along at least one prime ray, and that violation is measured explicitly by the defect term $\Delta_\psi$.

The bridge family of `coordination_neutrality.md` is pairwise coordination-neutral but appears not to admit such a lift in any obvious way. Determining whether that failure is essential, or whether a more subtle arithmetic shadow exists after reparameterization, is the natural frontier.

This is the point at which experts in valuation theory, multiplicative number theory, and operator algebras can engage the ACP program on clean mathematical ground.

---

## 11. Status

**Proved here.**

- The ratio operator on $\mathbb{Q}_{>0}^{\times}$ is coordination-neutral.
- Its arithmetic lift is the prime-valuation difference cocycle.
- Tree-compositions of the ratio operator linearize exactly in valuation space.
- In the one-dimensional smooth real-coordinate case, additive arithmetic shadows are classified by the mixed-derivative criterion of Theorem 6.2.
- Every one-dimensional smooth arithmetic-shadow operator is ratio-like up to input/output reparameterization (Corollary 6.3).
- Every smooth finite-dimensional real-vector-valued arithmetic shadow collapses to the scalar case (Theorem 7.2 and Corollary 7.3).
- Any additive abelian shadow linearizes tree composition as a signed sum in the target group (Theorem 8.1).
- Any valuation-type shadow on a free arithmetic state space is a weighted valuation-difference shadow (Theorem 9.3).
- Any primitive valuation-type shadow is canonically equivalent to the usual prime-valuation shadow up to target-group isomorphism (Corollary 9.5).
- Any additive shadow on a free arithmetic state space whose one-variable coordinate respects unique factorization is automatically valuation-type (Theorem 9.9).
- The exp-log bridge family is excluded from the factor-respecting arithmetic-shadow class because it is not ratio-class constant on the arithmetic domain (Proposition 9.14).
- Any additive arithmetic shadow decomposes exactly into a weighted-valuation baseline plus a defect coboundary built from ray distortion and prime mixing (Proposition 9.19).

**Not proved here.**

- Any ACP reduction theorem for number theory.
- Any extension from the smooth finite-dimensional real-target case to genuinely arithmetic targets such as discrete or infinite-rank abelian groups.
- Any proof that every discrete/infinite-rank additive shadow is valuation-type.
- Any extension from the ratio operator to the exp-log bridge family.
- Any adelic, automorphic, spectral, or zeta-function formulation.
- Any derivation of A.20's operator-algebraic floor from arithmetic data.

Those remain downstream.
