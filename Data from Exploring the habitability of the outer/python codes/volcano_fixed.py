import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel('/Volumes/T9/astro_analysis/Data from Exploring the habitability of the outer/primary_and_secondary_data/Control vs Exposed Differential Expression Analysis.xlsx')

# Rename the gene column
df = df.rename(columns={'Unnamed: 0': 'Gene_ID'})

# Filter out invalid padj values
df = df[df["padj"] > 0].copy()
df["neglog10_pval"] = -np.log10(df["padj"])
df["ranking_score"] = abs(df["log2FoldChange"]) * df["neglog10_pval"]

pvalue_cutoff = 0.05
log2FC_cutoff = 2

# Classify significance
df["significance"] = "Not Significant"
df.loc[(df["padj"] < pvalue_cutoff) & (df["log2FoldChange"] >= log2FC_cutoff), "significance"] = "Upregulated"
df.loc[(df["padj"] < pvalue_cutoff) & (df["log2FoldChange"] <= -log2FC_cutoff), "significance"] = "Downregulated"

# Top 5 up and down
top5_up = df[df["significance"] == "Upregulated"].nlargest(5, "ranking_score")
top5_down = df[df["significance"] == "Downregulated"].nlargest(5, "ranking_score")

# Plot
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x="log2FoldChange", y="neglog10_pval", hue="significance",
                palette={"Upregulated":"red", "Downregulated":"blue", "Not Significant":"grey"},
                alpha=0.7, edgecolor=None, s=15)

plt.axhline(-np.log10(pvalue_cutoff), color="black", linestyle="--", linewidth=0.8)
plt.axvline(-log2FC_cutoff, color="black", linestyle="--", linewidth=0.8)
plt.axvline(log2FC_cutoff, color="black", linestyle="--", linewidth=0.8)

# Label top genes
for _, row in top5_up.iterrows():
    plt.text(row["log2FoldChange"], row["neglog10_pval"], row["Gene_ID"], fontsize=9,
             ha="right", va="bottom", color="black")
for _, row in top5_down.iterrows():
    plt.text(row["log2FoldChange"], row["neglog10_pval"], row["Gene_ID"], fontsize=9,
             ha="right", va="bottom", color="black")

plt.xlabel("log2(Fold Change)", fontsize=12)
plt.ylabel("-log10(padj)")
plt.legend(title="Significance")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig('/Volumes/T9/astro_analysis/volcano_plot.png', dpi=150)
plt.show()