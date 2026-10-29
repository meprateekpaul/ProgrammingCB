# Module 4 Cheatsheet — Data Visualisation

### Chart Choice Matrix
| Biological Question | Recommended Plot | Matplotlib / Seaborn |
|---|---|---|
| Categorical comparisons (e.g. gene counts/chr) | Bar chart | `ax.bar(x, y)` / `sns.barplot(data, x, y)` |
| 1D continuous distribution (lengths, GC%) | Histogram + KDE | `ax.hist(vals, bins=30)` / `sns.histplot(vals, kde=True)` |
| Composition of parts (bases, variant types) | Pie / Donut | `ax.pie(vals, labels=labels, autopct='%1.1f%%')` |
| Distribution across groups with outliers | Box plot | `ax.boxplot(data)` / `sns.boxplot(data, x, y)` |
| Multimodal distribution shape per condition | Violin plot | `ax.violinplot(data)` / `sns.violinplot(data, x, y)` |
| Expression matrix / Gene correlation | Heatmap | `ax.imshow(mat)` / `sns.heatmap(df, annot=True)` |
| 2-variable relation / Volcano plot | Scatter plot | `ax.scatter(fc, pval)` / `sns.scatterplot(df, x, y)` |

### Matplotlib Object-Oriented Boilerplate
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(categories, values, color="#3498db", edgecolor="black")
ax.set_title("Gene Distribution across Chromosomes", fontsize=14, fontweight="bold")
ax.set_xlabel("Chromosome", fontsize=12)
ax.set_ylabel("Gene Count", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.6)

# Annotation with arrow
ax.annotate(
    "Highest: Chr 1",
    xy=(0, 2058), xytext=(2, 2200),
    arrowprops=dict(facecolor="black", arrowstyle="->")
)

fig.savefig("outputs/figure.png", dpi=300, bbox_inches="tight")
plt.close(fig)
```

### Seaborn Theming & Colorblind Palettes
```python
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.1)
palette = sns.color_palette("colorblind")  # Accessible

# Clustered heatmap
g = sns.clustermap(expression_df, cmap="viridis", z_score=0, figsize=(10, 8))
```
