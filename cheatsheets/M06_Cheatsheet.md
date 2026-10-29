# Module 6 Cheatsheet — os, NumPy & pandas for Biology

### File System Automation (`os`, `pathlib`, `shutil`)
```python
import os, shutil
from pathlib import Path

# Walk directory tree
for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith(".fasta") or file.endswith(".fa"):
            full_path = os.path.join(root, file)
            print(full_path, os.path.getsize(full_path), "bytes")

# Pathlib paths
data_dir = Path("data")
for fasta_file in data_dir.glob("**/*.fasta"):
    print(fasta_file.name, fasta_file.stat().st_size)
```

### NumPy Scientific Computing
```python
import numpy as np

# DNA One-Hot Encoding (L x 4)
mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
seq = "ATGC"
one_hot = np.zeros((len(seq), 4), dtype=int)
for i, base in enumerate(seq):
    one_hot[i, mapping[base]] = 1

# Vectorised Log2 Fold Change
control_mean = np.mean(ctrl_matrix, axis=1)
treated_mean = np.mean(trt_matrix, axis=1)
log2_fc = np.log2((treated_mean + 1e-6) / (control_mean + 1e-6))
```

### Pandas Tabular Wrangling
```python
import pandas as pd

# Load expression matrix
df = pd.read_csv("data/tables/expression_matrix.csv")

# Filter highly expressed genes
high_exp = df[df.mean(numeric_only=True, axis=1) > 100]

# Tidy / Long-form transformation for Seaborn
tidy_df = df.melt(id_vars=["gene"], var_name="sample", value_name="expression")

# Merge with annotations
annot = pd.read_csv("data/tables/gene_annotation.csv")
merged = pd.merge(df, annot, on="gene")
grouped = merged.groupby("chromosome")["Control_1"].mean()
```
