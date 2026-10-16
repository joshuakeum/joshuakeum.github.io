---
title: "Bioinformatics Walkthrough"
date: 2026-10-11 13:00:00 +0900
categories: [Personal Projects]
tags: [bioinformatics, genome mining, RiPPs]
description: A walkthrough of a basic bioinformatic workflow, using PadeK as the example.
math: true
---

## Goal

> We aim to explore the biosynthetic repertoire of PadeK ([Zhu, Marahiel et al., *J. Biol. Chem.*, **2016**](https://doi.org/10.1074/jbc.M116.722108)) through genome mining and pangenomic analysis.
{: .prompt-tip }

---

## Biochemical Foundations of Microbial Genome Mining

### Operons and Polycistronic mRNAs

![A polycistronic operon. A stretch of DNA with two open reading frames is transcribed into one mRNA that has two protein-coding regions, each with its own ribosome-binding site, and the mRNA is translated into two proteins](/assets/img/bioinformatics-walkthrough/polycistronic-operon.png){: w="1920" h="946" }
_**Fig 1**. [Shafee & Lowe, <i>WikiJournal of Medicine</i>, **2017**](https://doi.org/10.15347/wjm/2017.002), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gene_structure_prokaryote_2_annotated.svg), CC BY 4.0_

- In prokaryotes, neighboring genes are often organized into **operons**. The genes of an operon are co-transcribed from one promoter into a single mRNA.
- Such an mRNA comprises several coding regions at once; it is **polycistronic** (**Fig 1**). Each open reading frame (ORF) is then translated from its own ribosome-binding site (RBS).

### Gene Clusters

![Panel A shows five genes on a line of DNA, bracketed as one gene cluster. The first three follow one promoter and give one mRNA, and the last two follow a second promoter and give another mRNA. Panel B compares two donor genomes. Where the genes X, Y and Z are adjacent, one transferred DNA segment carries all three into the recipient genome. Where they are far apart, a segment of the same length carries only Y](/assets/img/bioinformatics-walkthrough/gene-clusters.svg){: w="720" h="486" }
_**Fig 2**. (A) A gene cluster that spans two operons. (B) Horizontal transfer of clustered genes and of scattered genes._

- It is common in microbial genomes for genes that cooperate with each other to sit in the same neighborhood. Such sets of nearby genes are called **gene clusters**.
- A gene cluster is not the same thing as an operon: a cluster may be a single operon, but it may also span several operons (**Fig 2A**).
- Two explanations are usually given for why cooperating genes cluster.
  - **Co-regulation**: genes in the same operon share the same promoter, so they are switched on and off together. Several operons of one cluster are often controlled together by a regulator encoded in the cluster.
  - **Horizontal gene transfer** (HGT): bacteria acquire DNA from other cells, and that DNA arrives as one continuous segment. Genes that sit next to each other are transferred together, so a whole cluster can move into a new genome and bring a complete function with it. Genes scattered across the genome would arrive one at a time, and each is of little use without the others (**Fig 2B**, [Lawrence & Roth, *Genetics*, **1996**](https://doi.org/10.1093/genetics/143.4.1843)).
- Genome mining needs only this premise: functionally linked genes sit close together, so the genomic context of a gene predicts its function ([Overbeek, Maltsev et al., *PNAS*, **1999**](https://doi.org/10.1073/pnas.96.6.2896)).

### Biosynthetic Gene Clusters

![Panel A shows the structures of five families of bacterial quorum-sensing signals. Panel B shows the agr locus of Paenibacillus, with the genes agrB, agrD, agrC, agrA and agrE drawn as arrows, and how the AgrD precursor peptide is processed into an autoinducing peptide that regulates antibiotic production](/assets/img/bioinformatics-walkthrough/agr-gene-cluster.jpg){: w="1650" h="1472" }
_**Fig 3**. [Chen, Li et al., <i>Sci. Adv.</i>, **2025**](https://doi.org/10.1126/sciadv.adw5076)_

- Gene clusters that encode the biosynthesis of a specialized metabolite are called **biosynthetic gene clusters** (BGCs, **Fig 3B**).
- Like other gene clusters, many BGCs span several operons.

---

## Brief Introduction to RiPPs

![A precursor peptide made of a leader domain and a core. PTMs modify the core, and proteolysis then removes the leader domain, leaving the modified core](/assets/img/bioinformatics-walkthrough/ripp-biosynthesis.jpg){: w="425" h="386" }
_**Fig 4**. Biosynthesis of RiPPs_

- **Ribosomally synthesized and post-translationally modified peptides** (RiPPs) are a large category of peptide natural products.
- RiPPs are produced by diverse post-translational modifications (PTMs) on the core of the ribosomal precursor peptide (**Fig 4**).
- Most precursors have an N-terminal leader (or occasionally a C-terminal follower) peptide that the modification enzymes recognize through protein-protein interaction.
- The leader (or follower) peptide is usually cleaved by a peptidase after the modification (**Fig 4**).
- Also, some RiPP modification enzymes have a **RiPP recognition element** (RRE) domain, which interacts with the leader (or follower) peptide to “recognize” the precursor.
- Such products have various biological functions, including microbial weaponry ([Li, Tao et al., *Nat. Commun.*, **2026**](https://www.nature.com/articles/s41467-026-70567-0)), quorum sensing ([Hirooka et al., *Biosci. Biotechnol. Biochem.*, **2020**](https://doi.org/10.1080/09168451.2019.1685371)), enzyme cofactors ([Zhu & Klinman, *Curr. Opin. Chem. Biol.*, **2020**](https://pmc.ncbi.nlm.nih.gov/articles/PMC7736144/)), and more.

---

## PadeK Chemistry

### Lasso Peptide Biosynthesis

![Structures of three lasso peptides, the gene clusters that encode them, and a scheme in which the B and C enzymes cleave off the leader peptide and close the ring](/assets/img/bioinformatics-walkthrough/lasso-biosynthesis.jpg){: w="956" h="1280" }
_**Fig 5**. [Zhu, Marahiel et al., <i>J. Biol. Chem.</i>, **2016**](https://doi.org/10.1074/jbc.M116.722108)_

- Lasso peptides are a class of RiPP products with a unique topology in which the C-terminus is threaded through a macrolactam ring formed between the core peptide’s N-terminus and the D/E side chain at position 7, 8, or 9 of the core.
- The B function has two parts: an RRE (B1) that binds the leader, and a cysteine protease with a transglutaminase-like fold (B2). They are either fused in one protein or encoded separately. After B2 removes the leader, LasC, an asparagine synthetase-like enzyme, uses ATP to activate the Asp/Glu side chain, and the new N-terminal amine attacks it to close the ring.

### PadeK, a Lasso Tailoring Kinase

![Lasso peptide gene clusters containing a kinase gene in four bacterial strains, an alignment of their precursor peptides, the map of the expression plasmid, and chromatograms showing the lasso peptide and its phosphorylated form](/assets/img/bioinformatics-walkthrough/padek.jpg){: w="1098" h="1280" }
_**Fig 6**. [Zhu, Marahiel et al., <i>J. Biol. Chem.</i>, **2016**](https://doi.org/10.1074/jbc.M116.722108)_

- [Zhu et al.](https://doi.org/10.1074/jbc.M116.722108) reported an HprK kinase homolog inside the lasso peptide BGC, and concluded that its role is the (multi)-phosphorylation of the product, paeninodin.
- Here, let’s expand the PadeK ([WP_006678397.1](https://www.ncbi.nlm.nih.gov/protein/WP_006678397.1)) chemistry and search for novel combinations between PadeK and other RiPP enzymes.

---

## Homologous Protein Search

### Ideation

Now, we want to obtain PadeK homologues from the vast genome and protein databases. Here, I present the bottom-up sequence search methods (BLASTP and PSI-BLAST) that start from a single query protein and the top-down method (database fetch) that start from a large set of protein accessions.

### Methods

#### BLAST

- The **basic local alignment search tool (BLAST)** is a heuristic *local* alignment algorithm that compares nucleotide or protein sequences within a library or database. The user of the algorithm must provide a query nucleotide or protein sequence and BLAST returns sequences that resemble the query below a certain cutoff.
- BLAST for a protein query uses the BLOSUM62 matrix (or other established matrices), which gives, for every amino acid pair, the log-odds of the pair being aligned in related proteins versus being aligned by chance.
- Position-specific iterated BLAST (PSI-BLAST) changes its position matrix throughout the iterations, so that the matrix is calibrated for the query protein and its homologs.
- After each round, PSI-BLAST builds a position-specific scoring matrix (PSSM) from the hits that pass the inclusion threshold and searches again with it. The PSSM replaces BLOSUM62 with scores tuned to each position of PadeK and its homologs.

Note: The first iteration of PSI-BLAST uses the BLOSUM62 matrix.

##### Application to PadeK

![Line plot of the BLASTP hits of PadeK against the clustered nr database: 5,000 accessions ranked by pE, with a dashed line at pE 60. The top hit has E = 0 and sits in a band above pE 180, the reporting limit of NCBI BLAST. The curve then declines gently from about 100 to about 75 over the first 700 accessions, drops to about 40 by accession 1,000, and flattens into a long tail that ends near 14; 820 hits are at or above pE 60](/assets/img/bioinformatics-walkthrough/blastp-padek.png){: w="2400" h="1480" }
_**Fig 7**. BLASTP result of PadeK against the clustered\_nr database. In clustered\_nr, each hit stands for a cluster of near-identical sequences: 90% identity and 90% length is the clustering cutoff of this database._

- With PadeK’s protein sequence as the query, the BLASTP result shows a stair curve. The E-value, in this situation, shows the number of alignments scoring at least $$S$$ that one would expect by chance from a search of a certain size: $$E=kmne^{-\lambda S}$$, where $$S$$ is the alignment score, $$m$$ and $$n$$ are the query and database lengths, and $$k$$ and $$\lambda$$ depend on the scoring system.
  - Let’s define $$pE = −\log{E}$$ ($$\log$$ is the base-10 logarithm).
  - Because $$E$$ grows with database size, $$pE$$ values compare hits within one search, not across databases.
- Hits within one step may belong to the same subfamily, and a cliff may mark a subfamily boundary.
  - PadeK BLASTP shows a major cliff at rank ~820, where $$pE$$ falls from ~75 to ~45.

Note: It is not true that the accessions in the same step have the same enzyme chemistry or biochemical function. The third bullet considers the “possibility” of being similar, not the similarity itself.

![Two panels. Panel A is a line plot of four PSI-BLAST cycles of PadeK against the clustered nr database, each with 5,000 accessions ranked by pE, and a dashed line at the inclusion threshold, pE 60. Hits with E = 0 sit in a band above pE 180, the reporting limit of NCBI BLAST: 1 in cycle 0, 254 in cycle 1, 208 in cycle 2 and 179 in cycle 3. Cycle 0 is the BLASTP curve. In cycles 1 to 3 the curves fall from 180 to about 120, drop steeply near accession 850, and nearly coincide. Panel B shows heatmaps of the 1,259 accessions that reach pE 60 in at least one cycle, in four groups: 820 at or above 60 in every cycle, 246 below 60 only in cycle 0, 24 at or above 60 only in cycles 1 and 2, and 169 at or above 60 only in cycle 1. The upper heatmap gives pE in each cycle, with E = 0 hits counted as pE 180, and the lower one the change from the previous cycle: nearly every accession rises from cycle 0 to cycle 1, and later cycles change little](/assets/img/bioinformatics-walkthrough/psi-blast-padek.png){: w="2400" h="2718" }
_**Fig 8**. PSI-BLAST result of PadeK. (A) pE of the hits in each cycle, ranked; the dashed line is the inclusion threshold. (B) The 1,259 accessions with pE ≥ 60 in at least one cycle: pE in each cycle (top) and its change from the previous cycle (bottom)._

- One can control the E-value threshold for PSSM inclusion of the next iteration in PSI-BLAST.
- I recommend setting the threshold in between different steps, so that the step(s) of interest get included.
- The cliffs — the vertical gaps in the score distribution — are useful, as they likely represent subfamily boundaries of enzyme homologs.
- Also, iterate the process until the next accessions under the inclusion threshold are all in the previous iteration, or simply, until the accessions converge.
- Make sure that the query does not get lost during the iterations. If there are too many irrelevant protein sequences, the PSSM may be corrupted, and therefore the process may result in a distorted set of proteins.

#### Fetch from Databases

<https://www.ebi.ac.uk/interpro/entry/pfam/PF07475/>

- If you aim to efficiently obtain a larger scope of homologous proteins, it is possible to fetch enzyme accessions from databases.
- Conserved domain analysis suggested that the domain of PadeK is an HPrK-related kinase domain.

## Clustering and Classification of Homologous Proteins

### Ideation

### Methods

#### Multiple Sequence Alignment and Phylogenetic Trees

#### Sequence Similarity Networks

#### MMseqs2

## Pangenomic Analysis

## Further Analysis

### Domain Architecture Predictions

#### HHsuite

#### HMMER

### Structural Analysis

#### ML/DL-based Structure Prediction Tools

##### AlphaFold

##### RoseTTAFold

##### ESMFold

#### Structure-based Search Tools

##### FoldSeek

##### Folddisco

#### Molecular Visualization Tools

##### PyMOL

##### ChimeraX

#### Structural Feature Prediction Tools

##### DeepTMHMM
