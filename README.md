# Astrobiology

Bioinformatics analyses exploring how life might survive in extreme environments.

## Rhodotorula frigidalcoholis Under Icy Moon Conditions

**Question:** How does this yeast survive simulated icy moon conditions (desiccation, radiation, UV)?

**Data:** RNA-seq differential expression data from Mendeley Data (doi: 10.17632/m65mc3vd5w.1)

## Analysis

I analyzed the differential expression data and generated a volcano plot comparing Control vs Exposed conditions. I then characterized the most extreme genes by extracting their sequences from EnsemblFungi, translating them to protein, and running BLASTp and InterPro.

## Key Findings

### Downregulated Gene (Conserving Energy)

**RHOSPDRAFT_33111 — F-box protein**
- Part of the cell's protein recycling system (tags proteins for destruction)
- Turned OFF during stress
- Likely conserves energy and preserves existing proteins

### Upregulated Genes (Active Survival Response)

**RHOSPDRAFT_27191 — DNA-binding transcription factor**
- Binds specific DNA sequences to control gene expression
- Likely the master regulator of the survival response
- Turns on other protective genes
- GO terms: regulation of DNA-templated transcription, DNA-binding transcription factor activity

**RHOSPDRAFT_14850 — Dihydroorotase**
- Enzyme in the pyrimidine biosynthesis pathway
- Makes the building blocks (C, T, U) for DNA and RNA
- Supplies nucleotides needed for DNA repair after radiation damage
- GO terms: pyrimidine nucleobase biosynthetic process, dihydroorotase activity

**RHOSPDRAFT_32292 — Intrinsically disordered protein (378 aa)**
- Highly upregulated during stress
- No structured domains (InterPro found no enzymatic or binding domains)
- Rich in serine, threonine, proline, and charged residues
- Predicted to be intrinsically disordered by MobiDB-lite
- Classified as low complexity, proline-rich, and polyampholytic
- Likely acts as a stress protectant or signaling hub rather than an enzyme
- Function remains uncharacterized — a genuine scientific gap

## Biological Story

The yeast survives icy moon conditions by:
1. Activating a master transcription factor (RHOSPDRAFT_27191)
2. Turning on DNA repair machinery (RHOSPDRAFT_14850 provides nucleotides)
3. Turning on other protective genes, including an intrinsically disordered protein (RHOSPDRAFT_32292)
4. Shutting down non-essential functions like protein recycling (RHOSPDRAFT_33111)

## Skills Used

Python (pandas, matplotlib, seaborn), BLAST, EnsemblFungi, NCBI, InterPro, sequence translation, functional annotation, GO term analysis

## Files

- `volcano_fixed.py` — Script to generate the volcano plot
- `volcano_plot.png` — Output figure
- `Data from Exploring the habitability of the outer/` — Source data from Mendeley
- `Rhodotorula_sp_jg_1b_gca_001541205.Rhosp1.cds.all.fa` — Genome coding sequences from EnsemblFungi
