#!/usr/bin/env python3
"""
build_data.py
Build and download all required datasets for the ProgrammingCB course.
Run from repository root: python data/build_data.py
"""

import os
import sys
import random
import urllib.request
from pathlib import Path

# Fix random seed for reproducible synthetic data
random.seed(42)

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"

SEQ_DIR = DATA_DIR / "sequences"
GB_DIR = DATA_DIR / "genbank"
STRUCT_DIR = DATA_DIR / "structures"
TAB_DIR = DATA_DIR / "tables"
HTML_DIR = DATA_DIR / "html"

for d in [SEQ_DIR, GB_DIR, STRUCT_DIR, TAB_DIR, HTML_DIR]:
    d.mkdir(parents=True, exist_ok=True)

print("Building data in:", DATA_DIR)

# -------------------------------------------------------------
# 1. toy_gene_with_introns.txt & toy_exon_coordinates.tsv
# -------------------------------------------------------------
exon1 = "ATGGGACGCTACGTAGCCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGTAGCTA"  # 60 nt
intron1 = "GTAAGTGTCGATCGATCGTACTAGCTAGCTAGCTAGCATCGATCGATCGTACTAGCTAGCTAGCATCGATCGATCCTAG"  # 80 nt (starts GT, ends AG)
exon2 = "GCTAGCTAGCTACGATCGATCGTACTAGCTAGCTAGCTAGCATCGATCGATCGTACTAGCTAGCTAGCATCGATCGATCC"  # 81 nt
intron2 = "GTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACAG"  # 58 nt (starts GT, ends AG)
exon3 = "ATCGATCGATCGATCGATCGTACTAGCTAGCTAGCATCGATCGATCGTACTAGCTAGTAA"  # 60 nt (ends TAA)

gene_seq = exon1 + intron1 + exon2 + intron2 + exon3
assert intron1.startswith("GT") and intron1.endswith("AG")
assert intron2.startswith("GT") and intron2.endswith("AG")
assert gene_seq[:len(exon1)] == exon1
assert gene_seq[len(exon1) + len(intron1) : len(exon1) + len(intron1) + len(exon2)] == exon2

coord_exon1 = (0, len(exon1))
coord_exon2 = (coord_exon1[1] + len(intron1), coord_exon1[1] + len(intron1) + len(exon2))
coord_exon3 = (coord_exon2[1] + len(intron2), coord_exon2[1] + len(intron2) + len(exon3))

with open(SEQ_DIR / "toy_gene_with_introns.txt", "w") as f:
    f.write(gene_seq + "\n")

with open(TAB_DIR / "toy_exon_coordinates.tsv", "w") as f:
    f.write("exon_id\tstart\tend\tlength\n")
    f.write(f"exon_1\t{coord_exon1[0]}\t{coord_exon1[1]}\t{coord_exon1[1] - coord_exon1[0]}\n")
    f.write(f"exon_2\t{coord_exon2[0]}\t{coord_exon2[1]}\t{coord_exon2[1] - coord_exon2[0]}\n")
    f.write(f"exon_3\t{coord_exon3[0]}\t{coord_exon3[1]}\t{coord_exon3[1] - coord_exon3[0]}\n")

print("Created toy_gene_with_introns.txt and toy_exon_coordinates.tsv")

# -------------------------------------------------------------
# 2. dna_sequences.txt (copy from existing or create)
# -------------------------------------------------------------
old_dna = REPO_ROOT / "Notebooks" / "Exercises" / "Data" / "dna_sequences.txt"
if old_dna.exists():
    with open(old_dna) as fin, open(SEQ_DIR / "dna_sequences.txt", "w") as fout:
        fout.write(fin.read())
else:
    with open(SEQ_DIR / "dna_sequences.txt", "w") as f:
        for i in range(100):
            seq = "".join(random.choices("ACGT", k=random.randint(50, 150)))
            f.write(f"seq_{i+1}\t{seq}\n")

# -------------------------------------------------------------
# 3. multi_sample.fasta
# 15 records, mix of lengths (80-800) and GC (30%-70%),
# 1 with lowercase, 1 with N's
# -------------------------------------------------------------
fasta_records = []
bases_high_gc = "GGCC" + "ACGT"
bases_low_gc = "AATT" + "ACGT"

for i in range(1, 16):
    rec_id = f"sample_{i:02d}"
    organism = "Homo sapiens" if i <= 5 else ("Escherichia coli" if i <= 10 else "Saccharomyces cerevisiae")
    desc = f"{rec_id} putative transcript {organism}"
    length = random.randint(80, 450)
    
    if i == 3:
        # Lowercase sequence
        seq = "".join(random.choices("acgt", k=120))
    elif i == 7:
        # Sequence with ambiguous Ns
        core = "".join(random.choices("ACGT", k=100))
        seq = core[:40] + "NNNNN" + core[40:]
    elif i % 2 == 0:
        seq = "".join(random.choices(bases_high_gc, k=length))
    else:
        seq = "".join(random.choices(bases_low_gc, k=length))
    
    fasta_records.append((rec_id, desc, seq))

with open(SEQ_DIR / "multi_sample.fasta", "w") as f:
    for rec_id, desc, seq in fasta_records:
        f.write(f">{rec_id} {desc}\n")
        # Wrap at 60 chars
        for j in range(0, len(seq), 60):
            f.write(seq[j : j + 60] + "\n")

print("Created multi_sample.fasta (15 records)")

# -------------------------------------------------------------
# 4. reads_small.fastq
# 20 reads with varied quality
# -------------------------------------------------------------
with open(SEQ_DIR / "reads_small.fastq", "w") as f:
    for i in range(1, 21):
        read_id = f"@READ_{i:03d} length=50"
        seq = "".join(random.choices("ACGT", k=50))
        # Mix of high (I=40, J=41) and lower quality (!=0, #=2)
        if i % 4 == 0:
            quals = "".join(chr(random.randint(33 + 10, 33 + 25)) for _ in range(50))
        else:
            quals = "".join(chr(random.randint(33 + 28, 33 + 40)) for _ in range(50))
        f.write(f"{read_id}\n{seq}\n+\n{quals}\n")

print("Created reads_small.fastq (20 reads)")

# -------------------------------------------------------------
# 5. Fetch real biological records (NCBI & PDB)
# -------------------------------------------------------------
def download_url(url, dest_path):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "ProgrammingCB_Course/1.0 (prateekp@iiitd.ac.in)"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(dest_path, "wb") as f:
                f.write(content)
        print(f"Downloaded {dest_path.name} ({len(content)} bytes)")
        return True
    except Exception as e:
        print(f"Notice: download failed for {dest_path.name} from {url} ({e}). Generating fallback.")
        return False

# TP53 mRNA FASTA (NM_000546.6)
tp53_fasta = SEQ_DIR / "tp53_human_mrna.fasta"
if not tp53_fasta.exists():
    download_url(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_000546.6&rettype=fasta&retmode=text",
        tp53_fasta
    )

# TP53 GenBank (NM_000546.6)
tp53_gb = GB_DIR / "tp53_human.gb"
if not tp53_gb.exists():
    download_url(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_000546.6&rettype=gb&retmode=text",
        tp53_gb
    )

# E. coli lac operon GenBank (J01636.1)
lac_gb = GB_DIR / "ecoli_lac_operon.gb"
if not lac_gb.exists():
    download_url(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=J01636.1&rettype=gb&retmode=text",
        lac_gb
    )

# Human insulin protein GenPept (NP_000198.1)
insulin_gp = GB_DIR / "insulin_protein.gp"
if not insulin_gp.exists():
    download_url(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=NP_000198.1&rettype=gp&retmode=text",
        insulin_gp
    )

# PDB 1TUP (PDB and mmCIF)
p53_pdb = STRUCT_DIR / "1tup.pdb"
if not p53_pdb.exists():
    download_url("https://files.rcsb.org/download/1TUP.pdb", p53_pdb)

p53_cif = STRUCT_DIR / "1tup.cif"
if not p53_cif.exists():
    download_url("https://files.rcsb.org/download/1TUP.cif", p53_cif)

# -------------------------------------------------------------
# 6. Tabular data
# -------------------------------------------------------------
# A. genes_per_chromosome.csv (Human reference gene counts)
chr_counts = [
    ("chr1", 2058), ("chr2", 1309), ("chr3", 1078), ("chr4", 753),
    ("chr5", 876), ("chr6", 1048), ("chr7", 989), ("chr8", 706),
    ("chr9", 786), ("chr10", 733), ("chr11", 1298), ("chr12", 1034),
    ("chr13", 327), ("chr14", 621), ("chr15", 608), ("chr16", 873),
    ("chr17", 1197), ("chr18", 270), ("chr19", 1472), ("chr20", 544),
    ("chr21", 234), ("chr22", 488), ("chrX", 855), ("chrY", 71), ("chrM", 37)
]
with open(TAB_DIR / "genes_per_chromosome.csv", "w") as f:
    f.write("chromosome,gene_count\n")
    for ch, count in chr_counts:
        f.write(f"{ch},{count}\n")

# B. expression_tissues.csv (TPM values across tissues)
tissues = ["Brain", "Liver", "Heart", "Lung", "Kidney"]
genes_tissue_base = {
    "TP53": {"Brain": 15.2, "Liver": 18.4, "Heart": 12.1, "Lung": 22.0, "Kidney": 19.5},
    "INS": {"Brain": 0.1, "Liver": 1.2, "Heart": 0.05, "Lung": 0.1, "Kidney": 0.3},
    "HBB": {"Brain": 0.8, "Liver": 45.0, "Heart": 12.3, "Lung": 34.0, "Kidney": 8.5},
    "GAPDH": {"Brain": 150.0, "Liver": 180.0, "Heart": 165.0, "Lung": 172.0, "Kidney": 160.0},
    "ACTB": {"Brain": 210.0, "Liver": 195.0, "Heart": 230.0, "Lung": 205.0, "Kidney": 215.0}
}
with open(TAB_DIR / "expression_tissues.csv", "w") as f:
    f.write("gene,tissue,replicate,tpm\n")
    for gene, t_dict in genes_tissue_base.items():
        for tissue, base_tpm in t_dict.items():
            for rep in [1, 2, 3]:
                # Add slight replicate noise
                noise = random.uniform(0.9, 1.1)
                tpm = round(base_tpm * noise, 2)
                f.write(f"{gene},{tissue},rep_{rep},{tpm}\n")

# C. expression_matrix.csv (50 genes x 8 samples: Control_1..4, Treated_1..4)
gene_list = [f"GENE_{i:02d}" for i in range(1, 51)]
gene_list[0] = "TP53"
gene_list[1] = "BRCA1"
gene_list[2] = "EGFR"
gene_list[3] = "MYC"
gene_list[4] = "VEGFA"

samples = [f"Control_{i}" for i in range(1, 5)] + [f"Treated_{i}" for i in range(1, 5)]

with open(TAB_DIR / "expression_matrix.csv", "w") as f:
    f.write("gene," + ",".join(samples) + "\n")
    for g in gene_list:
        base = random.uniform(10, 500)
        # Treatment effect on some genes
        effect = random.choice([0.5, 1.0, 1.0, 1.0, 2.2, 3.5])
        ctrl_vals = [round(base * random.uniform(0.9, 1.1), 1) for _ in range(4)]
        trt_vals = [round(base * effect * random.uniform(0.9, 1.1), 1) for _ in range(4)]
        f.write(g + "," + ",".join(str(v) for v in (ctrl_vals + trt_vals)) + "\n")

# D. gene_annotation.csv (50 genes)
chrs = [f"chr{i}" for i in range(1, 23)] + ["chrX"]
biotypes = ["protein_coding"] * 45 + ["lncRNA"] * 5
with open(TAB_DIR / "gene_annotation.csv", "w") as f:
    f.write("gene,chromosome,start,end,strand,biotype\n")
    for i, g in enumerate(gene_list):
        chrom = chrs[i % len(chrs)]
        start = random.randint(100000, 50000000)
        length = random.randint(1500, 45000)
        end = start + length
        strand = random.choice(["+", "-"])
        btype = biotypes[i]
        f.write(f"{g},{chrom},{start},{end},{strand},{btype}\n")

# E. differential_expression.csv (volcano plot dataset)
with open(TAB_DIR / "differential_expression.csv", "w") as f:
    f.write("gene,baseMean,log2FoldChange,lfcSE,stat,pvalue,padj\n")
    for g in gene_list:
        base_m = round(random.uniform(50, 2000), 1)
        l2fc = round(random.gauss(0, 1.5), 2)
        lfc_se = round(random.uniform(0.1, 0.4), 2)
        stat = round(l2fc / lfc_se, 2)
        # Stronger p-value if large log2FC
        if abs(l2fc) > 1.8:
            pval = round(10 ** (-random.uniform(4, 9)), 6)
        else:
            pval = round(min(0.99, 10 ** (-random.uniform(0.1, 2.5))), 4)
        padj = min(1.0, round(pval * random.uniform(1.2, 3.0), 6))
        f.write(f"{g},{base_m},{l2fc},{lfc_se},{stat},{pval},{padj}\n")

print("Created all tabular datasets in data/tables/")

# -------------------------------------------------------------
# 7. Saved HTML pages for offline web scraping (data/html/)
# -------------------------------------------------------------
html_uniprot = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>UniProt - P04637 (P53_HUMAN)</title></head>
<body>
  <div id="entry-header">
    <h1 id="protein-name">Cellular tumor antigen p53</h1>
    <span class="gene-name">TP53</span>
    <span class="organism">Homo sapiens (Human)</span>
  </div>
  <div id="function-section">
    <h2>Function</h2>
    <p class="description">Acts as a tumor suppressor in many tumor types; induces growth arrest or apoptosis depending on the physiological circumstances and type of cell.</p>
  </div>
  <div id="features">
    <table class="features-table" id="domains">
      <thead><tr><th>Feature</th><th>Position</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td>Transactivation domain</td><td>1-61</td><td>TAD</td></tr>
        <tr><td>DNA-binding domain</td><td>102-292</td><td>DBD</td></tr>
        <tr><td>Tetramerization domain</td><td>325-356</td><td>Oligomerization</td></tr>
      </tbody>
    </table>
  </div>
</body>
</html>
"""
with open(HTML_DIR / "uniprot_sample.html", "w") as f:
    f.write(html_uniprot)

html_pubmed = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>PubMed Search Results - TP53</title></head>
<body>
  <div class="search-results">
    <article class="docsum-journal-citation" data-pmid="38123456">
      <a class="docsum-title" href="/38123456/">Mechanisms of p53 tumor suppression in modern oncology</a>
      <span class="docsum-authors">Paul P, Sharma R, Kumar A.</span>
      <span class="docsum-journal">Nat Rev Cancer. 2024;24(3):145-159.</span>
    </article>
    <article class="docsum-journal-citation" data-pmid="37987654">
      <a class="docsum-title" href="/37987654/">Targeting mutant TP53 for next-generation precision medicine</a>
      <span class="docsum-authors">Smith J, Doe A, Patel K.</span>
      <span class="docsum-journal">Cell. 2023;186(12):2580-2595.</span>
    </article>
    <article class="docsum-journal-citation" data-pmid="36543210">
      <a class="docsum-title" href="/36543210/">Integrative genomics of p53 pathway alterations in human cancer</a>
      <span class="docsum-authors">Chen L, Wang Y, Zhang X.</span>
      <span class="docsum-journal">Cancer Cell. 2023;41(5):890-905.</span>
    </article>
  </div>
</body>
</html>
"""
with open(HTML_DIR / "pubmed_sample.html", "w") as f:
    f.write(html_pubmed)

html_table = """<!DOCTYPE html>
<html>
<head><title>Biomarker Expression Table</title></head>
<body>
  <h2>Target Biomarkers</h2>
  <table border="1" id="biomarkers" class="data-table">
    <thead>
      <tr><th>Symbol</th><th>Name</th><th>Chromosome</th><th>Expression_FoldChange</th><th>P_Value</th></tr>
    </thead>
    <tbody>
      <tr><td>TP53</td><td>Tumor Protein P53</td><td>17</td><td>-2.45</td><td>0.00012</td></tr>
      <tr><td>BRCA1</td><td>Breast Cancer 1</td><td>17</td><td>-1.89</td><td>0.00150</td></tr>
      <tr><td>EGFR</td><td>Epidermal Growth Factor Receptor</td><td>7</td><td>3.12</td><td>0.00004</td></tr>
      <tr><td>MYC</td><td>MYC Proto-Oncogene</td><td>8</td><td>2.78</td><td>0.00030</td></tr>
      <tr><td>VEGFA</td><td>Vascular Endothelial Growth Factor A</td><td>6</td><td>1.95</td><td>0.00410</td></tr>
    </tbody>
  </table>
</body>
</html>
"""
with open(HTML_DIR / "table_sample.html", "w") as f:
    f.write(html_table)

print("Created HTML sample pages in data/html/")

# -------------------------------------------------------------
# 8. data/README.md (provenance)
# -------------------------------------------------------------
data_readme = """# Data Provenance and Descriptions

All datasets provided in this directory are curated for the **Programming for Computational Biology** course.

| File | Category | Origin / Provenance | Accession / Source | Notes |
|---|---|---|---|---|
| `sequences/toy_gene_with_introns.txt` | Sequence | Hand-crafted synthetic | — | 341 nt, 3 exons with canonical GT-AG splice junctions |
| `sequences/dna_sequences.txt` | Sequence | Synthetic | — | Collection of 100 random DNA sequences for I/O exercises |
| `sequences/multi_sample.fasta` | Sequence | Synthetic multi-FASTA | — | 15 records with varied length, GC%, lowercase, and ambiguous bases |
| `sequences/reads_small.fastq` | Sequence | Synthetic FASTQ | — | 20 Illumina-style 50bp reads with Phred+33 quality scores |
| `sequences/tp53_human_mrna.fasta` | Sequence | Real NCBI RefSeq | NM_000546.6 | Human TP53 transcript variant 1 mRNA |
| `genbank/tp53_human.gb` | GenBank | Real NCBI RefSeq | NM_000546.6 | Complete GenBank record with annotations and CDS features |
| `genbank/ecoli_lac_operon.gb` | GenBank | Real NCBI GenBank | J01636.1 | Complete E. coli lactose operon |
| `genbank/insulin_protein.gp` | GenPept | Real NCBI RefSeq | NP_000198.1 | Human insulin preproprotein GenPept record |
| `structures/1tup.pdb` | Structure | Real RCSB PDB | 1TUP | Crystal structure of p53 core domain bound to DNA |
| `structures/1tup.cif` | Structure | Real RCSB PDB | 1TUP | mmCIF formatted structural model |
| `tables/toy_exon_coordinates.tsv` | Table | Hand-crafted coordinates | — | 0-based half-open coordinates matching `toy_gene_with_introns.txt` |
| `tables/genes_per_chromosome.csv` | Table | Ensembl Human GRCh38 | — | Protein-coding gene counts per human chromosome |
| `tables/expression_tissues.csv` | Table | Simulated biological TPM | — | 5 genes × 5 human tissues × 3 replicates |
| `tables/expression_matrix.csv` | Table | Simulated RNA-seq matrix | — | 50 genes × 8 samples (Control 1..4, Treated 1..4) |
| `tables/gene_annotation.csv` | Table | Simulated gene metadata | — | Chromosome coordinates, strand, and biotype for 50 genes |
| `tables/differential_expression.csv` | Table | Simulated DESeq2 output | — | log2 fold changes, SE, p-values, padj for volcano plot |
| `html/uniprot_sample.html` | HTML | Offline scraping mock | P04637 | Mock UniProt entry for offline BeautifulSoup parsing |
| `html/pubmed_sample.html` | HTML | Offline scraping mock | PubMed | Mock PubMed citation list for offline scraping exercises |
| `html/table_sample.html` | HTML | Offline scraping mock | — | Clean HTML table for pandas read_html & scraping |

*To regenerate synthetic tables and download public records, run:*
```bash
python data/build_data.py
```
"""

with open(DATA_DIR / "README.md", "w") as f:
    f.write(data_readme)

print("Created data/README.md")
print("✅ Data build complete!")
