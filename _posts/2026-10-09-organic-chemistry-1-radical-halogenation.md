---
title: "Organic Chemistry 1: Reactions of Alkanes — Radical Halogenation"
date: 2026-10-09 13:50:00 +0900
categories: [Course Notes, Organic Chemistry 1]
tags: [radicals, bond dissociation energy, hyperconjugation, hammond postulate, selectivity, halogenation]
description: Homolytic cleavage and bond dissociation energies, alkyl radical structure and hyperconjugation, the chain mechanism of methane chlorination, the Hammond postulate, and why bromination is selective where chlorination is not. Unit 5 of Organic Chemistry 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers the lecture of 16 March 2023, "Reaction of Alkanes",
> corresponding to Vollhardt chapter 3. It is the first complete reaction
> mechanism of the course.
{: .prompt-info }

## What this unit answers

Alkanes have no functional group, so there is nothing for a nucleophile to
attack and nothing for an electrophile to find. To do any chemistry at all you
have to break a C–H bond, and a C–H bond is both strong (about
100 kcal mol⁻¹) and barely polar.

The answer is to break it **homolytically**, giving radicals, and to let a
chain reaction do the work. This is the first mechanism in the course, and it
is chosen because it is the cleanest teaching example there is: three stages,
four elementary steps, and every step's enthalpy computable from a table.

But the real payload is **selectivity**. An alkane has many C–H bonds, which
are not all equivalent, and a reagent that attacks them indiscriminately is
useless. Understanding why bromine is selective and chlorine is not requires
putting together everything from
[unit 2](/posts/organic-chemistry-1-structure-reactivity/) — thermodynamics,
kinetics, transition states — with one new idea, the **Hammond postulate**. That
idea is the most transferable thing in the unit; it will be used in every
chapter that follows.

## Prerequisites

[Unit 2](/posts/organic-chemistry-1-structure-reactivity/) for ΔH° from bond
strengths, potential energy diagrams and the rate-determining step.
[Unit 1](/posts/organic-chemistry-1-structure-bonding/) for hybridization and
the empty p orbital.
[Unit 4](/posts/organic-chemistry-1-alkanes/) for the primary/secondary/tertiary
classification.

---

## Part 1 — breaking bonds

### Two ways

Every reaction requires bond breaking and bond making, and a bond can break two
ways.

**Homolytic cleavage.** The bonding pair splits, one electron to each fragment.
Drawn with **two single-barbed fishhook arrows**. The products are two uncharged
species, each with an unpaired electron — **radicals**.

$$
\mathrm{A{:}B} \;\longrightarrow\; \mathrm{A^{\bullet}} + \mathrm{{}^{\bullet}B}
$$

A radical is highly unstable because the atom bearing the odd electron has
only seven electrons, not an octet.

**Heterolytic cleavage.** Both electrons go to one fragment. Drawn with **one
double-barbed arrow**. The products are ions — this is the acid–base and polar
chemistry of unit 2.

$$
\mathrm{A{:}B} \;\longrightarrow\; \mathrm{A^{+}} + \mathrm{{:}B^{-}}
$$

Heterolysis of a C–Z bond gives either a **carbocation** — an unstable
intermediate with a carbon surrounded by only six electrons — or a
**carbanion**, with a negative charge on carbon, an element not electronegative
enough to want it.

Which path a bond takes depends on polarity and on conditions. A nonpolar bond
in a nonpolar solvent, heated or irradiated, goes homolytically. A polar bond in
a polar solvent goes heterolytically.

### Bond dissociation energy

**DH°** is the energy needed to cleave a bond **homolytically**. Three
properties follow from the definition, and all three matter:

- It is **always positive**. Breaking a bond always costs energy, so homolysis
  is always endothermic.
- Bond *formation* always releases energy, so it is always exothermic.
- It is always the **homolytic** number. A table of DH° values says nothing
  directly about heterolytic cleavage.

From [unit 2](/posts/organic-chemistry-1-structure-reactivity/), with
ΔG° = ΔH° − TΔS° and ΔS° negligible when the molecule count is unchanged:

$$
\Delta H^{\circ} = \sum (\text{bonds broken}) - \sum (\text{bonds made})
$$

> **Worked example.** Is CH₃–OH + H–I → CH₃–I + H–OH feasible?
>
> Bonds broken: CH₃–OH at 93 and H–I at 71, total 164 kcal mol⁻¹.
> Bonds made: CH₃–I at 57 and H–OH at 119, total 176 kcal mol⁻¹.
>
> ΔH° = 164 − 176 = **−12 kcal mol⁻¹**. Exothermic, so thermodynamically
> feasible. Note what this does and does not tell you: it says the equilibrium
> favours products, and says nothing whatever about whether it happens at a
> useful rate.
{: .prompt-tip }

### Not all C–H bonds are the same

To functionalize an alkane you have to break C–H. Are they all equivalent?
No — and the differences are what makes selectivity possible:

$$
\mathrm{CH_4} \;>\; \mathrm{R_{prim}{-}H} \;>\; \mathrm{R_{sec}{-}H} \;>\; \mathrm{R_{tert}{-}H}
$$

DH° decreases along the series. Methane's C–H is 105 kcal mol⁻¹, a primary C–H
about 101, a secondary about 98.5, a tertiary about 96.5.

Why? Because DH° measures the energy difference between the alkane and the
**radical it produces**, and the alkanes differ far less than the radicals do.
A weaker bond means a more stable radical. The question "why do these bond
strengths differ?" is really "why are substituted radicals more stable?", and
the next part answers it.

---

## Part 2 — alkyl radicals

### Structure

A carbon radical is **sp² hybridized and trigonal planar**, exactly like a
carbocation. The unhybridized p orbital holds the single unpaired electron and
extends above and below the plane.

This is the geometry of BH₃ from
[unit 1](/posts/organic-chemistry-1-structure-bonding/), with one electron in
the p orbital instead of none. The orbital holding the odd electron is called
the **SOMO** — singly occupied molecular orbital — and it is simultaneously the
highest occupied and the lowest unoccupied orbital, which is why radicals react
with both nucleophiles and electrophiles.

### Hyperconjugation

**Hyperconjugation** is the delocalization of electrons with the participation
of bonds of primarily σ character.

Applied to a radical: the p orbital carrying the unpaired electron overlaps
with the **bonding** molecular orbital of a neighbouring C–H bond. Electron
density from the filled σ(C–H) spills into the half-empty p orbital, which
spreads the unpaired electron over more than one atom — and by rule 2 of
[unit 1](/posts/organic-chemistry-1-structure-bonding/), delocalization lowers
energy.

In molecular-orbital terms, the filled σ(C–H) and the singly occupied p
combine; the resulting lower orbital takes two electrons and the upper one
takes one, so the net effect is stabilizing. The lecture slide puts it
directly: the σ(C–H) bond is stabilized.

**More neighbouring C–H bonds means more hyperconjugation.** An ethyl radical
has three C–H bonds on the adjacent carbon available to donate; an isopropyl
radical has six; a *tert*-butyl radical has nine. Hence:

$$
3^{\circ} > 2^{\circ} > 1^{\circ} > \text{methyl}
$$

for radical stability, which is exactly the inverse of the DH° ordering, as it
must be.

The prediction that follows — **the more substituted C–H should be more
reactive** — is the hypothesis the rest of the unit tests.

---

## Part 3 — the mechanism

### The overall reaction

$$
\mathrm{CH_4} + \mathrm{Cl_2} \;\xrightarrow{\;\Delta \text{ or } h\nu\;}\; \mathrm{CH_3Cl} + \mathrm{HCl}
$$

Check the thermodynamics with DH° values: broken, C–H at 105 and Cl–Cl at 58,
total 163; made, C–Cl at 85 and H–Cl at 103, total 188. So

$$
\Delta H^{\circ} = 163 - 188 = -25\ \text{kcal mol}^{-1}
$$

Exothermic — but it **needs heat (Δ) or light (hν) to start**. That gap between
"thermodynamically downhill" and "does not happen on its own" is exactly the
thermodynamics-versus-kinetics distinction of unit 2, and the mechanism explains
where the barrier is.

### Stage 1 — initiation: lighting the match

$$
\begin{aligned}
\mathrm{Cl_2} &\;\longrightarrow\; \mathrm{2\,Cl^{\bullet}} \\
\Delta H^{\circ} &= DH^{\circ}(\mathrm{Cl_2}) = +58\ \text{kcal mol}^{-1}
\end{aligned}
$$

Note which bond breaks. Not the C–H at 105, but the Cl–Cl at 58 — the weakest
bond in the mixture. Initiation always attacks the weakest bond available.

Two ways to supply the 58:

- **Thermally.** Vibrational energy in the Cl–Cl bond grows until it exceeds
  the bond strength and the bond flies apart.
- **Photochemically.** A photon promotes a bonding electron into the
  antibonding σ\* orbital. With one electron in σ and one in σ\*, the bond
  order is zero and the molecule dissociates. This is the
  [unit 1](/posts/organic-chemistry-1-structure-bonding/) MO diagram doing real
  work: the same reason He₂ does not exist is the reason light breaks Cl₂.

In practice, initiators are chosen as molecules with one deliberately weak
bond. **Benzoyl peroxide** has an O–O bond worth about 35 kcal mol⁻¹;
**AIBN** (azobisisobutyronitrile) fragments to two stabilized tertiary radicals
and a molecule of N₂, with the entropy of releasing a gas helping it along.
Both decompose at convenient temperatures, which is why they are standard
reagents in radical chemistry and in polymerization.

### Stage 2 — propagation: the fire

Two steps, which together consume starting material and regenerate the radical:

$$
\begin{aligned}
\mathrm{Cl^{\bullet}} + \mathrm{CH_4} &\to \mathrm{{}^{\bullet}CH_3} + \mathrm{HCl}
&& \Delta H^{\circ} = +2 \\
\mathrm{{}^{\bullet}CH_3} + \mathrm{Cl_2} &\to \mathrm{CH_3Cl} + \mathrm{Cl^{\bullet}}
&& \Delta H^{\circ} = -27
\end{aligned}
$$

The first comes from 105 − 103, the second from 58 − 85. Add them and the radicals cancel, leaving the overall reaction with
ΔH° = +2 − 27 = −25, as computed above. That cancellation is the defining
feature of a **chain mechanism**.

The practical consequence is the one the lecture emphasizes: **the initiation
step does not enter into the equation.** Only a few chlorine atoms are needed to
convert all of the starting material, because each one cycles through the
propagation loop thousands of times before it is destroyed. A catalytic amount
of initiator consumes a stoichiometric amount of substrate — which is also why
a single chlorine atom from a CFC molecule can destroy a great many ozone
molecules in the stratosphere, and why the airframe on the opening slide of the
lecture matters.

Each propagation step has its own barrier, so the energy profile for one cycle
has two humps. The first step, hydrogen abstraction, is the taller of the two
and is therefore **rate-determining**.

### Stage 3 — termination

Any step that consumes two radicals and makes none kills a chain:

$$
\begin{aligned}
\mathrm{Cl^{\bullet}} + \mathrm{Cl^{\bullet}} &\to \mathrm{Cl_2} \\
\mathrm{{}^{\bullet}CH_3} + \mathrm{{}^{\bullet}CH_3} &\to \mathrm{CH_3CH_3} \\
\mathrm{{}^{\bullet}CH_3} + \mathrm{Cl^{\bullet}} &\to \mathrm{CH_3Cl}
\end{aligned}
$$

These are all exothermic and have essentially no barrier, so why are they not
the dominant pathway? Because radical concentrations are tiny. A radical is far
more likely to meet a molecule of substrate than another radical, so
propagation outruns termination by orders of magnitude. The trace of ethane
found in methane chlorination is the fingerprint of the second termination step.

---

## Part 4 — which halogen

### The numbers

Running the same reaction with F₂, Cl₂, Br₂ and I₂ requires the relevant DH°
values. These are the ones to have in front of you:

| Bond | DH° (kcal mol⁻¹) |
|---|---|
| F–F | 38 |
| Cl–Cl | 58 |
| Br–Br | 46 |
| I–I | 36 |
| H–F | 136 |
| H–Cl | 103 |
| H–Br | 87 |
| H–I | 71 |
| CH₃–F | 110 |
| CH₃–Cl | 85 |
| CH₃–Br | 70 |
| CH₃–I | 57 |

All four X–X bonds are weak enough that **initiation is fine for all of them**.
The differences are entirely in propagation. Vollhardt's Table 3.5 gives each
step, in kcal mol⁻¹:

- **Propagation step 1**, X• + CH₄ → •CH₃ + HX —
  F −31, Cl +2, Br +18, I +34
- **Propagation step 2**, •CH₃ + X₂ → CH₃X + X• —
  F −72, Cl −27, Br −24, I −21
- **Overall**, CH₄ + X₂ → CH₃X + HX —
  F −103, Cl −25, Br −6, I +13

Read the first line. It is the rate-determining step, and it goes from strongly
exothermic for fluorine to strongly endothermic for iodine, tracking H–X bond
strength: 136, 103, 87, 71.

### What each one does

**Fluorine** releases 103 kcal mol⁻¹ overall. That much energy dumped into a
chain reaction is not a synthesis; it is an explosion. Fluorination is
uncontrollable without special technique.

**Chlorine and bromine** both work, and are the useful cases. Chlorine is
faster.

**Iodine will not go at all.** The overall reaction is endothermic by
13 kcal mol⁻¹, and the first propagation step by 34. There is no thermodynamic
driving force, because both the C–I bond (57) and the H–I bond (71) being
formed are too weak to repay what was broken. The lecture's handwritten margin
note says precisely this: the C–I and H–I bonds are weak, so the driving force
is absent.

So reactivity runs F₂ > Cl₂ ~ Br₂ > I₂, with fluorine exploding, iodine not
going, and the middle two useful.

> **A caution about the reasoning.** Rate is a kinetic quantity and DH° is a
> thermodynamic one, and unit 2 insisted these are independent. Here they track
> each other closely — which is a real phenomenon in this family of reactions,
> not a licence to equate them in general. The next part is the explanation of
> *why* they track, and the explanation is exactly what tells you when they
> would not.
{: .prompt-warning }

---

## Part 5 — the Hammond postulate

### The statement

> The transition state of a reaction resembles the structure of the species —
> reactant or product — to which it is **closer in energy**.

Transition states cannot be observed. They exist for a single vibration, cannot
be isolated, and no spectroscopy reaches them. The Hammond postulate is the
device that lets you reason about them anyway, by estimating a transition state
from its nearest observable neighbour.

Two cases:

- **Exothermic step.** The transition state is early, close in energy to the
  reactants, and therefore *looks like the reactants*. Bonds are barely broken
  and barely formed.
- **Endothermic step.** The transition state is late, close in energy to the
  products, and *looks like the products*. Bonds are nearly fully broken and
  formed.

![Two reaction coordinate diagrams side by side. On the left an exothermic step whose transition state sits early, close in both energy and position to the reactants. On the right an endothermic step whose transition state sits late, close to the products. Dashed lines mark the position of each transition state along the reaction coordinate](/assets/img/organic-chemistry-1/hammond-postulate.svg)

The consequence is the one that matters: **in an endothermic step, differences
in product stability show up in the transition state, and therefore in the
rate. In an exothermic step, they do not.** The postulate is what converts a
thermodynamic quantity — the stability of the product radical — into a kinetic
one.

### Applied to selectivity

Chlorination of propane can remove a primary hydrogen (six of them) or a
secondary one (two of them). Statistically that is 3:1 in favour of primary.
What is observed is roughly 1:1 — so, per hydrogen, the secondary is about
four times more reactive.

The reason is the rate-determining step. A chlorine atom meeting propane can
take either hydrogen, and the two outcomes differ:

- the **primary** hydrogen gives CH₃CH₂CH₂• and HCl, with
  ΔH° = −2 kcal mol⁻¹;
- the **secondary** hydrogen gives CH₃ĊHCH₃ and HCl, with
  ΔH° = −4.5 kcal mol⁻¹.

Removing the secondary hydrogen is more exothermic, because the secondary
radical is more stable. The transition states are radical-like enough to reflect
that, so the secondary barrier is Ea ≈ 0.5 kcal mol⁻¹ against
Ea ≈ 1 kcal mol⁻¹ for the primary — and the secondary route is faster.

Extending to tertiary C–H, using isobutane, gives the chlorination selectivity
at 25 °C:

$$
\text{tertiary} : \text{secondary} : \text{primary} \;\approx\; 5 : 4 : 1
$$

The prediction from part 2 is confirmed. But look at how *weak* the preference
is: a factor of five across the full range, when the radical stabilities differ
by nearly 9 kcal mol⁻¹. Chlorination is barely selective at all, and a
chlorination of any real substrate gives a mixture.

### Chlorination versus bromination

Two differences, and the second is the useful one:

1. **Chlorination is faster** than bromination.
2. **Chlorination is unselective**, giving mixtures; **bromination is
   selective**, often giving one major product.

The Hammond postulate explains both, and the key is the sign of the
rate-determining step.

**Bromination.** Abstraction of a 1° or 2° hydrogen by Br• is **endothermic**:
H–Br is only 87, against C–H at around 100. The transition state therefore
resembles the **products** — the radical. The energy difference between the
primary and secondary radicals appears almost in full in the transition states,
so the more stable radical is formed much faster, and a single product
dominates.

**Chlorination.** Abstraction by Cl• is **exothermic**: H–Cl is 103, enough to
repay the C–H. The transition state therefore resembles the **reactants** —
and the reactant is the *same* propane molecule in both cases. The radicals
being formed barely enter the picture, so both are formed, and the product is a
mixture.

The numbers make it vivid. Vollhardt's Table 3.6 gives relative reactivities per
C–H bond, normalized to primary:

- **CH₃–H** — F• 0.5, Cl• 0.004, Br• 0.002
- **primary, RCH₂–H** — 1, 1, 1 (this is the reference)
- **secondary, R₂CH–H** — F• 1.2, Cl• 4, Br• 80
- **tertiary, R₃C–H** — F• 1.4, Cl• 5, Br• 1700

The fluorine and chlorine figures are for 25 °C and the bromine ones for
150 °C, all in the gas phase. Fluorine is essentially
indiscriminate — 0.5 to 1.4 across the whole range — because its abstraction
step is exothermic by 31 kcal mol⁻¹ and its transition state is as early as a
transition state gets. Bromine, with the most endothermic abstraction, spreads
0.002 to 1700, a factor of nearly a million.

**The general rule:** *the more reactive the reagent, the less selective it is.*
A very reactive species has an early transition state and cannot tell its
options apart; a sluggish one has a late transition state and discriminates
sharply. This is the **reactivity–selectivity principle**, and it recurs
throughout organic chemistry.

One practical caveat the lecture closes on: selectivities vary considerably with
the reagent — ICl, ROCl, R₂NBr all behave differently — and with temperature and
solvent. The numbers above are for the gas phase at the stated temperature, and
they are a guide to the pattern rather than values to quote.

---

## Connections

- **Backward.** ΔH° from bond strengths, potential energy diagrams and the
  rate-determining step come straight from
  [unit 2](/posts/organic-chemistry-1-structure-reactivity/). The planar sp²
  carbon with a half-filled p orbital is the BH₃ geometry of
  [unit 1](/posts/organic-chemistry-1-structure-bonding/), and the photochemical
  initiation step is its MO diagram. Hyperconjugation is the same effect that
  explains ethane's rotational barrier in
  [unit 4](/posts/organic-chemistry-1-alkanes/) — here it stabilizes a radical
  instead of a conformation.
- **Forward.** The Hammond postulate will be used to explain carbocation
  rearrangements and Markovnikov selectivity in chapter 12, and to compare SN1
  and SN2 in chapter 6. The stability order tertiary > secondary > primary >
  methyl carries over unchanged to carbocations, for the same hyperconjugative
  reason. Radical halogenation itself returns in chapter 14 as allylic and
  benzylic bromination with NBS, where resonance stabilization of the radical
  makes selectivity nearly complete.
- **Outward.** Radical chain chemistry is how polymers are made industrially,
  how fats go rancid, how antioxidants work, and — in the stratospheric chlorine
  cycle the lecture opens with — how CFCs destroy ozone.

## Summary

- **Homolytic cleavage** gives radicals, drawn with fishhook arrows; **heterolytic** gives ions
- **DH° is always positive and always homolytic**; bond breaking is endothermic, bond making exothermic
- **ΔH° = bonds broken − bonds made**; CH₃OH + HI gives 164 − 176 = −12
- **C–H strength falls** CH₄ 105 > 1° 101 > 2° 98.5 > 3° 96.5
- **A weaker bond means a more stable radical** — DH° measures the radical, not the alkane
- **Alkyl radicals are sp², planar**, with the odd electron in a p orbital, the SOMO
- **Hyperconjugation** — filled σ(C–H) donating into the half-empty p orbital
- **Radical stability** 3° > 2° > 1° > methyl, tracking the number of neighbouring C–H bonds
- **Methane + Cl₂** — ΔH° = 163 − 188 = −25, exothermic but needs Δ or hν
- **Initiation breaks the weakest bond** — Cl–Cl at 58, not C–H at 105
- **Photochemical initiation** promotes σ to σ\*, bond order zero, dissociation
- **Propagation** +2 then −27; radicals cancel, so initiation is catalytic
- **Termination** consumes two radicals; rare, because radical concentrations are tiny
- **F explodes (−103), Cl and Br work, I will not go (+13)** — H–I and C–I are too weak
- **Hammond** — exothermic steps have early, reactant-like transition states; endothermic ones late, product-like
- **Chlorination is exothermic** at the rate-determining step, so unselective: 3°:2°:1° ≈ 5:4:1
- **Bromination is endothermic** there, so selective: 1700 : 80 : 1
- **The more reactive the reagent, the less selective** — the reactivity–selectivity principle

## References

- Peter C. Vollhardt & Neil E. Schore, *Organic Chemistry: Structure and Function*, 8th edition — chapter 3. The propagation enthalpies are Table 3.5 and the relative reactivities Table 3.6; the bond dissociation energies are the chapter 3 tables.
- Janice G. Smith, *Organic Chemistry* — the homolytic/heterolytic opening, the Hammond postulate statement and the chlorination-versus-bromination comparison follow her presentation, which is what several of the slides use.
- Organic Chemistry 1 (3343.205), Seoul National University, Spring 2023. Instructor: Seung Youn Hong (홍승윤). Lecture of 16 March 2023, "Week 03-2: Reaction of Alkanes", 35 slides.
- The Hammond postulate figure is drawn for these notes; the slide versions are publisher artwork. All DH° values and both tables are as given in the lecture.
- The explanation that iodination fails for want of a thermodynamic driving force in the C–I and H–I bonds is a handwritten annotation on the lecture slide.
- The propane selectivity arithmetic — six primary hydrogens against two secondary, a 3:1 statistical expectation against a roughly 1:1 observation — is worked out here; the slide gives the energy diagram and the per-hydrogen conclusion without the counting. The 1° and 2° activation energies of 1 and 0.5 kcal mol⁻¹ and the ΔH° values of −2 and −4.5 are from that diagram.
- The initiator bond strengths, the reactivity–selectivity principle as a named idea, and the remark that the trace of ethane in methane chlorination identifies the termination step are mine. The ozone connection is the lecturer's opening slide.
