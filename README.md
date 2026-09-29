# Astrobiology

Bioinformatics analyses exploring how life might survive in extreme environments.

## Rhodotorula frigidalcoholis Under Icy Moon Conditions

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

## Skills Used
Python (pandas, matplotlib, seaborn), BLAST, EnsemblFungi, NCBI, sequence translation, functional annotation
