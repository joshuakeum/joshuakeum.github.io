---
title: "Organic Chemistry 1: Functional Groups and Physical Properties"
date: 2026-10-09 13:30:00 +0900
categories: [Course Notes, Organic Chemistry 1]
tags: [functional groups, intermolecular forces, hydrogen bonding, boiling point, solubility]
description: What a functional group is and why it localizes reactivity, van der Waals forces, dipole-dipole interactions and hydrogen bonding, and how they set boiling point, melting point and solubility. Unit 3 of Organic Chemistry 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers the first half of the lecture of 14 March 2023, "Functional
> Group & Alkanes". The material is Vollhardt chapter 2's closing sections
> reorganized along the lines of Janice Smith's chapter 3, which is where the
> slide artwork comes from. The second half of the lecture is
> [unit 4](/posts/organic-chemistry-1-alkanes/).
{: .prompt-info }

## What this unit answers

Organic chemistry would be impossible if every bond in a molecule were equally
reactive. A modest natural product has sixty or eighty bonds; if a reagent
attacked all of them you could never do anything deliberate.

It does not, and the reason is the **functional group**. Reactivity is
localized — concentrated at a small number of sites, each of which behaves the
same way no matter what molecule it is attached to. A ketone in a steroid reacts
like a ketone in acetone. That transferability is what makes the subject
learnable: you learn perhaps twenty functional groups and their reactions
rather than a reaction for every molecule.

The second half of the unit is about what functional groups do when they are
*not* reacting. Boiling point, melting point and solubility are all determined
by intermolecular forces, and intermolecular forces are determined by functional
groups. This is the practical half of the subject — it is how you choose a
solvent, how you work up a reaction, and how you separate a product from
everything else in the flask.

## Prerequisites

[Unit 1](/posts/organic-chemistry-1-structure-bonding/) for bond polarity,
electronegativity, lone pairs and molecular shape.

---

## Part 1 — functional groups

### Definition

A **functional group** is an atom or group of atoms with characteristic chemical
and physical properties. It controls the reactivity of the molecule as a whole.

The structural picture is a **carbon backbone** — C–C and C–H bonds, inert — to
which functional groups are attached. Everything interesting happens at the
attachment points.

Two structural features make a functional group a functional group:

- **Heteroatoms** — any atom that is not carbon or hydrogen. They bring lone
  pairs and electronegativity, which means polarity, which means a δ+ carbon
  that nucleophiles can attack and a δ− heteroatom that can act as a base.
- **π bonds** — most commonly C=C and C=O. A π bond is weaker than a σ bond and
  its electrons are further from the nuclei, which makes them available: a C=C
  is a nucleophile, and a C=O is polarized so strongly that its carbon is one
  of the best electrophiles in the subject.

### The families

**Hydrocarbons** contain only carbon and hydrogen:

| Family | Feature |
|---|---|
| Alkane | all single bonds — no functional group at all |
| Alkene | C=C |
| Alkyne | C≡C |
| Arene | a benzene ring |

**C–Z σ bonds**, where Z is an electronegative heteroatom. These all have a δ+
carbon and are the substrates of chapters 6 to 9:

| Family | Feature |
|---|---|
| Alkyl halide | C–X, where X is F, Cl, Br or I |
| Alcohol | C–OH |
| Ether | C–O–C |
| Amine | C–N |
| Thiol | C–SH |

**C=O, the carbonyl group**, which is the single most important functional group
in organic chemistry. The parent is the aldehyde and ketone; the rest are
carbonyls with a heteroatom attached, and that heteroatom changes everything
about their reactivity:

| Family | Feature |
|---|---|
| Aldehyde | C(=O)H |
| Ketone | C(=O)C |
| Carboxylic acid | C(=O)OH |
| Ester | C(=O)OR |
| Amide | C(=O)NR₂ |
| Acyl chloride | C(=O)Cl |

An ordinary drug molecule carries several at once. The antibiotic the lecture
opened with has six: an ester, a carboxylic acid, an amide, an alcohol, and
both a primary and a secondary amine — every one of them a separate handle for
chemistry, and every one a separate liability in storage.

### Parts of a functional group

When analysing reactivity, look for three things:

- **Lone pairs** — a site that can donate, i.e. a base or nucleophile.
- **π bonds** — likewise electron-rich, and attackable from above or below the
  plane.
- **Polar σ bonds** — a δ+ carbon that will be attacked, and a heteroatom that
  will leave with the electrons.

Almost every reaction in the course is one of these three features meeting its
opposite.

> **Why alkanes get a chapter anyway.** Alkanes have none of the three. No
> heteroatom, no π bond, no polar bond, no lone pair, nothing to attack and
> nothing to attack with. They are the only compound class in the course
> *defined* by having no functional group — and the whole of
> [unit 5](/posts/organic-chemistry-1-radical-halogenation/) is about the one
> kind of chemistry that still works on them.
>
> This is also why **C–H functionalization** is a live research area rather than
> a solved problem. Turning an unactivated C–H bond into C–X selectively, in a
> molecule full of more reactive groups, is one of the hardest things in
> synthesis — the instructor flagged it as a state-of-the-art topic, and it is
> what his own laboratory works on.
{: .prompt-tip }

---

## Part 2 — intermolecular forces

Ionic and covalent compounds behave entirely differently here. An ionic solid is
held together by full charges in a lattice and needs enormous energy to melt. A
covalent molecular compound is held to its neighbours only by the weak
interactions below, and those are what we need.

There are three, in order of increasing strength.

### van der Waals (London) forces

Very weak interactions caused by **momentary** fluctuations in electron density.
At any instant an electron cloud is slightly lopsided, creating a transient
dipole; that dipole induces a matching one in a neighbour, and the two attract.
The average dipole is zero, but the average *interaction* is not.

Every compound has them, and in a nonpolar compound they are the **only**
attractive force. Two things make them stronger:

**Surface area.** The larger the contact area between two molecules, the more
instantaneous dipoles can line up. This is why boiling point rises steadily
along a homologous series, and why branched isomers boil lower than straight
chains: a sphere has less surface for its volume than a rod. Pentane boils at
36 °C; neopentane, the same formula packed into a ball, boils at 10 °C.

**Polarizability.** How easily an electron cloud distorts. Large atoms with
loosely held valence electrons — iodine, sulfur — are highly polarizable; small
atoms holding their electrons tightly — fluorine — are not. This is why CH₃I
boils at 42 °C and CH₃F at −78 °C.

### Dipole–dipole interactions

Attraction between the **permanent** dipoles of polar molecules. Neighbouring
molecules align so that δ+ sits near δ−; in liquid acetone the carbonyls stack
in alternating directions.

Much stronger than van der Waals forces, because the dipoles are always there
rather than flickering in and out.

### Hydrogen bonding

The special case, and the strongest of the three between neutral molecules. It
occurs when a hydrogen **bonded to O, N or F** is attracted to a **lone pair on
an O, N or F** in another molecule.

The restriction to those three elements is not arbitrary. They are small and
very electronegative, so the H–X bond is extremely polar and the hydrogen — a
bare proton with essentially no electron density of its own — gets unusually
close to the lone pair. A hydrogen bond runs 3 to 10 kcal mol⁻¹, perhaps a
twentieth of a covalent bond, but twenty times a van der Waals contact.

It is also why water is a liquid at room temperature while H₂S, which is
heavier, is a gas; why alcohols boil far above ethers of the same mass; and why
DNA has two strands.

### Summary of part 2

As the polarity of an organic molecule increases, so does the strength of its
intermolecular forces — van der Waals only, then plus dipole–dipole, then plus
hydrogen bonding.

---

## Part 3 — physical properties

### Boiling point

Boiling means separating molecules from one another entirely, so the boiling
point measures intermolecular force strength directly.

**At comparable molecular weight**, the ordering follows the forces: nonpolar
compounds boil lowest, polar aprotic ones higher, hydrogen-bonding ones highest.
Butane (58 g mol⁻¹, nonpolar) boils at 0 °C; acetone (58, dipole–dipole) at
56 °C; propan-1-ol (60, hydrogen bonding) at 97 °C.

**Within a functional group class**, two things raise the boiling point: larger
surface area, and more polarizable atoms.

### Melting point

Melting means breaking up a crystal lattice, which is a different question —
and this is where the two properties come apart.

Stronger intermolecular forces still raise the melting point. But a second
factor enters that has no effect on boiling: **symmetry**. A compact,
symmetrical molecule packs efficiently into a lattice, with many good contacts
per molecule, and takes more energy to dislodge.

The standard demonstration is the pentanes. Neopentane, a near-spherical
molecule, melts at −17 °C. Isopentane, the same formula in an awkward branched
shape that cannot tile space, melts at −160 °C — a difference of 143 degrees
from shape alone. Note that the boiling points go the other way (10 °C versus
28 °C), because boiling rewards surface area and melting rewards packing. The
two properties are measuring genuinely different things.

### Solubility

**Solubility** is the extent to which a solute dissolves in a solvent.
Dissolving costs energy — you have to break up solute–solute interactions and
push the solvent apart — and that cost is paid by the new solute–solvent
interactions formed. Dissolution happens when the new interactions are
comparable to the ones destroyed.

That is the whole content of **"like dissolves like"**, and it is worth working
through why the slogan is true rather than memorizing it.

> **Why do likes dissolve likes?** Take two failures.
>
> **NaCl in hexane.** The Na⁺–Cl⁻ interaction is a full ion–ion attraction,
> enormously strong. The best hexane can offer in return is an ion-induced
> dipole. The books do not balance, so there is no incentive for solvation and
> the salt sits at the bottom.
>
> **Hexane in water.** Now the reverse. Water–water hydrogen bonding is strong;
> the water–hexane interaction that would replace it is a weak van der Waals
> contact. Dissolving hexane would mean breaking good hydrogen bonds to make
> bad contacts, so again no.
>
> Notice that in neither case is the problem the solute "hating" the solvent.
> The problem is always that the *interaction being destroyed* is stronger than
> the one being created. Hydrophobicity is not a repulsion; it is water
> preferring its own company.
{: .prompt-tip }

Consequences:

- **Ionic compounds** are mostly water-soluble and organic-insoluble. Water
  replaces strong ion–ion interactions with many weaker ion–dipole ones, and
  wins on numbers; organic solvents cannot.
- **Polar organic compounds** dissolve in polar solvents — water, alcohols —
  that can hydrogen bond to them.
- **Nonpolar compounds** dissolve in nonpolar solvents such as hexane or carbon
  tetrachloride, or in weakly polar ones such as diethyl ether.

### Hydrophilic and hydrophobic

Most real organic molecules are both. A molecule has a **hydrophilic** part —
the polar, hydrogen-bonding functional groups — and a **hydrophobic** part — the
hydrocarbon skeleton. Which dominates decides the behaviour, and for simple
compounds the rule of thumb is a ratio: an alcohol with up to about five
carbons per OH group is water-soluble, and beyond that it is not. Methanol,
ethanol and propanol are miscible with water in all proportions; hexanol is
essentially insoluble.

When the two parts are both large and clearly separated, the molecule is a
**surfactant** and does something more interesting than dissolving: it
assembles, with the hydrophobic tails buried together and the hydrophilic heads
facing the water. That is soap, and it is also the cell membrane.

> **Why milk and not water.** Capsaicin, the compound that makes chillies hot,
> is largely hydrophobic — a long nonpolar tail on a modestly polar aromatic
> head. Water cannot solvate the tail, so drinking water spreads the capsaicin
> around without removing it.
>
> Milk works because it contains casein, a protein with hydrophobic regions,
> and fat. Both provide the nonpolar environment capsaicin prefers, so it
> partitions out of your tissue and into the milk. "Like dissolves like" is
> not an abstraction; it is dinner.
{: .prompt-info }

---

## Connections

- **Backward.** Bond polarity and lone pairs from
  [unit 1](/posts/organic-chemistry-1-structure-bonding/) are the whole basis of
  this unit — a functional group is just a place where unit 1's features are
  concentrated.
- **Forward.** [Unit 4](/posts/organic-chemistry-1-alkanes/) takes the one
  family defined by having no functional group, and
  [unit 5](/posts/organic-chemistry-1-radical-halogenation/) shows what it takes
  to react with it. Solvent choice becomes a mechanistic variable in chapter 6,
  where polar protic and polar aprotic solvents favour different substitution
  pathways.
- **Outward.** Intermolecular forces are what chromatography separates on, what
  recrystallization exploits, and what a liquid–liquid extraction in a
  separating funnel is doing. The hydrophobic effect is the organizing principle
  of protein folding and membrane biology.

## Summary

- **A functional group localizes reactivity** — a ketone behaves like a ketone wherever it sits
- **Three structural features** — heteroatoms, π bonds, polar σ bonds
- **Alkanes have none of them**, which is why they are inert and why C–H functionalization is hard
- **The carbonyl** is the central functional group; its family members differ by what is attached
- **van der Waals (London)** — momentary dipoles, present in everything, the only force in nonpolar compounds
- **Stronger with surface area and with polarizability** — pentane beats neopentane, iodide beats fluoride
- **Dipole–dipole** — permanent dipoles aligning, stronger than van der Waals
- **Hydrogen bonding** — H on O, N or F to a lone pair on O, N or F; 3–10 kcal mol⁻¹
- **Boiling point** tracks intermolecular force strength and surface area
- **Melting point** tracks force strength **and symmetry** — neopentane melts 143° above isopentane
- **Like dissolves like** because dissolution must repay the interactions it destroys
- **Hydrophobicity is not repulsion** — it is water preferring its own hydrogen bonds
- **Roughly five carbons per polar group** is the water-solubility cutoff

## References

- Peter C. Vollhardt & Neil E. Schore, *Organic Chemistry: Structure and Function*, 8th edition — chapter 2, functional groups and physical properties.
- Janice G. Smith, *Organic Chemistry* — chapter 3. The intermolecular forces sequence, the figures on surface area and polarizability, and the solubility treatment follow her organization, which is what the slides use.
- Organic Chemistry 1 (3343.205), Seoul National University, Spring 2023. Instructor: Seung Youn Hong (홍승윤). Lecture of 14 March 2023, "Week 03-1: Functional Group & Alkanes", slides 1–28.
- The "why do likes dissolve likes" argument with NaCl in hexane and hexane in water, and the capsaicin-and-milk example, are the lecturer's.
- Specific boiling and melting points — the pentanes, the 58 g mol⁻¹ comparison set, CH₃I against CH₃F, the hydrogen bond energy range and the five-carbon solubility rule — are standard values added here; the slides give the trends without the numbers.
