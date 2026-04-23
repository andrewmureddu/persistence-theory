# Second-Pass Literature Scan: Structural Neighbors of ACP/CDT and the Restraint-Power Law

*Date:* 2026-04-22
*Status:* research memo

---

## Purpose

This note ranks existing domain-native results by structural proximity to four claims in the project:

- **ACP:** persistent systems occupy a non-degenerate interval between dissolution and overclosure.
- **CDT:** stabilizing mechanisms progressively narrow future options and can harden into rigidity.
- **Restraint-Power (RP):** as a persistent composite approaches its coordination floor, the most concentrated or most load-bearing subsystem must change first, and that change must be decodable by the rest of the system.
- **Vulnerable-Margin (VM):** failure often first appears at the weakest coupling, edge, or interface rather than at the center.

This is not an equivalence hunt. The aim is to separate:

- **Direct analogs:** results that instantiate most of the structure in domain-native form.
- **Strong partial analogs:** results that capture one major slice of the structure cleanly, but not the whole pattern.
- **Adjacent neighbors:** results that illuminate a nearby tradeoff or limit without matching the project's architecture tightly.

---

## Bottom Line

No single existing theorem found in this pass captures the full ACP + CDT + RP + VM package at once.

The closest matches split by component:

- **Best RP analogs:** Weingast on self-enforcing limits, Ikenberry on strategic restraint, anti-windup / actuator saturation, and AIMD congestion avoidance.
- **Best ACP/CDT analogs:** Brummitt-D'Souza-Leicht on optimal interdependence, HOT, March on exploration/exploitation, Arthur on path dependence, and Holling on resilience.
- **Best VM analogs:** Motter-Lai on cascade from key nodes, Buldyrev et al. on interdependent-network collapse, and hybrid percolation / k-core style collapse.

The strongest recurring pattern is therefore **not** a single theorem already waiting under another name, but a three-way distribution:

1. governance, commitment, and control literatures are best for "the strongest must restrain itself, visibly";
2. robustness-fragility and learning/lock-in literatures are best for "stabilization causes rigidity";
3. cascade and percolation literatures are best for "failure manifests first at the margin".

---

## Tier A: Closest Structural Analogs

| Result / mechanism | Field | Structural pattern | Best fit | Assessment |
|---|---|---|---|---|
| [The Political Foundations of Democracy and the Rule of the Law](https://www.cambridge.org/core/journals/american-political-science-review/article/political-foundations-of-democracy-and-the-rule-of-the-law/564FB92EE1808897FD0041E25289CF1F) | Political theory | Stable order requires the sovereign to remain within self-enforcing limits, and those limits must be legible enough for citizens to coordinate on enforcement. | `RP` | Closest match to the full RP structure. The most powerful actor must limit itself first, and the limit only works if it is publicly decodable. Weak on CDT except indirectly. |
| [After Victory: institutions, strategic restraint, and the rebuilding of order after major wars](https://collaborate.princeton.edu/en/publications/after-victory-institutions-strategic-restraint-and-the-rebuilding/) | IR / institutional order | Durable order emerges when a hegemon binds and restrains itself through institutions, making commitments credible to weaker states. | `RP + CDT` | Another strong RP analog. The dominant actor must move first, and visible self-binding is what stabilizes the wider system. Also hints at CDT because successful order gets institutionalized and harder to alter. |
| [Anti-windup / actuator saturation](https://www.sciencedirect.com/science/article/abs/pii/S0167691104000167) | Control theory | The controller's own effort can destabilize the system once actuators saturate, so the stabilizing element must explicitly curb or redesign its action first. | `RP + ACP` | Strong control-theoretic RP analog. The dominant control channel must restrain itself to preserve the whole. Visibility is present operationally through the signal path rather than politically or socially. |
| [Analysis of the increase and decrease algorithms for congestion avoidance in computer networks](https://www.sciencedirect.com/science/article/pii/0169755289900196) | Computer science / networking | Heavy senders must back off on explicit congestion signals to keep the network in the efficient region between underuse and overload. | `RP + ACP` | One of the cleanest distributed-systems matches. The most load-imposing agent changes first, and the change must be signaled and decodable by peers. Less about long-run lock-in than immediate stabilization. |
| [Suppressing cascades of load in interdependent networks](https://pmc.ncbi.nlm.nih.gov/articles/PMC3311366/) | Network theory / complex systems | Some interdependence suppresses local cascades, but too much coupling increases total load and opens new cascade routes; asymmetric capacity can drive an arms race. | `ACP + CDT` | Best ACP/CDT analog in the scan. It explicitly gives a productive interval, shows the stabilizer becoming destabilizing, and even produces self-reinforcing escalation. Not a full RP theorem, but very close to the project's overall shape. |

---

## Tier B: Strong Partial Analogs

| Result / mechanism | Field | Structural pattern | Best fit | Assessment |
|---|---|---|---|---|
| [Exploration and Exploitation in Organizational Learning](https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71) | Organization theory | Adaptive success improves exploitation faster than exploration, making organizations effective in the short run but self-destructive in the long run. | `CDT` | Nearly a direct organizational expression of crystallization drift. Very strong on lock-in, weak on strongest-goes-first and weak on explicit margin localization. |
| [Highly Optimized Tolerance](https://pubmed.ncbi.nlm.nih.gov/11018927/) | Complex systems / engineering | Design for expected disturbances produces efficient and robust but highly specialized systems that become fragile to model error and off-design shocks. | `CDT` | One of the best generic rigidity-from-optimization neighbors. It captures attractor narrowing and robust-yet-fragile structure cleanly, but not the visible-restraint part of RP. |
| [Increasing Returns and Path Dependence in the Economy](https://www.jstor.org/stable/10.3998/mpub.10029) | Economics | Positive feedback and increasing returns create lock-in and make reversal increasingly costly. | `CDT` | Strong on reinforcement-driven narrowing of accessible futures. It is a major CDT neighbor, though not a floor/visibility theorem. |
| [Resilience and Stability of Ecological Systems](https://www.annualreviews.org/doi/10.1146/annurev.es.04.110173.000245) | Ecology / resilience | System persistence depends on remaining within a basin of attraction; resilience loss near thresholds yields abrupt regime shift. | `ACP + VM` | Strong ecological ACP analog. The interval is framed as resilience inside a basin, and failure occurs at threshold breach. It does not by itself give the strongest-goes-first claim. |
| [The Electronic Mail Game](https://econpapers.repec.org/RePEc:aea:aecrev:v:79:y:1989:i:3:p:385-91) | Game theory | Very high but finite mutual knowledge is not enough for coordination; almost-common knowledge is structurally different from common knowledge. | `ACP` | Strong support for the "visible / decodable" requirement. It does not say the powerful side must move first, but it does say coordinated preservation requires publicly legible signaling. |
| [Agreeing to Disagree](https://www.ma.huji.ac.il/raumann/pdf/Agreeing%20to%20Disagree.htm) | Epistemic game theory | Once posteriors are common knowledge, divergence collapses. | `ACP` | Another visibility / decodability neighbor. Good for the communication-floor side of the project, not for RP or VM directly. |
| [Stabilization with data-rate-limited feedback](https://www.sciencedirect.com/science/article/pii/S0167691100000372) | Control + information theory | Stabilization requires a minimum feedback rate tied to plant instability. | `ACP` | Strong hard-floor theorem: below a coordination rate, stabilization is impossible. It supports the "floor cannot be breached" side of the project but has little strongest-first content. |
| [Coordination Failures and the Lender of Last Resort](https://academic.oup.com/jeea/article/2/6/1116/2280850) | Finance | A central authority may need to intervene first when solvent but illiquid institutions cannot coordinate liquidity privately. | `RP + VM` | Strong partial RP analog in finance. The powerful stabilizer moves first to preserve the system, while stress often surfaces at the vulnerable banking margin. Less clean on CDT. |
| [Stability Properties of Constrained Queueing Systems and Scheduling Policies for Maximum Throughput in Multihop Radio Networks](https://drum.lib.umd.edu/handle/1903/5346) | Distributed systems | There is a maximal stability region, and outside it no scheduling policy can keep queues stable. | `ACP` | A good formal floor result. It helps with coordination-region thinking, but not with visible restraint by the strongest node specifically. |
| [Inhibition stabilization is a widespread property of cortical networks](https://elifesciences.org/articles/54875) | Neuroscience | Strong recurrent excitation is unstable unless inhibitory circuitry tracks and restrains it. | `RP` partial | Interesting neural analog: the most amplifying subsystem survives only because another system applies restraint. This is close to the project's structure but still not a literal self-restraint theorem. |

---

## Tier C: Vulnerable-Margin and Cascade Neighbors

| Result / mechanism | Field | Structural pattern | Best fit | Assessment |
|---|---|---|---|---|
| [Cascade-based attacks on complex networks](https://pubmed.ncbi.nlm.nih.gov/12513335/) | Network theory | Disabling a single high-load node redistributes load and can cause system-wide cascade. | `VM + RP` partial | Strong on central concentration and cascade, but it is a damage theorem, not a self-restraint theorem. Useful mainly for the load-concentration side of RP and for margin-sensitive failure propagation. |
| [Catastrophic cascade of failures in interdependent networks](https://www.nature.com/articles/nature08932) | Interdependent networks | Small failures in one layer can recursively collapse the whole coupled system. | `VM + CDT` | Strong vulnerable-margin analog. Also shows that a form of successful interdependence can create hidden fragility. Still not a strongest-must-change theorem. |
| [Universal mechanism for hybrid percolation transitions](https://www.nature.com/articles/s41598-017-06182-3) | Statistical physics / network cascades | Long periods of critical branching give way to abrupt supercritical collapse. | `VM + ACP` | Useful for formalizing threshold structure and sudden edge failure. Good on collapse geometry, weak on restraint and visibility. |

---

## Tier D: Adjacent but Not Especially Tight

| Result / mechanism | Field | Structural pattern | Best fit | Assessment |
|---|---|---|---|---|
| [A Note on Trophic Complexity and Community Stability](https://doi.org/10.1086/282586) | Ecology | A keystone predator prevents a dominant competitor from monopolizing shared space. | `RP` inverse | Close in spirit, but the restraint is imposed on the dominant actor rather than voluntarily performed by it. Better read as an inverse or dual analog. |
| [A single quantum cannot be cloned](https://www.nature.com/articles/299802a0) | Quantum information | Unknown quantum states cannot be perfectly replicated because of linearity. | floor only | A real coordination / measurement constraint, but not a good RP or CDT analog. It functions more as a useful negative control than as a close neighbor. |

---

## Strongest Matches by Project Claim

### 1. Best neighbors of ACP

1. [Suppressing cascades of load in interdependent networks](https://pmc.ncbi.nlm.nih.gov/articles/PMC3311366/)
2. [Stabilization with data-rate-limited feedback](https://www.sciencedirect.com/science/article/pii/S0167691100000372)
3. [The Electronic Mail Game](https://econpapers.repec.org/RePEc:aea:aecrev:v:79:y:1989:i:3:p:385-91)
4. [Resilience and Stability of Ecological Systems](https://www.annualreviews.org/doi/10.1146/annurev.es.04.110173.000245)
5. [AIMD congestion avoidance](https://www.sciencedirect.com/science/article/pii/0169755289900196)

These are the cleanest "there is a workable region, and crossing the boundary breaks coordination" results.

### 2. Best neighbors of CDT

1. [Suppressing cascades of load in interdependent networks](https://pmc.ncbi.nlm.nih.gov/articles/PMC3311366/)
2. [Highly Optimized Tolerance](https://pubmed.ncbi.nlm.nih.gov/11018927/)
3. [Exploration and Exploitation in Organizational Learning](https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71)
4. [Increasing Returns and Path Dependence in the Economy](https://www.jstor.org/stable/10.3998/mpub.10029)
5. [Catastrophic cascade of failures in interdependent networks](https://www.nature.com/articles/nature08932)

These are the strongest existing formulations of the core CDT intuition: success narrows possibility space.

### 3. Best neighbors of Restraint-Power

1. [The Political Foundations of Democracy and the Rule of the Law](https://www.cambridge.org/core/journals/american-political-science-review/article/political-foundations-of-democracy-and-the-rule-of-the-law/564FB92EE1808897FD0041E25289CF1F)
2. [After Victory](https://collaborate.princeton.edu/en/publications/after-victory-institutions-strategic-restraint-and-the-rebuilding/)
3. [Anti-windup / actuator saturation](https://www.sciencedirect.com/science/article/abs/pii/S0167691104000167)
4. [AIMD congestion avoidance](https://www.sciencedirect.com/science/article/pii/0169755289900196)
5. [Coordination Failures and the Lender of Last Resort](https://academic.oup.com/jeea/article/2/6/1116/2280850)

This is the strongest cluster in the memo. The clearest domain-native statement of RP appears in political commitment and protocol-control settings, not in statistical-physics settings.

### 4. Best neighbors of Vulnerable-Margin

1. [Cascade-based attacks on complex networks](https://pubmed.ncbi.nlm.nih.gov/12513335/)
2. [Catastrophic cascade of failures in interdependent networks](https://www.nature.com/articles/nature08932)
3. [Universal mechanism for hybrid percolation transitions](https://www.nature.com/articles/s41598-017-06182-3)
4. [Resilience and Stability of Ecological Systems](https://www.annualreviews.org/doi/10.1146/annurev.es.04.110173.000245)

These results are the best support for the claim that failure often first appears at the weak interface rather than at the visibly dominant center.

---

## Main Synthesis

### 1. Where the "strongest goes first" structure is really strongest

The most convincing matches are not in generic cascade mathematics. They are in literatures where the center can choose a policy:

- sovereign restraint,
- hegemonic self-binding,
- controller anti-windup,
- congestion control,
- central-bank backstop behavior.

This matters because RP is not only a load theorem. It is a **choice-under-asymmetry** theorem. The dominant subsystem is the only one with enough slack or leverage to change the regime before the floor is breached.

### 2. Where the visibility requirement is strongest

The visibility / decodability clause is best supported by:

- common knowledge and almost-common-knowledge results,
- public commitment theory,
- protocol-level explicit congestion signaling,
- institutional self-binding visible to weaker actors.

In other words, the "strongest must change first" half and the "that change must be legible" half often live in different literatures and need to be combined to recover the full project structure.

### 3. Where the vulnerable-margin claim is strongest

The VM claim is extremely common in network, ecology, and cascading-failure work, but usually in a descriptive rather than prescriptive register. Those results show:

- where collapse first becomes visible,
- where slack is smallest,
- where local failure first propagates globally.

They do **not** usually say that the center must restrain itself in response. That prescriptive bridge is what the project adds.

### 4. What appears genuinely distinctive in the project's formulation

The rare combination is not any single piece taken alone. The distinctive claim is the composition:

1. the system has a hard coordination floor;
2. successful stabilization narrows future options;
3. under pressure, the highest-capacity subsystem must initiate change first;
4. that change only works if other subsystems can decode it;
5. if restraint fails, breakdown often surfaces first at the margin rather than the center.

This exact five-part package was not found as a domain-native theorem in the current scan.

---

## Working Conclusion

The best current reading is:

- **ACP/CDT** already have many neighbors under names like resilience thresholds, path dependence, robust-yet-fragile design, and exploitation traps.
- **Restraint-Power** has fewer close matches, but the strongest are real and important: self-enforcing political limits, hegemonic strategic restraint, anti-windup, and congestion-control backoff.
- **Vulnerable-Margin** is widespread and strongly supported, but usually appears as an empirical failure geometry rather than as part of a full theory of preservation.

So the project is not inventing every component from nothing. What seems comparatively uncommon is the claim that these components are **one recurring structural law** rather than a loose family of analogies.

