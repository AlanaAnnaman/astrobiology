# Astrobiology: HSV-1 Latency and Icy Moon Survival

This repository contains bioinformatics analyses exploring how life might survive in extreme environments.

## Project 1: Rhodotorula frigidalcoholis Under Icy Moon Conditions

**Question:** How does this yeast survive simulated icy moon conditions (desiccation, radiation, UV)?

**Data:** RNA-seq differential expression data from Mendeley Data (doi: 10.17632/m65mc3vd5w.1)

**Analysis:**
- Volcano plot of Control vs Exposed conditions
- Identified top downregulated gene: RHOSPDRAFT_33111
- Extracted sequence from EnsemblFungi
- Translated to protein and ran BLASTp
- Found 77% identity to an F-box protein in *Rhodotorula pacifica*

**Key Finding:** The yeast shuts down an F-box protein (part of the protein recycling system) during stress, conserving energy for survival.

**Next Steps:** Investigate the most highly upregulated genes (RHOSPRAFT_27191, RHOSPRAFT_32292, RHOSPRAFT_14850) to understand the active survival response.

## Files
- `volcano_fixed.py`  Script to generate the volcano plot
- `volcano_plot.png`  Output figure
- `simple_volcano.py`  Initial exploratory script

## Skills Used
Python (pandas, matplotlib, seaborn), BLAST, EnsemblFungi, NCBI, sequence translation, functional annotation
