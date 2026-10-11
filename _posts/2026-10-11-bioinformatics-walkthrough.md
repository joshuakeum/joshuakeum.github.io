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

### Operons and Polycistronic mRNAs

![A polycistronic operon. A stretch of DNA with two open reading frames is transcribed into one mRNA that has two protein-coding regions, each with its own ribosome-binding site, and the mRNA is translated into two proteins](/assets/img/bioinformatics-walkthrough/polycistronic-operon.png){: w="1920" h="946" }
_**Fig 1**. [Shafee & Lowe, <i>WikiJournal of Medicine</i>, **2017**](https://doi.org/10.15347/wjm/2017.002), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gene_structure_prokaryote_2_annotated.svg), CC BY 4.0_

- In prokaryotes, neighboring genes are often organized into **operons**. The
  genes of an operon are co-transcribed from one promoter into a single mRNA.
- Such an mRNA comprises several coding regions at once; it is
  **polycistronic** (**Fig 1**). Each open reading frame (ORF) is then
  translated from its own ribosome-binding site (RBS).

### Gene Clusters

![Panel A shows five genes on a line of DNA, bracketed as one gene cluster. The first three follow one promoter and give one mRNA, and the last two follow a second promoter and give another mRNA. Panel B compares two donor genomes. Where the genes A, B and C are adjacent, one transferred DNA segment carries all three into the recipient genome. Where they are far apart, a segment of the same length carries only B](/assets/img/bioinformatics-walkthrough/gene-clusters.svg){: w="720" h="486" }
_**Fig 2**. (A) A gene cluster that spans two operons. (B) Horizontal transfer of clustered genes and of scattered genes._

- It is common in microbial genomes for genes that cooperate with each other
  to sit in the same neighborhood. Such sets of nearby genes are called
  **gene clusters**.
- A gene cluster is not the same thing as an operon: a cluster may be a single
  operon, but it may also span several operons (**Fig 2A**).
- Two explanations are usually given for why cooperating genes cluster.
  - **Co-regulation**: genes in the same operon share one promoter, so they
    are switched on and off together.
  - **Horizontal gene transfer** (HGT): bacteria acquire DNA from other cells,
    and that DNA arrives as one continuous segment. Genes that sit next to
    each other are transferred together, so a whole cluster can move into a
    new genome and bring a complete function with it. Genes scattered across
    the genome would arrive one at a time, and each is of little use without
    the others (**Fig 2B**, [Lawrence & Roth, *Genetics*, **1996**](https://doi.org/10.1093/genetics/143.4.1843)).
- Genome mining needs only this premise: functionally linked genes sit close
  together, so the genomic context of a gene predicts its function
  ([Overbeek, Maltsev et al., *PNAS*, **1999**](https://doi.org/10.1073/pnas.96.6.2896)).

### Biosynthetic Gene Clusters

![Panel A shows the structures of five families of bacterial quorum-sensing signals. Panel B shows the agr locus of Paenibacillus, with the genes agrB, agrD, agrC, agrA and agrE drawn as arrows, and how the AgrD precursor peptide is processed into an autoinducing peptide that regulates antibiotic production](/assets/img/bioinformatics-walkthrough/agr-gene-cluster.jpg){: w="1650" h="1472" }
_**Fig 3**. [Chen, Li et al., <i>Sci. Adv.</i>, **2025**](https://doi.org/10.1126/sciadv.adw5076)_

- If the purpose of the gene clusters is the biosynthesis of metabolites, they
  are called **biosynthetic gene clusters** (BGCs, **Fig 3B**).
- Like other gene clusters, many BGCs span several operons.

---

## Brief Introduction to RiPPs

![A precursor peptide made of a leader domain and a core. PTMs modify the core, and proteolysis then removes the leader domain, leaving the modified core](/assets/img/bioinformatics-walkthrough/ripp-biosynthesis.jpg){: w="425" h="386" }
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
  enzyme cofactors ([Zhu & Klinman, *Curr. Opin. Chem. Biol.*, **2020**](https://pmc.ncbi.nlm.nih.gov/articles/PMC7736144/)),
  and more.

---

## PadeK Chemistry

### Lasso Peptide Biosynthesis

![Structures of three lasso peptides, the gene clusters that encode them, and a scheme in which the B and C enzymes cleave off the leader peptide and close the ring](/assets/img/bioinformatics-walkthrough/lasso-biosynthesis.jpg){: w="956" h="1280" }
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

![Lasso peptide gene clusters containing a kinase gene in four bacterial strains, an alignment of their precursor peptides, the map of the expression plasmid, and chromatograms showing the lasso peptide and its phosphorylated form](/assets/img/bioinformatics-walkthrough/padek.jpg){: w="1098" h="1280" }
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
