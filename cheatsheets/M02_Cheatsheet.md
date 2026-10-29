# Module 2 Cheatsheet — File Handling & Biopython

### File I/O Basics
```python
from pathlib import Path

# Always use context managers (with)
with open("data/sequences/dna_sequences.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Process line
```

### Parsing FASTA by Hand
```python
def read_fasta(filepath):
    records = {}
    current_id = None
    seq_chunks = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    records[current_id] = "".join(seq_chunks)
                current_id = line[1:].split()[0]
                seq_chunks = []
            else:
                seq_chunks.append(line)
        if current_id:
            records[current_id] = "".join(seq_chunks)
    return records
```

### Biopython SeqIO Core Patterns
```python
from Bio import SeqIO
from Bio.Seq import Seq

# Single record vs Multiple records
single_rec = SeqIO.read("data/genbank/tp53_human.gb", "genbank")
multi_recs = list(SeqIO.parse("data/sequences/multi_sample.fasta", "fasta"))

# Extracting CDS features from GenBank
for feature in single_rec.features:
    if feature.type == "CDS":
        gene = feature.qualifiers.get("gene", ["unknown"])[0]
        translation = feature.qualifiers.get("translation", [""])[0]
        cds_seq = feature.extract(single_rec.seq)

# Format conversion
SeqIO.convert("data/genbank/tp53_human.gb", "genbank", "outputs/tp53.fasta", "fasta")
```

### Bio.SeqUtils
```python
from Bio.SeqUtils import gc_fraction, molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis

gc = gc_fraction("ATGC") * 100
mw = molecular_weight("ATGC", seq_type="DNA")

analyzed = ProteinAnalysis("MKWVTFISLLLLFSSAYSRG")
pi = analyzed.isoelectric_point()
instability = analyzed.instability_index()
```
