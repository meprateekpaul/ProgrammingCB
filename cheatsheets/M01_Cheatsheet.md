# Module 1 Cheatsheet — Python Basics for Biology

### Sequence Slicing & Manipulation
```python
seq = "ATGCGTACGTTA"

# Slicing: [start:stop:step] (0-based, half-open)
codon = seq[0:3]          # 'ATG'
reverse_seq = seq[::-1]   # 'ATTGCATGCGTA'
every_third = seq[::3]    # 'AGGT'

# Nucleotide Counts & GC Content
gc = (seq.count("G") + seq.count("C")) / len(seq) * 100

# Reverse Complement
trans = str.maketrans("ACGTacgt", "TGCAtgca")
rev_comp = seq.translate(trans)[::-1]

# Transcription (DNA -> RNA)
rna = seq.replace("T", "U")
```

### Translation & Codon Table
```python
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

def translate(dna):
    return "".join(CODON_TABLE.get(dna[i:i+3], "?") for i in range(0, len(dna)-2, 3))
```

### Exon / Intron Coordinate Rules
- Python indices are **0-based, half-open** `[start, end)`.
- If an exon is at 1-based coordinates `1..100`, in Python it is `seq[0:100]`.
- Canonical splice donor starts with `GT`, acceptor ends with `AG`.
