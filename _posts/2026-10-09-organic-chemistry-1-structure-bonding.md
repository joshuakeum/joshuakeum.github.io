---
title: "Organic Chemistry 1: Structure and Bonding"
date: 2026-10-09 13:10:00 +0900
categories: [Course Notes, Organic Chemistry 1]
tags: [bonding, lewis structures, resonance, molecular orbitals, hybridization, vsepr]
description: Vitalism and Wöhler, ionic and covalent bonding, electronegativity, Lewis structures and formal charge, resonance, atomic and molecular orbitals, and hybridization through ethene and ethyne. Unit 1 of Organic Chemistry 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers the lecture of 6 March 2023, "Structure and Bonding",
> corresponding to Vollhardt chapter 1. It is the longest single lecture of the
> five and it is almost entirely revision of general chemistry — but revision
> aimed at a different target, so it is worth reading even if none of it is new.
{: .prompt-info }

## What this unit answers

General chemistry taught you to draw Lewis structures and to label a molecule
sp³. This unit asks a question general chemistry does not: **what are those
pictures for?**

The answer is that every one of them is a map of where the electrons are, and
electrons are the only thing that reacts. A lone pair is a place that will
attack something. An empty orbital is a place that will be attacked. A polar
bond is a place where one end is slightly one and the other end slightly the
other. By the end of this unit you should be able to look at a structure and
read off its reactive sites, which is the entire skill the rest of the course
builds on.

Three specific things to carry forward:

- **Formal charge**, because it tells you which resonance structure matters and
  which atoms are electron-poor.
- **Resonance**, because delocalization is the single most common reason one
  species is more stable than another — and stability differences are what
  drive every reaction.
- **Hybridization**, because the s-character of an orbital controls bond angle,
  bond length, bond strength, and — as unit 2 will show — acidity.

## Prerequisites

General chemistry: the periodic table, electron configuration, the octet rule,
and electronegativity. Nothing from later units.

---

## Part 1 — why organic chemistry is a subject

### Vitalism and its death

Until the early nineteenth century, "organic" meant *produced by a living
organism*, and the distinction was taken to be fundamental. Jöns Jacob
Berzelius, who coined the term, held the **vital force theory**: compounds made
by living things contained some animating principle that could not be
reproduced in a flask. Organic and inorganic chemistry were different sciences
because organic and inorganic matter were different kinds of stuff.

In 1828 Friedrich Wöhler heated ammonium cyanate — an unambiguously inorganic
salt — and got urea, an unambiguously organic product, excreted by mammals.

$$
\mathrm{NH_4^+\,OCN^-} \;\longrightarrow\; \mathrm{(NH_2)_2C{=}O}
$$

Wöhler wrote to Berzelius that he could make urea without needing a kidney,
whether of man or dog. The vital force did not survive the letter.

What makes the story worth telling is not the chemistry — the reaction is a
rearrangement, and Wöhler was trying to make something else — but what it
licensed. If organic compounds are just compounds, they can be *designed*. The
complexity of what chemists have been willing to attempt since then has grown
roughly exponentially: urea in 1828, two atoms of carbon; glucose by Emil
Fischer in 1890; morphine in 1952; vitamin B₁₂, a twenty-year international
effort finished in 1973; palytoxin, with its 64 stereocentres, in 1994; Taxol
in 1993.

### What carbon has that other elements do not

Carbon sits in the middle of the second row with four valence electrons, which
gives it three properties no other element combines:

- **It forms four strong covalent bonds**, so it can be a branch point.
- **It bonds to itself indefinitely** — catenation — in chains and rings,
  because the C–C bond is strong (about 90 kcal mol⁻¹) and is not destabilized
  by lone-pair repulsion the way N–N and O–O are.
- **Its bonds to hydrogen are unreactive**, so a carbon skeleton is a stable
  scaffold on which reactive groups can be hung.

Silicon is directly below carbon and does none of this well: Si–Si is weak,
Si–H is reactive, and Si–O is so strong that silicon chemistry collapses into
silicates.

---

## Part 2 — bonds

### Why bonds form at all

Two statements cover every bond in the course:

1. **Opposite charges attract** — Coulomb's law. Nuclei are positive, electrons
   are negative; a bond is an arrangement in which electron density sits between
   two nuclei and is attracted to both.
2. **Electrons prefer to be delocalized** — spreading an electron over more
   space lowers its energy. This is quantum mechanical rather than classical,
   and it is the reason resonance stabilizes, the reason larger ions are more
   stable, and the reason a bonding molecular orbital is lower in energy than
   either atomic orbital that made it.

Hold both together and you get the shape of every bond-energy curve: as two
atoms approach, attraction dominates and the energy falls; past a certain
separation the nuclei begin to repel each other and the energy climbs steeply.
The minimum is the **bond length**; its depth below the separated atoms is the
**bond strength**.

### The two extremes

**Ionic bonding** is the complete transfer of one or more electrons. It happens
when the electronegativity difference is large — lithium hands its 2s electron
to fluorine, and both end up with a noble-gas configuration: a *duet* for
hydrogen and lithium, which are filling a 1s shell, and an *octet* for
everything else in the second row. What holds the solid together afterwards is
pure electrostatics between the ions.

**Covalent bonding** is sharing. Two hydrogen atoms cannot both have the
electron, so they both have both, and the pair sits between the nuclei.

A sense of scale is worth keeping, because it explains why chemistry is about
electrons and not nuclei. A nucleus is about 10⁻¹⁵ m across; an atom is about
10⁻¹⁰ m. That is five orders of magnitude — if the nucleus were a marble on the
centre spot, the electrons would be in the stands. And a proton outweighs an
electron by a factor of roughly 1800. Nuclei are heavy, tiny and effectively
stationary; all the interesting motion is electronic.

### The middle: polar covalent bonds

Most bonds are neither. When two different atoms share a pair, the more
electronegative one takes a larger share, and the bond acquires a dipole: δ− on
the greedier atom, δ+ on the other.

Pauling's electronegativity scale runs from about 0.8 (caesium) to 4.0
(fluorine). The values that matter constantly in this course:

| Element | Electronegativity |
|---|---|
| H | 2.2 |
| C | 2.5 |
| N | 3.0 |
| O | 3.4 |
| F | 4.0 |
| Cl | 3.2 |
| Br | 3.0 |
| I | 2.7 |

Two consequences to internalize now. C–H is barely polar — the difference is
0.3, which is why hydrocarbons are inert and nonpolar. C–O and C–N are
noticeably polar, with the carbon δ+, which is why nearly every reaction in the
course happens at a carbon bearing a heteroatom.

### Molecular shape: VSEPR

Electron pairs around a central atom repel each other and get as far apart as
they can. Counting *all* pairs — bonding and lone — gives the geometry:

- **Two atoms** — linear, necessarily.
- **Three atoms, two electron groups** — linear, as in CO₂ and BeH₂.
  **Three atoms, three groups** (one a lone pair) — bent, as in H₂O and SO₂.
- **Four atoms, three groups** — trigonal planar, as in BH₃ and formaldehyde.
  **Four atoms, four groups** (one a lone pair) — trigonal pyramidal, as in NH₃.
- **Five atoms, four groups** — tetrahedral, as in CH₄.

Lone pairs take up more room than bonding pairs, because a bonding pair is
pinched between two nuclei and a lone pair is held by only one. That is why the
angles shrink as lone pairs are added: methane 109.5°, ammonia 107.3°, water
104.5°.

---

## Part 3 — Lewis structures

### The rules

1. **Count the valence electrons.** Add one per negative charge, subtract one
   per positive charge.
2. **Draw the skeleton** and connect the atoms with single bonds. Hydrogen and
   the halogens are almost always terminal; the least electronegative atom is
   usually central.
3. **Distribute the remaining electrons** as lone pairs, filling the outer atoms
   to an octet first, then the central atom.
4. **If the central atom is short of an octet, make multiple bonds** by
   converting a lone pair on a neighbour into a shared pair.

### Formal charge

Formal charge is the bookkeeping that tells you whether an atom has the number
of electrons it is entitled to.

$$
\mathrm{FC} = V - L - \tfrac{1}{2} B
$$

where $$V$$ is the atom's group valence electron count, $$L$$ the number of
electrons it holds in lone pairs, and $$B$$ the number of electrons in bonds to
it. The half is the point: in a shared pair, each atom gets credit for one
electron.
A cleaner way to say the same thing is that an atom's **effective electron
count** is its lone-pair electrons plus half its bonding electrons, and the
formal charge is how far that falls short of, or exceeds, the atom's valence
count.

Worked, for the nitrogen in the ammonium ion NH₄⁺: nitrogen's group valence
count is 5; it has no lone pairs; it has four bonds, so eight bonding electrons,
of which it gets four. Formal charge = 5 − 0 − 4 = +1. The charge lives on
nitrogen, not spread over the ion, and that is what the drawn "+" means.

> **The shortcut for CO₂.** You can skip step 4 by noticing that carbon needs
> four bonds and each oxygen needs two, and the only arrangement that satisfies
> both is O=C=O. Most small molecules yield to this kind of valence-counting
> faster than to the formal procedure, and it is worth developing the habit:
> C wants 4 bonds, N wants 3 plus a lone pair, O wants 2 plus two lone pairs,
> halogens want 1 plus three lone pairs.
{: .prompt-tip }

### Resonance

Some species cannot be drawn with one Lewis structure. The carbonate ion
CO₃²⁻ has one C=O and two C–O⁻ in any single drawing, but every measurement says
the three oxygens are identical and every C–O bond length is the same, between
a single and a double bond.

The resolution is that the true structure is none of the drawings. It is a
single, unchanging electronic structure — the **resonance hybrid** — and the
drawings are a limitation of the notation. The double-headed arrow ↔ between
contributors does *not* mean the molecule interconverts. Nothing moves. The
molecule is the average, all the time.

Resonance always lowers energy, by rule 2 above: the electrons are spread over
more atoms.

### Ranking resonance contributors

Contributors do not usually weight equally. Three rules, in order of priority:

1. **A structure with complete octets beats one without.** This outranks
   everything else.
2. **Negative charge belongs on the more electronegative atom**, and positive
   charge on the less electronegative.
3. **Fewer charges, and less separation between them, is better.**

The order matters, because the rules disagree. In the **enolate** anion, the
charge can sit on carbon or on oxygen with complete octets either way, so rule 2
decides and the oxygen contributor dominates — which is why enolates react at
carbon but are stabilized by oxygen. In **formic acid**, the neutral structure
and the charge-separated one both have octets, and rule 3 picks the neutral one.

The instructive counterexamples run the other way. For **nitrosonium**, NO⁺, and
for **carbon monoxide**, the best contributor carries formal charges that rule 2
would call wrong — carbon negative and oxygen positive in CO — because the
alternative violates the octet, and rule 1 outranks rule 2. Carbon monoxide's
reactivity as a ligand follows directly from the lone pair on that
formally-negative carbon.

### When the octet fails

The octet rule is a strong guideline with three families of exception:

- **Radicals** have an odd electron count, so some atom has seven. Unit 5 is
  about these.
- **Electron-deficient species** — BH₃, BF₃, carbocations — have a central atom
  with only six. These are the electrophiles of unit 2.
- **Valence shell expansion** happens from the third row down, where d orbitals
  are accessible: PCl₅, SF₆, sulfate.

Second-row elements never exceed an octet. Carbon, nitrogen, oxygen and fluorine
have no accessible d orbitals, and a structure that gives them ten electrons is
simply wrong.

---

## Part 4 — orbitals

### Where the picture comes from

The Lewis picture is nineteenth-century. Everything after it comes from a
twenty-five-year run at the start of the twentieth:

- **Planck (1900) and Einstein (1905)** — energy is quantized; light comes in
  photons of energy $$E = h\nu$$.
- **de Broglie (1924)** — matter has a wavelength, $$\lambda = h/p$$. An
  electron confined to an atom is a standing wave.
- **Heisenberg (1927)** — position and momentum cannot both be known;
  $$\Delta x \, \Delta p \ge \hbar/2$$. There are no orbits.
- **Schrödinger (1926)** — the wave equation whose solutions $$\psi$$ are the
  orbitals. $$\lvert\psi\rvert^2$$ is the probability density.

An **orbital** is a one-electron wavefunction. It has a sign — positive in some
regions, negative in others — and that sign is not charge; it is the phase of a
wave, and it is what makes orbital overlap constructive or destructive. A
**node** is a surface where ψ = 0 and the electron is never found. More nodes
means higher energy.

### s and p

The **1s** orbital is spherical with no nodes. **2s** is spherical with one
radial node — a shell where ψ changes sign. The three **2p** orbitals are
dumbbells along x, y and z, each with one nodal *plane* through the nucleus, and
the two lobes have opposite sign.

Filling follows three rules: **Aufbau** (lowest energy first), **Pauli** (at
most two electrons per orbital, with opposite spins), and **Hund** (within a
degenerate set, spread out with parallel spins before pairing).

### Molecular orbitals

Atomic orbitals describe electrons on one atom. For a molecule you need
molecular orbitals, and the practical way to get them is the **linear
combination of atomic orbitals**: add and subtract the atomic orbitals you
started with. *N* atomic orbitals in gives *N* molecular orbitals out.

For two hydrogen atoms:

$$
\begin{aligned}
\psi_{+} &= \psi_{1s}(\mathrm{A}) + \psi_{1s}(\mathrm{B}) \\
\psi_{-} &= \psi_{1s}(\mathrm{A}) - \psi_{1s}(\mathrm{B})
\end{aligned}
$$

The sum is **bonding**: the two waves interfere constructively between the
nuclei, electron density piles up there, and the energy drops. The difference is
**antibonding**, written σ\*: the waves cancel, there is a node between the
nuclei, electron density is pushed to the outside, and the energy rises — by
slightly more than the bonding orbital fell.

![Molecular orbital diagram for H₂: two 1s atomic orbitals, one on each side, combining into a lower-energy bonding sigma orbital holding both electrons and a higher-energy empty antibonding sigma-star orbital](/assets/img/organic-chemistry-1/h2-mo-diagram.svg)

**Bond order** = ½(bonding electrons − antibonding electrons). Hydrogen has two
electrons, both in σ, so the bond order is 1 and H₂ exists. Helium would have
four, two in σ and two in σ\*, giving bond order 0 — and He₂ does not exist.
That is the whole explanation, and it is a better one than "helium has a full
shell", because it is quantitative.

### σ and π

The distinction is about the *symmetry* of the overlap, not the orbitals
involved.

- A **σ bond** is cylindrically symmetric about the internuclear axis. Rotate
  about the bond and nothing changes. End-on overlap — s with s, s with p, p
  with p head to head, or any hybrid with any hybrid.
- A **π bond** comes from side-on overlap of two parallel p orbitals. It has a
  nodal plane containing both nuclei, with density above and below. Rotating
  about the bond would have to break it.

That last clause is the reason double bonds do not rotate, which is the reason
cis/trans isomerism exists, which is chapter 5.

---

## Part 5 — hybridization

### The problem it solves

Carbon's ground-state configuration is 1s² 2s² 2p², which has only two unpaired
electrons. It should form two bonds at 90°. It forms four at 109.5°.

Hybridization is the bookkeeping fix: mix the 2s with some number of 2p orbitals
to make an equivalent set of new orbitals pointing where the bonds actually go.
Mixing *n* orbitals gives *n* hybrids, and the geometry follows from VSEPR
because the hybrids are just the electron groups.

- **sp** — one s plus one p, giving two hybrids. Linear, 180°, 50% s-character.
- **sp²** — one s plus two p, giving three hybrids. Trigonal planar, 120°,
  33% s-character.
- **sp³** — one s plus three p, giving four hybrids. Tetrahedral, 109.5°,
  25% s-character.

### The three worked cases

**BeH₂, sp.** Beryllium has two electron groups, so two hybrids at 180°, and one
unused p orbital in each of the two perpendicular directions. Linear.

**BH₃, sp².** Three groups, three hybrids at 120° in a plane, and one empty p
orbital perpendicular to it. That empty p orbital is why borane is a Lewis acid
— and it is worth noticing that BH₃ is **isoelectronic with the methyl cation**
CH₃⁺, which has exactly the same geometry and exactly the same empty p orbital.
Carbocations are not exotic; they are boranes with a different nucleus.

**CH₄, sp³.** Four groups, four hybrids pointing at the corners of a
tetrahedron, 109.5° apart.

Ammonia and water are sp³ too, with lone pairs occupying one and two of the
hybrids. The angles compress to 107.3° and 104.5° exactly as VSEPR predicts.

### Double and triple bonds

**Ethene, C₂H₄.** Each carbon has three electron groups, so each is sp². The
C–C σ bond is an sp²–sp² overlap; the four C–H bonds are sp²–1s. That leaves one
unhybridized p orbital on each carbon, perpendicular to the molecular plane, and
their side-on overlap is the π bond. The molecule is planar, with 120° angles,
and it cannot rotate about the double bond.

In molecular-orbital terms the two p orbitals give a filled π and an empty π\*.
That pair — the highest occupied and lowest unoccupied orbitals — is where
alkene chemistry happens, and it will reappear constantly.

**Ethyne, C₂H₂.** Two electron groups per carbon, so sp, linear, 180°. One
sp–sp σ bond, two sp–1s C–H bonds, and *two* perpendicular p orbitals on each
carbon giving *two* π bonds at right angles. The combined π density is a
cylinder around the C–C axis.

### Why s-character is worth tracking

An s orbital has density at the nucleus; a p orbital has a node there. So the
more s-character a hybrid has, the closer its electrons sit to the positively
charged nucleus, and the lower their energy.

Three consequences, all of which get used later:

- **Bonds get shorter and stronger** going sp³ → sp² → sp.
- **Carbon gets effectively more electronegative** going sp³ → sp² → sp, because
  it holds its electrons more tightly.
- **A lone pair in a high-s-character orbital is more stable and less
  available**, which makes the corresponding anion weaker as a base — the
  hybridization effect on acidity in [unit 2](/posts/organic-chemistry-1-structure-reactivity/).

### Drawing in three dimensions

The hashed-wedged line notation: a plain line in the plane of the page, a solid
wedge towards the reader, a hashed wedge away. For a tetrahedral carbon the
standard drawing is two plain lines, one wedge and one hash, with the two plain
bonds adjacent — which reads as a tetrahedron correctly and is the only
arrangement that does.

---

## Connections

- **Backward.** Everything here is general chemistry, reframed. The one genuinely
  new idea is reading a structure for its reactive sites rather than for its
  formula.
- **Forward.** Formal charge and resonance are the whole of acid–base theory in
  [unit 2](/posts/organic-chemistry-1-structure-reactivity/); the empty p orbital
  of BH₃ is the model for every electrophile; hybridization and s-character
  return as an acidity factor there and as the explanation of alkyne acidity in
  chapter 13. The planar sp² carbon with a singly occupied p orbital is the
  alkyl radical of [unit 5](/posts/organic-chemistry-1-radical-halogenation/).
- **Outward.** The LCAO picture scales directly to conjugated systems and
  aromaticity, and the π/π\* pair introduced for ethene becomes the HOMO–LUMO
  language of pericyclic reactions and of ultraviolet spectroscopy.

## Summary

- **Wöhler's urea synthesis (1828)** killed vitalism; organic compounds are just compounds
- **Two rules make every bond** — opposite charges attract, electrons prefer to delocalize
- **Ionic vs covalent** is a spectrum; most bonds are polar covalent with δ+/δ− ends
- **Electronegativity** C 2.5, N 3.0, O 3.4 — so C is δ+ to every heteroatom
- **VSEPR** counts all electron groups, lone pairs included, and lone pairs push harder
- **Formal charge** = valence − lone pair electrons − ½(bonding electrons)
- **Resonance** is one structure, not an equilibrium; it always lowers energy
- **Ranking contributors** — octets first, then charge on the right element, then fewest charges
- **Octet exceptions** — radicals, electron-deficient boron and carbocations, third row and below
- **Orbitals have phase**; nodes raise energy; bond order = ½(bonding − antibonding)
- **H₂ has bond order 1 and exists; He₂ has bond order 0 and does not**
- **σ is cylindrically symmetric, π has a nodal plane** — so π bonds forbid rotation
- **sp 180° / sp² 120° / sp³ 109.5°**, with 50 / 33 / 25 percent s-character
- **BH₃ is isoelectronic with CH₃⁺** — same geometry, same empty p orbital
- **More s-character** means shorter, stronger bonds and a less available lone pair

## References

- Peter C. Vollhardt & Neil E. Schore, *Organic Chemistry: Structure and Function*, 8th edition — chapter 1. Electronegativity values are Pauling's, as tabulated there.
- Organic Chemistry 1 (3343.205), Seoul National University, Spring 2023. Instructor: Seung Youn Hong (홍승윤). Lecture of 6 March 2023, "Week 02-1: Structure and Bonding", 48 slides.
- The vitalism narrative, the complexity timeline and the resonance-ranking counterexamples (enolate, formic acid, NO⁺, CO) are the lecturer's framing, expanded here.
- The molecular orbital figure is redrawn; the slide version is publisher artwork. Bond angles, bond orders and electronegativities are as given in the lecture.
- The remark that BH₃ is isoelectronic with CH₃⁺ is a handwritten annotation on the lecture slide, and is kept because it is the most useful sentence on that slide.
