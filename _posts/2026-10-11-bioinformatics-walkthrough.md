---
title: "Bioinformatics Walkthrough"
date: 2026-10-11 13:00:00 +0900
categories: [Personal Projects]
tags: [bioinformatics, genome mining, RiPPs]
description: A walkthrough of a basic bioinformatic workflow, using PadeK as the example.
---

## Goal

> We aim to explore the biosynthetic repertoire of PadeK ([Zhu, Marahiel et al., *J. Biol. Chem.*, **2016**](https://doi.org/10.1074/jbc.M116.722108)) through genome mining and pangenomic analysis.
{: .prompt-tip }

---

## Biochemical Foundations of Microbial Genome Mining

### Transcription and Translation of Microbial mRNAs

#### Polysome Structures

![Line drawing of a strand of DNA with three mRNAs of increasing length coming off it. Each mRNA carries a row of ribosomes, and the longest is labelled as a polysome](/assets/img/bioinformatics-walkthrough/fig1-polysome.jpg){: w="704" h="304" }
_**Fig 1**. [Gonzalezmg1, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Final_polysome.jpg), CC BY-SA 4.0 (cropped)_

- Prokaryotes lack nuclei.
- Transcription and translation are coupled both spatially and temporally.
- **Polysomes** (**Fig 1**) form during prokaryotic translation: multiple
  ribosomes attach to a single mRNA strand that is still undergoing
  transcription.

#### Operons and Polycistronic mRNAs

![A polycistronic operon. A stretch of DNA with two open reading frames is transcribed into one mRNA that has two protein-coding regions, each with its own ribosome-binding site, and the mRNA is translated into two proteins](/assets/img/bioinformatics-walkthrough/fig2-polycistronic-operon.png){: w="1920" h="946" }
_**Fig 2**. [Shafee & Lowe, <i>WikiJournal of Medicine</i>, **2017**](https://doi.org/10.15347/wjm/2017.002), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gene_structure_prokaryote_2_annotated.svg), CC BY 4.0_

- Microbial genes are activated in **operons** that contain several genes at
  once. In other words, the transcription and translation of those genes take
  place simultaneously.
- Prokaryotic mRNAs comprise several coding regions at once; they are
  **polycistronic** (**Fig 2**).

#### Biosynthetic Gene Clusters

![Panel A shows the structures of five families of bacterial quorum-sensing signals. Panel B shows the agr locus of Paenibacillus, with the genes agrB, agrD, agrC, agrA and agrE drawn as arrows, and how the AgrD precursor peptide is processed into an autoinducing peptide that regulates antibiotic production](/assets/img/bioinformatics-walkthrough/fig3-agr-gene-cluster.jpg){: w="1650" h="1472" }
_**Fig 3**. [Chen, Li et al., <i>Sci. Adv.</i>, **2025**](https://doi.org/10.1126/sciadv.adw5076)_

- Due to polysomes and the polycistronic nature of prokaryotic gene
  expression, it is common in microbial genomes for genes that cooperate with
  each other to sit in the same neighborhood. Such sets of nearby genes are
  called **gene clusters**.
- If the purpose of the gene clusters is the biosynthesis of metabolites, they
  are called **biosynthetic gene clusters** (BGCs, **Fig 3B**).

---

## Brief Introduction to RiPPs

![A precursor peptide made of a leader domain and a core. PTMs modify the core, and proteolysis then removes the leader domain, leaving the modified core](/assets/img/bioinformatics-walkthrough/fig4-ripp-biosynthesis.jpg){: w="425" h="386" }
_**Fig 4**. Biosynthesis of RiPPs_

- **Ribosomally synthesized and post-translationally modified peptides**
  (RiPPs) are a large category of peptide natural products.
- RiPPs are produced by diverse post-translational modifications (PTMs) on the
  core of the ribosomal precursor peptide (**Fig 4**).
- Most precursors have an N-terminal leader (or occasionally a C-terminal
  follower) domain that the modification enzymes recognize through
  protein-protein interaction.
- The leader domain is usually cleaved by a peptidase after the modification
  (**Fig 4**).
- Such products have various biological functions, including microbial
  weaponry ([Li, Tao et al., *Nat. Comm.*, **2026**](https://www.nature.com/articles/s41467-026-70567-0)),
  quorum sensing ([Hirooka et al., *Biosci. Biotechnol. Biochem.*, **2020**](https://doi.org/10.1080/09168451.2019.1685371)),
  enzyme cofactors ([Moog, Dooley et al., *PNAS*, **1986**](https://doi.org/10.1073/pnas.83.22.8435)),
  and more.

---

## PadeK Chemistry

### Lasso Peptide Biosynthesis

![Structures of three lasso peptides, the gene clusters that encode them, and a scheme in which the B and C enzymes cleave off the leader peptide and close the ring](/assets/img/bioinformatics-walkthrough/fig5-lasso-biosynthesis.jpg){: w="956" h="1280" }
_**Fig 5**. [Zhu, Marahiel et al., <i>J. Biol. Chem.</i>, **2016**](https://doi.org/10.1074/jbc.M116.722108)_

- Lasso peptides are a class of RiPP products with a unique topology in which
  the C-terminus penetrates through a macrolactam ring formed between the core
  peptide's N-terminus and the D/E side chain.
- Either fused or split, the LasB protein consists of two domains: one RiPP
  recognition element that binds with the leader, and one peptidase with a
  transglutaminase fold. The LasB protein first cleaves the leader, and the
  new N-terminus constructs a macrolactam ring with the side chain via the Asn
  synthase-like LasC enzyme.

### PadeK, a Lasso Tailoring Kinase

![Lasso peptide gene clusters containing a kinase gene in four bacterial strains, an alignment of their precursor peptides, the map of the expression plasmid, and chromatograms showing the lasso peptide and its phosphorylated form](/assets/img/bioinformatics-walkthrough/fig6-padek.jpg){: w="1098" h="1280" }
_**Fig 6**. [Zhu, Marahiel et al., <i>J. Biol. Chem.</i>, **2016**](https://doi.org/10.1074/jbc.M116.722108)_

- [Zhu and Marahiel et al.](https://doi.org/10.1074/jbc.M116.722108) reported
  an HprK kinase homolog near a lasso peptide BGC, and concluded that its role
  is the (multi)-phosphorylation of the products.
- Here, let's expand the PadeK ([WP_006678397.1](https://www.ncbi.nlm.nih.gov/protein/WP_006678397.1))
  chemistry and search for novel combinations between PadeK and other RiPP
  enzymes.

---

## Homologous Protein Search

### Ideation

Now, we want to obtain PadeK homologues from the vast genome and protein
databases. There are several ways to achieve that goal. I intentionally
omitted the mathematical background behind them. Look for these keywords —
hidden Markov models, stochastic processes, and E-values.

### Methods

#### BLAST

#### Fetch from Databases

## Clustering and Classification of Homologous Proteins

### Ideation

### Methods

#### Multiple Sequence Alignment and Phylogenetic Trees

#### Sequence Similarity Networks

## Pangenomic Analysis
