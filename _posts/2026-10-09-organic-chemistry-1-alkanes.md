---
title: "Organic Chemistry 1: Alkanes — Nomenclature and Conformation"
date: 2026-10-09 13:40:00 +0900
categories: [Course Notes, Organic Chemistry 1]
tags: [alkanes, iupac nomenclature, isomers, newman projection, conformation, torsional strain]
description: Constitutional isomers and homologous series, the IUPAC naming rules worked on a hard example, then Newman projections, staggered and eclipsed ethane, anti and gauche butane, and torsional versus steric strain. Unit 4 of Organic Chemistry 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers the second half of the lecture of 14 March 2023, "Functional
> Group & Alkanes" — slides 29 to 61, corresponding to Vollhardt chapter 2's
> treatment of alkanes and the start of chapter 3. The first half is
> [unit 3](/posts/organic-chemistry-1-functional-groups/).
{: .prompt-info }

## What this unit answers

Alkanes are the compounds with no functional group: only C–C and C–H σ bonds,
no lone pairs, no π bonds, no polar bonds. They have no reactive sites, and
they are consequently very unreactive.

So why spend a lecture on them?

Two reasons, and both are about infrastructure rather than chemistry.

**Naming.** Every compound in the course is named as a substituted alkane. The
IUPAC rules are learned once, on the family where nothing else is going on, and
then used for the next two years. Getting them wrong is not a small error —
the name *is* the structure, and a misnumbered chain is a different compound.

**Conformation.** A C–C single bond rotates, so a molecule with one is not a
single shape but a continuously varying family of them. Which shapes are
populated, and at what cost, turns out to control reaction rates. This unit
introduces the analysis on ethane and butane, where the answer is simple;
chapter 4 applies it to cyclohexane, where it becomes the most important
geometric fact in the subject.

## Prerequisites

[Unit 1](/posts/organic-chemistry-1-structure-bonding/) for sp³ hybridization,
tetrahedral geometry and hashed-wedged drawings.
[Unit 3](/posts/organic-chemistry-1-functional-groups/) for why alkanes are
inert.

---

## Part 1 — structure and isomerism

### Tetrahedral carbon

Every carbon in an alkane has four groups around it, so every one is sp³
hybridized and tetrahedral with bond angles of 109.5°. The flat zig-zag that
everyone draws is a projection; the real molecule is a three-dimensional chain
of tetrahedra, and the zig-zag drawing is the tetrahedral angle viewed
edge-on.

### Constitutional isomers

**Butane** and **isobutane** both have the formula C₄H₁₀. They are different
compounds — different boiling points, different melting points, separable — and
they differ only in how the atoms are connected: four carbons in a row, versus
three with a branch.

Two compounds with the same molecular formula and different connectivity are
**constitutional isomers** (also called structural isomers). The count grows
fast: C₄H₁₀ has 2, C₅H₁₂ has 3, C₆H₁₄ has 5, C₁₀H₂₂ has 75, and C₃₀H₆₂ has over
four billion. This combinatorial explosion is the reason a systematic naming
scheme is not optional.

### Homologous series

Insert a –CH₂– group into a C–C bond and you move one step along a
**homologous series**: methane, ethane, propane, butane, pentane, and so on.
Members of a series share chemical behaviour and vary smoothly in physical
properties.

The general formulas, which are worth knowing cold:

- **Acyclic alkane** — CₙH₂ₙ₊₂, written as a straight chain CH₃(CH₂)ₓCH₃
- **Cycloalkane** — CₙH₂ₙ

Closing a ring costs two hydrogens. More generally, each ring or π bond in a
molecule reduces the hydrogen count by two relative to the saturated formula,
and counting those **degrees of unsaturation** is the first thing to do with a
molecular formula from a mass spectrum.

**Cycloalkanes** are named by adding the prefix *cyclo-* to the alkane with the
same number of carbons: cyclopropane, cyclobutane, cyclopentane, cyclohexane.

---

## Part 2 — IUPAC nomenclature

The suffix **-ane** identifies a molecule as an alkane. Four rules build the
rest.

### Rule 1 — find and name the longest chain

The **parent** is the longest continuous carbon chain, which is not necessarily
the one drawn horizontally. A molecule drawn as a branched pentane may well be
a hexane.

If two chains tie for longest, **choose the one with more substituents.** A
seven-carbon chain with three branches beats a seven-carbon chain with two.

### Rule 2 — name the substituents

Substituents are alkyl groups or halogens.

**Halogens** become *fluoro-, chloro-, bromo-, iodo-*.

**Straight-chain alkyl groups** take the alkane name with *-ane* changed to
*-yl*: methane → methyl, hexane → hexyl. The shorthand is that R–H is an alkane
and R– is the corresponding alkyl group.

**Branched alkyl groups** are named as substituted alkyl groups, by the same
rules applied recursively: find the longest chain *starting from the point of
attachment*, then name its own substituents.

**Repeated substituents** take multiplying prefixes. For simple substituents,
*di-, tri-, tetra-, penta-*: two methyls make a dimethyl. For **branched**
substituents, where *di-* would be ambiguous, use *bis-, tris-, tetrakis-* and
put the substituent name in parentheses: bis(1-methylethyl), not
di(1-methylethyl).

**Common names** survive in practice and the course uses them colloquially:
*isopropyl* for 1-methylethyl, *tert-butyl* for 1,1-dimethylethyl, *neopentyl*
for 2,2-dimethylpropyl.

### Rule 3 — number the chain

Number from the end **closest to a substituent**.

If both ends are equidistant from the first substituent, keep going to the
**first point of difference** and number so that the lower number comes first
there.

For a branched substituent, the carbon of attachment is defined as C1 of that
substituent's own numbering.

### Rule 4 — assemble the name

List substituents in **alphabetical order**, not numerical, each with its
position number. Then two sub-rules about the prefixes:

- Multiplying prefixes (*di-*, *tri-*) are **not** counted for alphabetization
  of the main stem: "4-ethyl-2,3-dimethyl…" alphabetizes ethyl under E and
  methyl under M, ignoring the *di-*.
- They **are** counted when they are part of a branched substituent's own name:
  "(1,2-dimethylpropyl)" alphabetizes under D.

### A worked example

The lecture's practice problem, which is deliberately unpleasant:

> **Step 1 — longest chain.** Count carefully; it is an **octane**, eight
> carbons, and it is not the chain the drawing emphasizes.
>
> **Step 2 — substituents.** A bromo; an iodo; two methyls on the same carbon;
> and a branched group that is itself a substituted ethyl — a
> **1-chloroethyl**, named by taking its attachment carbon as C1 and finding
> the chlorine there.
>
> **Step 3 — number.** Numbering from the bromine end puts the first
> substituent at C1; from the other end the first would be at C2. So number
> from the bromine.
>
> **Step 4 — alphabetize.** bromo, chloroethyl, iodo, methyl — B, C, I, M. The
> *di-* in dimethyl does not count; the *chloro* inside the parenthesized
> substituent does.
>
> **Answer:** 1-bromo-5-(1-chloroethyl)-7-iodo-2,2-dimethyloctane.

Three things that example is testing: that you find the real longest chain,
that you can name a substituent recursively, and that you alphabetize rather
than order by position.

---

## Part 3 — conformational analysis

### Conformations are not isomers

**Conformations** are different arrangements of the same atoms, interconverted
by rotation about single bonds.

This is a different relationship from any other in the course, and it is worth
separating from two things it resembles:

- **Not resonance.** Resonance structures are drawings of one unchanging
  electronic structure; nothing moves. Conformations are genuinely different
  geometries, and the molecule really does move between them.
- **Not isomers.** Constitutional isomers are separable compounds. Conformations
  interconvert millions of times a second at room temperature and cannot be
  isolated at all under ordinary conditions.

What they *do* control is population. Low-energy conformations are occupied more
than high-energy ones, and since reactions happen from particular geometries,
the population distribution sets the rate.

### Newman projections

The standard tool: look straight **down** a C–C bond, so the two carbons are
one behind the other.

**How to draw one.**

1. Sight along the C–C bond end-on. Draw a circle with a dot at its centre. The
   dot is the **front** carbon, the circle the **back** carbon.
2. Draw the front carbon's three bonds as lines meeting at the centre. Draw the
   back carbon's three bonds as lines starting at the **edge** of the circle.
3. Add the atoms at the ends.

The whole value of the projection is that it makes the **dihedral** (torsional)
angle — the angle between a front bond and a back bond, viewed along the
axis — directly visible, which no other drawing does.

### Ethane

Two limiting conformations, 60° apart:

- **Staggered** — each front C–H bisects a back H–C–H angle. The bonds are as
  far from each other as they can get.
- **Eclipsed** — each front C–H is directly aligned with a back C–H.

Staggered is lower in energy by about **3 kcal mol⁻¹**, and since there are
three eclipsing interactions, each eclipsed H,H pair contributes about
**1 kcal mol⁻¹**.

That difference is called **torsional energy**, and the penalty for eclipsing is
**torsional strain**. It is small — comparable to the thermal energy available
at room temperature — so ethane rotates essentially freely, passing through the
barrier roughly 10¹¹ times a second. "Freely rotating" is an approximation, but
a good one.

> **Where torsional strain comes from.** The textbook answer used to be that
> eclipsed C–H bonds repel each other electrostatically. The modern answer,
> which the lecture ends on, is **hyperconjugation**: in the staggered
> conformation each filled σ(C–H) bonding orbital is **anti-periplanar** to a
> σ\*(C–H) antibonding orbital on the adjacent carbon, and that alignment is
> exactly the geometry for the two to overlap. Electron density flows from the
> filled orbital into the empty one, and the molecule is stabilized.
>
> In the eclipsed conformation the alignment is wrong and the stabilization is
> lost. So staggered is not so much *penalized less* as *rewarded more*. This
> is a **stereoelectronic effect** — an energy that depends on the relative
> orientation of orbitals rather than on sterics — and the same
> filled-into-empty, donor-into-acceptor analysis explains the anomeric effect
> in sugars and the geometry requirements of E2 elimination in chapter 7.
{: .prompt-info }

### Butane

Butane is the smallest alkane where rotation about the central C2–C3 bond gives
genuinely different conformations, because now the front and back carbons each
carry a methyl group as well as two hydrogens. Six conformations, at 60°
intervals:

- **Anti** (dihedral 180°) — the two methyls as far apart as possible.
  The global minimum; take this as zero.
- **Gauche** (60° and 300°) — staggered, but with the methyls only 60° apart.
  About **0.9 kcal mol⁻¹** above anti. There are two of these, and they are
  mirror images.
- **Eclipsed** (120° and 240°) — methyl eclipsing hydrogen. A local maximum.
- **Totally eclipsed** (0°) — methyl eclipsing methyl. The global maximum.

![Potential energy curve for rotation about the central bond of butane through 360 degrees, with Newman projections at each minimum and maximum: anti at 180 degrees as the lowest point, two gauche minima at 60 and 300 degrees, and three eclipsed maxima including the methyl-methyl eclipse at 0 degrees](/assets/img/organic-chemistry-1/butane-conformations.svg)

The barriers, measured from the adjacent minimum: 3.6 kcal mol⁻¹ from anti over
the methyl–hydrogen eclipse into gauche, 4.0 from gauche over the
methyl–methyl eclipse, and 2.7 from gauche back over the other
methyl–hydrogen eclipse.

### Torsional strain versus steric strain

Butane needs **two** separate penalties, and distinguishing them is the point of
the whole analysis.

**Torsional strain** is the cost of eclipsing — it depends only on the dihedral
angle, and it is present in ethane where there is nothing bulky at all.

**Steric strain** is the cost of forcing two non-bonded atoms too close
together. It depends on *size*, not on dihedral angle as such, and ethane has
none of it.

The evidence that they are different is the gauche conformation. Gauche butane
is **staggered** — no eclipsing, so no torsional strain at all — and it still
sits 0.9 kcal mol⁻¹ above anti. That 0.9 is pure steric strain between two
methyl groups at 60°.

Vollhardt's Table 4.3 collects the increments, and they add:

| Interaction | Energy increase (kcal mol⁻¹) |
|---|---|
| H,H eclipsing | 1.0 |
| H,CH₃ eclipsing | 1.4 |
| CH₃,CH₃ eclipsing | 2.6 |
| gauche CH₃ groups | 0.9 |

Check the arithmetic against the curve, taking anti as zero. The
methyl–hydrogen eclipse at 120° has two H,CH₃ interactions plus one H,H:
1.4 + 1.4 + 1.0 = 3.8 predicted, against 3.6 measured. The methyl–methyl
eclipse at 0° has one CH₃,CH₃ plus two H,H: 2.6 + 1.0 + 1.0 = 4.6 predicted,
against 0.9 + 4.0 = 4.9 measured. Both agree to within three tenths of a
kcal mol⁻¹, which is the useful claim: you can **predict** a conformational
energy by counting interactions rather than measuring it.

### Barrier to rotation

The **barrier to rotation** is the energy difference between the lowest and
highest conformations — 3 kcal mol⁻¹ for ethane, 4.9 for butane. Both are small
enough that rotation is fast at room temperature and the conformations cannot be
separated. The equilibrium populations follow from ΔG°: the 0.9 kcal mol⁻¹ gap
puts butane at roughly 70% anti and 30% gauche at 25 °C, counting both gauche
forms.

Larger alkanes have many rotatable C–C bonds, each with its own profile, and the
number of conformations grows as 3ⁿ. The lowest-energy arrangement of a long
chain is all-anti, which is the extended zig-zag everyone draws — and that is
why the standard drawing is also the correct one.

---

## Connections

- **Backward.** sp³ geometry and the hashed-wedge convention from
  [unit 1](/posts/organic-chemistry-1-structure-bonding/); the inertness of
  alkanes from [unit 3](/posts/organic-chemistry-1-functional-groups/). The
  hyperconjugation explanation of torsional strain is the σ/σ\* language of
  unit 1 applied to conformations.
- **Forward.** [Unit 5](/posts/organic-chemistry-1-radical-halogenation/) uses
  the primary/secondary/tertiary classification that nomenclature sets up, and
  hyperconjugation again — this time stabilizing a radical rather than a
  conformation. Chapter 4 runs the whole conformational analysis on cyclohexane,
  where ring closure fixes the dihedral angles and the axial/equatorial
  distinction appears. Chapter 7's E2 elimination requires a specific dihedral
  angle, so conformation becomes a mechanistic requirement rather than a
  statistical one.
- **Outward.** Conformational analysis scales directly to macromolecules: the
  Ramachandran plot for proteins is the butane diagram in two dimensions, and
  the preference for all-anti chains is why lipid tails pack and why polyethylene
  crystallizes.

## Summary

- **Alkanes have no functional group** — sp³ throughout, 109.5°, unreactive
- **Constitutional isomers** differ in connectivity; the count explodes with carbon number
- **CₙH₂ₙ₊₂ acyclic, CₙH₂ₙ cyclic** — each ring or π bond costs two hydrogens
- **Rule 1** — longest chain; ties broken by more substituents
- **Rule 2** — *-yl* for alkyl, *halo-* for halogen; branched substituents named recursively from their attachment carbon
- **di/tri for simple, bis/tris for branched** substituents
- **Rule 3** — number from the end nearest a substituent, ties broken at the first point of difference
- **Rule 4** — alphabetical order; *di-* ignored in the stem, counted inside a branched substituent
- **Conformations are not resonance and not isomers** — they interconvert freely and cannot be separated
- **Newman projection** — front carbon is the dot, back carbon the circle
- **Ethane** — staggered beats eclipsed by 3 kcal mol⁻¹, 1 per eclipsed H,H pair
- **Torsional strain is really lost hyperconjugation** — σ(C–H) into σ\*(C–H), anti-periplanar
- **Butane** — anti 0, gauche +0.9, barriers 3.6 / 4.0 / 2.7 kcal mol⁻¹
- **Gauche is staggered and still strained**, which is what separates steric from torsional strain
- **Strain increments add** — count the interactions and predict the energy

## References

- Peter C. Vollhardt & Neil E. Schore, *Organic Chemistry: Structure and Function*, 8th edition — chapter 2, alkanes and conformations. The strain increments are Table 4.3 and the butane barriers are the figure accompanying it.
- Janice G. Smith, *Organic Chemistry* — the Newman projection "how to" and the conformation sequence follow her presentation, which is what the slides use.
- Organic Chemistry 1 (3343.205), Seoul National University, Spring 2023. Instructor: Seung Youn Hong (홍승윤). Lecture of 14 March 2023, "Week 03-1: Functional Group & Alkanes", slides 29–61.
- The butane energy figure is redrawn for these notes; the slide version is publisher artwork. The quoted barriers, 3.6 / 4.0 / 2.7 kcal mol⁻¹ and the 0.9 kcal mol⁻¹ gauche penalty, are as given on the slide.
- The worked nomenclature problem is the lecturer's, reproduced with the reasoning filled in; the slides give the question and the final answer on separate slides and work it out on the board.
- The additivity check against Table 4.3, the isomer counts, the 70:30 anti–gauche population and the note that conformations are not resonance structures are mine. The last is prompted by a handwritten annotation on the slide reading *"different from resonance"*.
- The hyperconjugation account of torsional strain extends the lecture's closing slide, "Stereoelectronic effects", which makes the donor–acceptor point for a lone pair into a σ\*(O–H) orbital and leaves the application to ethane's barrier unstated. The σ(C–H) → σ\*(C–H) version given here is the modern explanation of that barrier (Pophristic and Goodman, *Nature* **411**, 565, 2001); the connection to the anti-periplanar requirement in E2 is mine.
