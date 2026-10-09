---
title: "Organic Chemistry 1: Structure and Reactivity"
date: 2026-10-09 13:20:00 +0900
categories: [Course Notes, Organic Chemistry 1]
tags: [thermodynamics, kinetics, acids and bases, pka, resonance, lewis acids, electrophile]
description: Equilibria and free energy, enthalpy from bond strengths, activation barriers and rate laws, then Brønsted-Lowry acids and bases, pKa, the four factors governing acid strength, and the Lewis picture. Unit 2 of Organic Chemistry 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers the lecture of 9 March 2023, "Structure and Reactivity",
> corresponding to Vollhardt chapter 2. The acid–base half of it — the four
> factors, the conjugate-base method, the treatment of nitrogen bases — follows
> Janice Smith's organization rather than Vollhardt's, and the slides are drawn
> from her text.
{: .prompt-info }

## What this unit answers

Two questions, and the whole point is that they are **separate**.

**Will the reaction go?** That is thermodynamics. It depends only on the energy
difference between where you start and where you finish, and it is completely
indifferent to how you get there.

**How fast?** That is kinetics. It depends only on the highest point along the
path, and it is completely indifferent to where the path ends.

Confusing the two is the most common error in first-year organic chemistry, and
it produces errors in both directions: predicting that a favourable reaction
will happen when it has a prohibitive barrier, and predicting that a fast
reaction goes to completion when its equilibrium lies to the left.

The second half of the unit applies all of this to the simplest reaction there
is — moving a proton. Acid–base chemistry is worth the time it gets because
**pKa is the only quantitative reactivity scale you will have all semester.**
Almost every "will this base deprotonate that?" question in the rest of the
course is answered by comparing two numbers from one table.

## Prerequisites

[Unit 1](/posts/organic-chemistry-1-structure-bonding/) for Lewis structures,
formal charge, resonance, electronegativity and hybridization. Resonance in
particular — the acid–base half of this unit is largely resonance applied to
anions.

---

## Part 1 — thermodynamics

### Everything is an equilibrium

Write any reaction A ⇌ B. At equilibrium the composition is fixed by

$$
K = \frac{[\mathrm{B}]}{[\mathrm{A}]}
$$

and the vocabulary follows: a large K means the reaction is "complete", "to the
right", "downhill"; a small K means the opposite. The combustion of octane,
which is what a car engine does, is the extreme case —

$$
\mathrm{2\,C_8H_{18} + 25\,O_2 \longrightarrow 16\,CO_2 + 18\,H_2O}
$$

— with an equilibrium constant so large that calling it an equilibrium is a
technicality. It is still one.

### Quantifying it: Gibbs free energy

$$
\Delta G^{\circ} = -RT \ln K = -2.3\,RT \log K
$$

with *T* in kelvin (0 K = −273 °C) and *R* ≈ 2 cal deg⁻¹ mol⁻¹. The ° means
standard states: 1 atm, 25 °C (298 K), 1 M.

At 298 K the numbers collapse to something you should simply know:

$$
\Delta G^{\circ} = -1.36 \log K \quad (\text{kcal mol}^{-1})
$$

so every factor of ten in K costs 1.36 kcal mol⁻¹:

| K | ΔG° (kcal mol⁻¹) |
|---|---|
| 1 (a 50/50 mixture) | 0 |
| 10 | −1.36 |
| 100 | −2.72 |
| 0.1 | +1.36 |

This is a much smaller energy than chemical intuition suggests. A reaction that
is 99:1 at equilibrium is downhill by only 2.7 kcal mol⁻¹ — less than the
rotational barrier in ethane. Conversely, running the relation backwards:
ΔG° = −23.4 kcal mol⁻¹ corresponds to log K ≈ 23.4/1.36 ≈ 17, so K ≈ 10¹⁷.
Modest-looking energies produce absurd equilibrium constants.

### Splitting ΔG° into ΔH° and ΔS°

$$
\Delta G^{\circ} = \Delta H^{\circ} - T\,\Delta S^{\circ}
$$

**Enthalpy, ΔH°**, is the heat of reaction, and in organic chemistry it comes
almost entirely from changes in bond strength:

$$
\Delta H^{\circ} = \sum (\text{bonds broken}) - \sum (\text{bonds made})
$$

Note the direction. Breaking bonds costs energy and making them releases it, so
the *broken* term comes first and is positive. Negative ΔH° is **exothermic**;
positive is **endothermic**. A worked case from the slides: a reaction breaking
159 kcal mol⁻¹ worth of bonds and making 187 has
ΔH° = 159 − 187 = −28 kcal mol⁻¹, comfortably exothermic.

**Entropy, ΔS°**, measures the change in disorder — in the "freedom" of the
system, or equivalently in how widely its energy is dispersed. Nature strives
for disorder, so:

- more disorder ⇒ positive ΔS° ⇒ a *negative* contribution to ΔG°, because of
  the minus sign;
- more order ⇒ negative ΔS° ⇒ a *positive* contribution to ΔG°.

Entropy is reported in entropy units, e.u., which are cal mol⁻¹ K⁻¹. The factor
T matters: at 298 K, an entropy change of −31.3 e.u. contributes
−TΔS° = +9.3 kcal mol⁻¹, which is enough to overturn a respectable enthalpy.
The lecture's example had ΔH° = −15.5 kcal mol⁻¹ against
ΔS° = −31.3 e.u., leaving ΔG° ≈ −6 kcal mol⁻¹ — still favourable, but barely
half of what the enthalpy alone would suggest.

> **The working shortcut.** If the number of molecules is unchanged across the
> reaction, ΔS° is small and ΔH° controls the sign of ΔG°. Since you can
> estimate ΔH° from a table of bond strengths and cannot easily estimate ΔS° at
> all, this is what makes back-of-envelope thermodynamics possible. The
> shortcut fails exactly when it should: reactions that change the number of
> particles, and anything involving a gas or a ring opening.
{: .prompt-tip }

---

## Part 2 — kinetics

### Why anything survives

Every process has an **activation barrier**, Ea. This is not a technical detail;
it is the reason the world is not on fire. You, your desk and this page are all
thermodynamically unstable with respect to carbon dioxide and water in the
presence of atmospheric oxygen. What stops the conversion is that the first
step costs more energy than room temperature supplies.

Four things control a rate:

1. **Barrier height.** The energy of the transition state. Bonds have to be
   loosened before new ones form, and that costs.
2. **Temperature.** Higher T means faster-moving molecules, more collisions, and
   — far more importantly — a larger fraction of molecules with enough energy to
   clear the barrier.
3. **Concentration.** More collisions per unit time.
4. **The probability factor.** How likely a collision is to actually produce
   reaction, which depends on orientation (sterics) and on whether the right
   orbitals meet (electronics).

### The Boltzmann distribution, and why temperature matters so much

At any temperature, molecular energies are distributed, not uniform. The
Boltzmann distribution gives the fraction of molecules with energy at least Ea
as roughly $$e^{-E_a/RT}$$, and this exponential is the whole story.

Put numbers on it. The average kinetic energy of a molecule at room temperature
is about **0.6 kcal mol⁻¹**. A typical activation barrier is about
**20 kcal mol⁻¹**. The average molecule is more than thirty times short of what
it needs — and reactions still happen, because the distribution has a tail. The
number of molecules in that tail is what changes when you heat the flask, and
because the dependence is exponential, a small temperature rise produces a large
rate increase. The standard rule of thumb, that a 10 °C rise roughly doubles the
rate, is this exponential in disguise.

### Rate laws

Measuring a rate tells you something about the **transition state**, because the
rate law counts the molecules present in it.

- **Unimolecular**: rate = *k*[A]. Only A is in the transition state.
- **Bimolecular**: rate = *k*[A][B]. Both are.

This is the standard tool for distinguishing mechanisms, and in chapter 6 it is
what separates SN1 from SN2.

The barrier itself comes from the temperature dependence, via the **Arrhenius
equation**:

$$
k = A\,e^{-E_a/RT}
$$

Plot ln *k* against 1/T and the slope is −Ea/R. Two consequences worth stating
plainly: large Ea means a slow reaction, and increasing the temperature speeds
it up.

### Potential energy diagrams

The standard picture: energy on the vertical axis, "reaction coordinate" — a
deliberately vague composite of all the bond lengths and angles that change —
on the horizontal. Reactants on the left, products on the right, and the
transition state at the maximum.

![Two reaction coordinate diagrams side by side: on the left an exothermic reaction with a high barrier, on the right an endothermic reaction with a low barrier, showing that the activation energy and the overall energy change are independent](/assets/img/organic-chemistry-1/reaction-coordinate.svg)

Read off: the **barrier height** Ea, left to right, is the kinetics; the
**net change** ΔG°, left to right, is the thermodynamics. The figure makes the
central point of this unit visible — the left reaction is favourable and slow,
the right one unfavourable and fast. Nothing links the two quantities.

The transition state is not an intermediate. It is a maximum, not a minimum: it
has no lifetime, cannot be isolated, and cannot be put in a bottle. It is marked
‡. An **intermediate**, by contrast, sits in a local minimum, and a diagram with
an intermediate has two humps.

### The rate-determining step

Most reactions have several steps, and therefore several transition states. The
rate is set by the **highest** one — the bottleneck. Everything downstream of it
is invisible to kinetics.

> **A problem from the lecture.** On heating, a compound A becomes C. Three
> proposals: (a) A converts to C directly; (b) A goes first to B, then to C;
> (c) nothing happens. Given an energy diagram in which B sits between A and C
> with a modest barrier from A and a larger one from B to C, which is right?
>
> The answer is (b), and the reasoning is that (a) is not a competing *outcome*
> but a competing *path*: A → C directly has a much higher barrier than
> A → B, so the molecule takes the cheap step first. The highest point on the
> A → B → C route is the B → C transition state, and that is what determines
> the rate at which C appears. Choice (c) is wrong because heating supplies
> enough energy for the first barrier; the compound does not stay put.
{: .prompt-tip }

---

## Part 3 — Brønsted–Lowry acids and bases

### Definitions and arrows

**Acid = proton donor. Base = proton acceptor.** A proton here is literally
H⁺ — a bare nucleus, with no electrons at all, which is why it never travels
alone and why acid–base chemistry is really about what the *base* does.

Every Brønsted–Lowry reaction is the same two curved arrows:

- one from a lone pair on the base to the acidic hydrogen, forming the new bond;
- one from the H–A bond to A, giving those electrons to the leaving atom.

The products are the **conjugate acid** of the base and the **conjugate base**
of the acid. The arrows must balance: every bond formed is one arrow in, every
bond broken is one arrow out.

> **On arrow conventions.** A full, double-barbed arrow moves a pair of
> electrons. A single-barbed fishhook moves one, and belongs only in radical
> mechanisms ([unit 5](/posts/organic-chemistry-1-radical-halogenation/)).
> Arrows always start at electrons — never at a positive charge, never at an
> atom. An arrow drawn from H⁺ to a base is backwards, even though the reaction
> is right.
{: .prompt-warning }

### pKa

The acidity constant for HA ⇌ H⁺ + A⁻ in water is

$$
K_a = \frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}, \qquad
\mathrm{p}K_a = -\log K_a
$$

Water is omitted from the denominator because it is the solvent, present in
vast excess and effectively constant. **Low pKa means strong acid.** The scale
is logarithmic, so one unit is a factor of ten.

The anchor values worth memorizing, from Vollhardt's Table 2.2:

| Acid | pKa |
|---|---|
| HI | −10 |
| HBr | −9 |
| HCl | −8 |
| H₂SO₄ | −3 |
| H₃O⁺ | −1.7 |
| HF | 3.2 |
| CH₃COOH (acetic acid) | 4.7 |
| HCN | 9.2 |
| NH₄⁺ | 9.3 |
| CH₃SH | 10.0 |
| CH₃OH (methanol) | 15.5 |
| H₂O | 15.7 |
| HC≡CH (ethyne) | 25 |
| NH₃ | 35 |
| H₂C=CH₂ (ethene) | 44 |
| CH₄ (methane) | 50 |

The span is sixty orders of magnitude. Methane is the weakest acid in the table
by a wide margin, and that is just another way of saying what unit 1 said: a
C–H bond has nowhere to put a negative charge.

> **Why is the pKa of water 15.7 and not 14?** Because 14 is pK<sub>w</sub>, not
> pKa, and the two differ by the concentration of water itself.
>
> The autoionization constant is
> K<sub>w</sub> = [H₃O⁺][OH⁻] = 10⁻¹⁴. But for water *acting as an acid*,
> the equilibrium is H₂O + H₂O ⇌ H₃O⁺ + OH⁻, so
> K<sub>eq</sub> = [H₃O⁺][OH⁻]/[H₂O]², and the acidity constant is the one with
> a single water in the denominator:
> K<sub>a</sub> = [H₂O]·K<sub>eq</sub> = [H₃O⁺][OH⁻]/[H₂O].
>
> Pure water is 1000 g per litre at 18 g mol⁻¹, so [H₂O] = 55.5 M. Then
> K<sub>a</sub> = 10⁻¹⁴/55.5 = 1.8 × 10⁻¹⁶ and pKa = −log(1.8 × 10⁻¹⁶) = 15.7.
> The same correction is why H₃O⁺ is listed at −1.7 rather than 0.
{: .prompt-info }

### A warning about the table

Every pKa above is measured **in water**, and the solvent is not a spectator.
In dimethyl sulfoxide — a polar aprotic solvent that solvates cations well and
anions badly — the numbers shift, and they do not all shift by the same amount.
Anions that water stabilizes by hydrogen bonding are left exposed in DMSO, so
their acids look much weaker there.

The practical consequence is that a pKa comparison is only safe between two
compounds measured in the same solvent, and that reactions run in THF or DMSO
do not necessarily follow the aqueous ordering. Keep the table, but keep the
caveat with it.

---

## Part 4 — the four factors

### The method

To compare the acidity of any two acids:

1. **Draw the conjugate bases.**
2. **Decide which conjugate base is more stable.**
3. **The more stable the conjugate base, the stronger the acid.**

That is the whole technique, and it works because the acid and its conjugate
base differ by one proton: anything that lowers the energy of A⁻ pulls the
equilibrium towards it.

Four things stabilize an anion, and the rest of this part is each in turn.

### 1. Element effects

**Across a row**, acidity increases with the electronegativity of the atom
bearing the charge. CH₄ at pKa 50, NH₃ at 35, H₂O at 15.7, HF at 3.2 — a span
of nearly fifty units, driven entirely by which atom holds the lone pair.
Oxygen is far more electronegative than carbon, so it accepts a negative charge
far more willingly.

**Down a column**, electronegativity *stops* being the answer and **size**
takes over. HF (3.2) → HCl (−8) → HBr (−9) → HI (−10): acidity increases going
down, even though electronegativity decreases. The reason is the delocalization
rule from unit 1 — charge spread over a larger volume is more stable — and
iodide is a very large ion.

This is the one place in the subject where the obvious answer is wrong, and it
is worth stating as a slogan: **across a row, electronegativity; down a column,
size.** Element effects are also the strongest of the four factors; when they
point one way and another factor points the other, element effects usually win.

### 2. Inductive effects

An inductive effect is the pull of electron density **through σ bonds**, caused
by electronegativity differences. It is transmitted through the bonding
framework, not through space, and it dies off fast with distance.

The canonical comparison: **2,2,2-trifluoroethanol** (CF₃CH₂OH, pKa 12.4) is far
more acidic than **ethanol** (CH₃CH₂OH, pKa 16). The acidic hydrogen is on
oxygen in both. What differs is that three fluorines two bonds away pull
electron density out of the conjugate base's oxygen, spreading the charge and
stabilizing it.

Three dependencies: the more electronegative the atom, the greater the effect;
the more such atoms, the greater; and the closer they are to the charge, the
greater. An electron-withdrawing group on the far end of a long chain does
essentially nothing.

### 3. Resonance effects

Delocalizing the charge over several atoms stabilizes it, and this is often
worth more than any inductive effect.

**Acetic acid** (CH₃COOH, pKa 4.7) is eleven orders of magnitude more acidic
than **ethanol** (pKa 16), even though in both the proton comes off an oxygen
and the charge lands on an oxygen. Same element, same row, same column —
element effects predict a tie.

The difference is entirely in the conjugate bases. **Ethoxide**, CH₃CH₂O⁻, has
its charge localized on one oxygen. **Acetate**, CH₃COO⁻, has two equivalent
resonance contributors, so the charge is shared equally over two oxygens and
every C–O bond is identical. Electrostatic potential maps show the point
directly: ethoxide has one intense pocket of negative charge, acetate has it
smeared over both oxygens.

Eleven pKa units — a factor of 10¹¹ — for one resonance contributor. This is why
resonance is the first thing to look for.

### 4. Hybridization effects

Compare three C–H bonds:

- **ethane**, CH₃CH₃, sp³ carbon, pKa 50
- **ethene**, H₂C=CH₂, sp² carbon, pKa 44
- **ethyne**, HC≡CH, sp carbon, pKa 25

All three put the charge on carbon, so element effects are identical, there is
no inductive group and no resonance. The only difference is the orbital holding
the lone pair in the conjugate base: sp³ (25% s), sp² (33% s), sp (50% s).

An s orbital has electron density **at** the nucleus; a p orbital has a node
there. So electrons in a hybrid with more s-character sit closer to the
positively charged nucleus, interact with it more strongly, and are lower in
energy. More s-character ⇒ more stable anion ⇒ stronger acid.

Twenty-five pKa units from nothing but hybridization. This is also why the
terminal alkyne C–H is the one acidic proton in all of hydrocarbon chemistry,
and it is the basis of acetylide chemistry in chapter 13.

---

## Part 5 — bases, and the reagents you will actually use

### Acids used in practice

Alongside HCl and H₂SO₄, two organic acids appear constantly:

- **Acetic acid**, CH₃COOH, pKa 4.7 — a mild acid, often used as a solvent too.
- **p-Toluenesulfonic acid**, TsOH, pKa ≈ −2.8 — a strong acid that is a
  convenient crystalline solid rather than a corrosive liquid. Its strength
  comes from the **three** equivalent resonance contributors available to the
  sulfonate conjugate base, which spread the charge over three oxygens.

### What makes a strong base

- Strong bases have **weak conjugate acids**, with high pKa — usually above 12.
- Strong bases usually carry a net negative charge, but **not every anion is a
  strong base.** The halides F⁻, Cl⁻, Br⁻ and I⁻ are not, because their
  conjugate acids are strong acids. They are excellent *nucleophiles* and poor
  bases, and chapter 6 depends on that distinction.
- **Carbanions are exceptionally strong bases**, because their conjugate acids
  are alkanes with pKa around 50. The standard reagent is **butyllithium**,
  BuLi, which is strong enough to deprotonate almost anything and reactive
  enough to require handling under inert atmosphere.

Common bases in order of increasing strength: hydroxide and alkoxides
(conjugate acids at pKa 15–18), amide NH₂⁻ (pKa 35), carbanions (pKa ~50).

### Neutral nitrogen bases

Amines — triethylamine, pyridine — are basic because nitrogen has a lone pair.
They are weaker than anionic bases because they are neutral, but they are the
bases you actually reach for when you need to mop up a proton without starting
side reactions.

Ranking them uses **pKaH**, the pKa of the *conjugate acid*. Higher pKaH means
the protonated form holds its proton more tightly, which means the base is
stronger. Two factors decide:

- **availability of the lone pair** for protonation, and
- **stability of the conjugate acid** once formed.

Three effects follow, and notice that they are the same effects as for acids,
run in reverse:

**Inductive.** Nitrogen attached to an electron-withdrawing group is less basic:
the EWG pulls density out of the lone pair, making it less available. A nitrogen
flanked by fluorines or carbonyls is barely basic at all.

**Hybridization.** A lone pair in sp is held closer to the nucleus than one in
sp³, so it is more stable and *less available to react*. Basicity therefore
falls sp³ > sp² > sp — the mirror image of the acidity trend. This is why
pyridine (sp², pKaH 5.2) is far less basic than piperidine (sp³, pKaH 11.1),
and why a nitrile nitrogen (sp) is essentially non-basic.

**Conjugation.** A lone pair delocalized into a π system is not a lone pair any
more. Pyrrole's nitrogen lone pair is part of the aromatic sextet and the
compound is not basic in the ordinary sense; an amide nitrogen's lone pair is
delocalized onto the carbonyl oxygen, which is why amides are roughly 10¹⁰ times
less basic than amines and why proteins have rigid, planar peptide bonds.

> **A worked equilibrium.** Take a C–H with pKa ≈ 35 and ask whether bicarbonate
> (conjugate acid H₂CO₃, pKa 10.3) can deprotonate it. It cannot — not even
> slightly. The difference is about 25 pKa units, so the equilibrium constant is
> around 10⁻²⁵ and ΔG° is about +34 kcal mol⁻¹.
>
> Reversing an equilibrium like that is not a matter of using more base. It
> requires either a far stronger base, or removing the product as it forms —
> distilling it off, precipitating it, or letting it react onward irreversibly
> so that the unfavourable step is pulled forward. Le Châtelier is the whole
> toolkit, and most of synthetic chemistry's cleverness lives there.
{: .prompt-tip }

---

## Part 6 — the Lewis picture

### Definitions

- A **Lewis base** is an electron pair donor.
- A **Lewis acid** is an electron pair acceptor.

A Lewis base is structurally identical to a Brønsted–Lowry base: both need an
available electron pair, either a lone pair or the electrons of a π bond. The
difference is only in what they give it to. A Brønsted–Lowry base always donates
to a proton; a Lewis base donates to **anything electron-deficient**.

The containment runs one way. Every Brønsted–Lowry acid is a Lewis acid, because
H⁺ accepts an electron pair. The converse fails: BF₃ has no proton to donate but
is a perfectly good Lewis acid, because boron's empty p orbital
([unit 1](/posts/organic-chemistry-1-structure-bonding/)) accepts a pair.

The common Lewis acids that are not Brønsted acids are group 3A compounds —
BF₃, AlCl₃, BH₃ — precisely because they have unfilled valence shells. In the
reaction of BF₃ with water, the oxygen lone pair attacks boron and a new B–O
bond forms; boron picks up a formal negative charge and oxygen a positive one,
and nothing is deprotonated.

### The rename that matters

Lewis acid–base reactions are a special case of the one pattern that runs
through all of organic chemistry: **electron-rich species react with
electron-poor species.** Once you accept that, the terminology changes to match:

- A Lewis acid is an **electrophile** — "electron-loving", the electron-poor
  partner, the one attacked.
- A Lewis base reacting with anything other than a proton is a
  **nucleophile** — "nucleus-loving", the electron-rich partner, the attacker.

In the BF₃ + H₂O reaction, BF₃ is the electrophile and water the nucleophile.

The distinction between "base" and "nucleophile" is the same species viewed
through two different questions: basicity is a *thermodynamic* property measured
against a proton, nucleophilicity is a *kinetic* property measured against
carbon. Iodide is a weak base and an excellent nucleophile. Separating those two
scales is the central skill of chapters 6 and 7.

Note finally what does *not* happen in a Lewis acid–base reaction: the electron
pair is not removed from the base. It is *donated*, and one new covalent bond
forms with both electrons coming from the same atom. That is a **dative** or
coordinate bond, and it is drawn and counted exactly like any other bond once
it exists.

---

## Connections

- **Backward.** Resonance, formal charge and hybridization from
  [unit 1](/posts/organic-chemistry-1-structure-bonding/) are doing all the work
  in parts 4 and 5. The empty p orbital of BH₃ becomes the definition of an
  electrophile.
- **Forward.** ΔH° from bond strengths is the computational core of
  [unit 5](/posts/organic-chemistry-1-radical-halogenation/), and the potential
  energy diagram there acquires the Hammond postulate. pKa decides which base
  to use in every elimination in chapter 7, and the base-versus-nucleophile
  split is what chapter 6 is about.
- **Outward.** The Arrhenius equation and the Boltzmann tail are the same
  physics as in physical chemistry; the Hammett equation, which quantifies
  inductive and resonance effects on a single scale, is the natural sequel to
  part 4.

## Summary

- **Thermodynamics and kinetics are independent** — ΔG° is the endpoints, Ea is the highest point
- **ΔG° = −RT ln K**; at 25 °C, ΔG° = −1.36 log K, so one order of magnitude in K costs 1.36 kcal mol⁻¹
- **ΔH° = bonds broken − bonds made**; negative is exothermic
- **ΔS° in e.u.**; if the molecule count is unchanged, ΔS° is small and ΔH° decides
- **Four rate factors** — barrier height, temperature, concentration, probability
- **Average thermal energy is 0.6 kcal mol⁻¹ against barriers near 20** — reactions run on the Boltzmann tail
- **Rate law counts molecules in the transition state**; Arrhenius extracts Ea
- **The rate-determining step is the highest transition state**, not the slowest-looking one
- **Acid = proton donor**; curved arrows start at electrons, never at charges
- **pKa = −log Ka; low pKa, strong acid.** Water 15.7, acetic acid 4.7, methane ~50
- **Water is 15.7 not 14** because Ka divides by [H₂O] = 55.5 M
- **pKa is solvent-dependent** — the table is aqueous and DMSO reorders it
- **To compare acids, draw the conjugate bases** and ask which anion is happier
- **Element effects** — across a row, electronegativity; down a column, size
- **Inductive** — σ-withdrawal, stronger when closer; CF₃CH₂OH beats CH₃CH₂OH
- **Resonance** — acetate over ethoxide, worth 11 pKa units
- **Hybridization** — more s-character, more stable anion; ethyne 25 vs ethane 50
- **Halides are weak bases but good nucleophiles**; carbanions are the strongest bases
- **pKaH ranks neutral bases**; basicity falls with EWGs, with s-character, and with conjugation
- **Lewis acid = electrophile, Lewis base = nucleophile** — electron-rich attacks electron-poor

## References

- Peter C. Vollhardt & Neil E. Schore, *Organic Chemistry: Structure and Function*, 8th edition — chapter 2. The pKa values are Table 2.2.
- Janice G. Smith, *Organic Chemistry* — the four-factor treatment of acid strength, the conjugate-base comparison method, and the Lewis acid–base material follow her organization, which is what the lecture slides use.
- Organic Chemistry 1 (3343.205), Seoul National University, Spring 2023. Instructor: Seung Youn Hong (홍승윤). Lecture of 9 March 2023, "Week 02-2: Structure and Reactivity", 54 slides.
- The reaction coordinate figure is drawn for these notes rather than reproduced; the slide versions are publisher artwork.
- The pKa-of-water derivation, the DMSO caveat and the bicarbonate equilibrium problem are the lecturer's, worked out in full here. The slides pose the last as a question and leave the numbers to the reader.
- pKa values not given in the lecture — trifluoroethanol 12.4, ethanol 16, TsOH −2.8, pyridine and piperidine as conjugate acids — are standard values added for the comparisons to be quantitative.
