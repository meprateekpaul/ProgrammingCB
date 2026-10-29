# Programming for Computational Biology (PCB) — Python
### Course Blueprint, Repository Restructure & Notebook Authoring Guide

> **Repository:** `meprateekpaul/ProgrammingCB`
> **Purpose of this file:** the single source of truth for what the course contains, how the repo is laid out, and exactly what every notebook must include. Put it in the repo root as `COURSE_PLAN.md` and tick items off as notebooks are built.

---

## Table of Contents

1. [Audit of the current repository](#1-audit-of-the-current-repository)
2. [Course at a glance](#2-course-at-a-glance)
3. [Target repository structure](#3-target-repository-structure)
4. [Standard notebook template](#4-standard-notebook-template)
5. [Module-by-module content plan](#5-module-by-module-content-plan)
   - [Module 0 — Setup & Orientation](#module-0--setup--orientation)
   - [Module 1 — Basics of Python](#module-1--basics-of-python)
   - [Module 2 — File Handling & Biopython](#module-2--file-handling--biopython)
   - [Module 3 — Object-Oriented Programming](#module-3--object-oriented-programming)
   - [Module 4 — Data Visualisation](#module-4--data-visualisation)
   - [Module 5 — Databases & Web Scraping](#module-5--accessing-and-querying-databases--web-scraping)
   - [Module 6 — os, NumPy & pandas (Assignment)](#module-6--os-numpy--pandas-assignment)
   - [Capstone (optional)](#capstone-optional)
6. [Data files to create](#6-data-files-to-create)
7. [Assessment plan](#7-assessment-plan)
8. [Suggested teaching schedule](#8-suggested-teaching-schedule)
9. [Authoring workflow & quality checklist](#9-authoring-workflow--quality-checklist)
10. [Migration plan (old → new)](#10-migration-plan-old--new)
11. [References](#11-references)

---

## 1. Audit of the current repository

### What exists today

| File | Content | Maps to syllabus | Solutions? |
|---|---|---|---|
| `Tutorial_1_BioComputing_Basics` | ~70 short Qs: strings, lists, dicts, loops, conditionals, GC, translation, exons | Module 1 | ✅ |
| `Tutorial_2_Sequence_Alignment` | Scoring, Hamming, NW/SW matrix filling | Enrichment (not in syllabus) | ✅ |
| `Tutorial_3_BioComputing_Intermediate` | 10 problems: motifs, Tm, k-mers, ORFs | Module 1 | ✅ |
| `Tutorial_4_FASTA_FASTQ` | 3 Qs: FASTA parser, Phred | Module 2 | ✅ |
| `Tutorial_5_Biological_Databases` | GenBank, UniProt, PDB, Entrez, KEGG | Module 5 | ❌ |
| `Tutorial_6_FileHandling_Part1` | read/write/append, FASTA by hand, ORFs | Module 2 | ❌ |
| `Tutorial_7_FileHandling_Part2` | SeqIO, GenBank, features, SeqUtils, convert | Module 2 | ❌ |
| `Tutorial_8_OOPs` | Classes, encapsulation, inheritance, polymorphism, 20 Qs | Module 3 | ❌ |
| `Tutorial_9_DataVisualization` | Plot-type catalogue by biology field, bar/scatter/box/heatmap/violin | Module 4 | ❌ |
| `Tutorial_10_BiologicalDB` | Near-duplicate of Tutorial 5 | Module 5 | ❌ |
| `Tutorial_11_WebScraping` | String parsing, HTML parser, MechanicalSoup, 10 bio tasks | Module 5 | ❌ |

### Gaps and problems to fix

| # | Issue | Fix |
|---|---|---|
| 1 | **Tutorials 5 and 10 are near-duplicates** | Merge into one Module 5A/5B notebook pair |
| 2 | **Duplicate notebooks inside `Exercises/Data/`** (`Class1_FileHandelingPart1/2.ipynb`, copies of T6/T7) | Delete; `data/` should hold data only |
| 3 | **Generated outputs committed** (`output.fasta`, `output.gb`, `modified_output.fasta`, `new_file.txt`, …) | Remove; write outputs to `outputs/` which is git-ignored |
| 4 | **Solutions missing for T5–T11** | Create one solution notebook per exercise notebook |
| 5 | **Access modifiers (public / _protected / __private) not covered** | Add explicit section in Module 3B |
| 6 | **Abstraction via `abc.ABC` / `@abstractmethod` not covered** | Add to Module 3B |
| 7 | **Histogram and pie chart only lightly covered; no Seaborn-vs-Matplotlib comparison** | Module 4 restructure |
| 8 | **No API-key / NCBI rate-limit / `time.sleep` content** | Module 5C "Best practices" notebook |
| 9 | **UniProt: no modern REST API (`rest.uniprot.org`) usage** | Add in Module 5B |
| 10 | **Web scraping: ethics/legal only touched; no `requests` + `BeautifulSoup` core flow** | Rewrite Module 5D around Requests + BS4; keep MechanicalSoup as optional |
| 11 | **`os`, NumPy, pandas module not present** | New Module 6 assignment notebook |
| 12 | **No environment file** (`requirements.txt`/`environment.yml`) | Add both |
| 13 | **Inconsistent naming** (`Tutorial_n_...`, `Class1_FileHandeling...` typo) | Adopt the naming convention in §3 |
| 14 | Alignment (T2) isn't in the syllabus | Keep as **Module 1 Enrichment** (optional) |

---

## 2. Course at a glance

| Module | Title | Notebooks | Est. hours (lecture + lab) | Assessed by |
|---|---|---|---|---|
| 0 | Setup & Orientation | 1 | 1 | — |
| 1 | Basics of Python | 4 (+1 enrichment) | 8 | Quiz 1, Lab 1 |
| 2 | File Handling & Biopython | 3 | 6 | Lab 2 |
| 3 | Object-Oriented Programming | 3 | 5 | Quiz 2, Lab 3 |
| 4 | Data Visualisation | 3 | 5 | Lab 4 |
| 5 | Databases & Web Scraping | 5 | 8 | Lab 5, Homework (scraping) |
| 6 | os, NumPy & pandas | 1 (assignment) | self-study ~6 | Assignment |
| — | Capstone (optional) | 1 | self-study | Project |

**Learning path:**
`M0 → M1 → M2 → M3 → M4 → M5 → M6 (parallel with M4/M5) → Capstone`

**Running biological thread:** use the same small set of real genes throughout the course (e.g. human **TP53**, **INS**, **HBB**, and *E. coli* **lacZ**). Students see the same gene as a string (M1), a FASTA/GenBank file (M2), a `Gene` object (M3), a plot (M4), and a database record (M5). This continuity is the single biggest thing that makes the course feel coherent.

---

## 3. Target repository structure

```
ProgrammingCB/
├── README.md                     # Landing page: course overview, how to start, module links, Colab badges
├── COURSE_PLAN.md                # This file
├── SYLLABUS.md                   # Student-facing syllabus (short version of §2 + §5)
├── LICENSE
├── requirements.txt              # pip install -r requirements.txt
├── environment.yml               # conda env create -f environment.yml
├── .gitignore                    # ignores outputs/, .ipynb_checkpoints/, __pycache__/, .env
│
├── data/                         # READ-ONLY input data, shared across modules
│   ├── README.md                 # Provenance of every file (source, accession, date fetched)
│   ├── sequences/                # *.fasta, *.fa, *.txt
│   ├── genbank/                  # *.gb, *.gp
│   ├── structures/               # *.pdb, *.cif
│   ├── tables/                   # *.csv, *.tsv (expression, metadata)
│   └── html/                     # Saved HTML pages for offline scraping practice
│
├── modules/
│   ├── M00_Setup/
│   │   └── M00_Setup_and_Orientation.ipynb
│   ├── M01_Python_Basics/
│   │   ├── M01A_Core_Python.ipynb
│   │   ├── M01B_Sequence_Manipulation.ipynb
│   │   ├── M01C_ORFs_Exons_Introns.ipynb
│   │   ├── M01D_Practice_Problems.ipynb
│   │   ├── M01E_Enrichment_Sequence_Alignment.ipynb
│   │   └── solutions/
│   │       └── M01A_Core_Python_Solutions.ipynb … (one per notebook)
│   ├── M02_File_Handling/
│   │   ├── M02A_Text_Files.ipynb
│   │   ├── M02B_FASTA_by_Hand.ipynb
│   │   ├── M02C_Biopython_SeqIO_GenBank.ipynb
│   │   └── solutions/
│   ├── M03_OOP/
│   │   ├── M03A_Classes_and_Objects.ipynb
│   │   ├── M03B_Four_Pillars_and_Access_Modifiers.ipynb
│   │   ├── M03C_OOP_Practice_and_Mini_Project.ipynb
│   │   └── solutions/
│   ├── M04_Visualisation/
│   │   ├── M04A_Biological_Plots_Theory.ipynb
│   │   ├── M04B_Matplotlib.ipynb
│   │   ├── M04C_Seaborn_and_Styling.ipynb
│   │   └── solutions/
│   ├── M05_Databases_and_Scraping/
│   │   ├── M05A_Entrez_GenBank_PubMed.ipynb
│   │   ├── M05B_UniProt_PDB_KEGG.ipynb
│   │   ├── M05C_Best_Practices_API_Keys.ipynb
│   │   ├── M05D_Web_Scraping_Fundamentals.ipynb
│   │   ├── M05E_Web_Scraping_Homework.ipynb
│   │   └── solutions/
│   ├── M06_os_NumPy_pandas/
│   │   ├── M06_Assignment.ipynb
│   │   └── solutions/
│   └── Capstone/
│       └── Capstone_Gene_Report_Pipeline.ipynb
│
├── assessments/
│   ├── quizzes/                  # Quiz_1.md, Quiz_2.md (MCQ + short code reading)
│   └── rubrics/                  # Rubric_Lab.md, Rubric_Homework.md, Rubric_Capstone.md
│
├── cheatsheets/                  # 1-page markdown/PDF per module (mirrors SummarySheet)
│
├── outputs/                      # git-ignored; every notebook writes here
│
└── .github/workflows/
    └── test-notebooks.yml        # Executes all SOLUTION notebooks on each push (see §9)
```

### Naming conventions

| Thing | Convention | Example |
|---|---|---|
| Module folder | `M<2-digit>_<Title>` | `M02_File_Handling` |
| Notebook | `M<2-digit><Letter>_<Topic>.ipynb` | `M02C_Biopython_SeqIO_GenBank.ipynb` |
| Solution | same name + `_Solutions` inside `solutions/` | `solutions/M02C_Biopython_SeqIO_GenBank_Solutions.ipynb` |
| Exercise IDs | `<Module><Letter>.<n>` | `Ex 2C.4` |
| Data files | lowercase, underscores, include organism/gene | `tp53_human_mrna.fasta` |
| Outputs | written to `../../outputs/<notebook_id>/` | `outputs/M02C/lacz_protein.fasta` |

### `requirements.txt`

```text
python>=3.10
jupyterlab
biopython>=1.83
numpy
pandas
matplotlib
seaborn
requests
beautifulsoup4
lxml
mechanicalsoup      # optional, Module 5D appendix
python-dotenv       # loading NCBI API key from .env
nbval               # CI testing of notebooks
```

### `.gitignore` additions

```text
outputs/
.ipynb_checkpoints/
__pycache__/
.env
*.pyc
```

---

## 4. Standard notebook template

**Every** exercise notebook follows the same skeleton. Students learn the layout once and then concentrate on content.

```
┌─────────────────────────────────────────────────────────────┐
│ 0. HEADER (markdown)                                        │
│    Title · Module · Author · Last updated · Colab badge     │
│    Estimated time · Difficulty (★☆☆ / ★★☆ / ★★★)            │
├─────────────────────────────────────────────────────────────┤
│ 1. LEARNING OUTCOMES (markdown)                             │
│    "By the end of this notebook you will be able to…"       │
│    3–6 measurable verbs: write, parse, explain, plot…       │
├─────────────────────────────────────────────────────────────┤
│ 2. PREREQUISITES (markdown)                                 │
│    Notebooks to finish first; concepts assumed              │
├─────────────────────────────────────────────────────────────┤
│ 3. SETUP (code)                                             │
│    Imports · paths (DATA_DIR, OUT_DIR) · version print      │
│    Colab detection + pip install if needed                  │
├─────────────────────────────────────────────────────────────┤
│ 4. CONCEPT SECTIONS  ×N                                     │
│    4.x.1 Theory (markdown, short, with a biology hook)      │
│    4.x.2 Worked example (code, fully commented)             │
│    4.x.3 ✏️ Try it (1 small exercise + assert check)         │
│    4.x.4 ⚠️ Common mistakes (markdown bullet list)           │
├─────────────────────────────────────────────────────────────┤
│ 5. PRACTICE EXERCISES                                       │
│    Level 1 (★)  — direct application                         │
│    Level 2 (★★) — combine 2–3 concepts                       │
│    Level 3 (★★★)— open-ended, real data                      │
│    Each: problem · input · expected output · TODO cell ·     │
│          test cell (assert)                                  │
├─────────────────────────────────────────────────────────────┤
│ 6. MINI-PROJECT / CHALLENGE (optional)                      │
├─────────────────────────────────────────────────────────────┤
│ 7. SUMMARY + CHEAT-SHEET TABLE                              │
├─────────────────────────────────────────────────────────────┤
│ 8. FURTHER READING (links: Real Python, Biopython Tutorial) │
└─────────────────────────────────────────────────────────────┘
```

### Header cell (copy-paste)

```markdown
# M02C · Biopython: SeqIO, GenBank & SeqUtils
**Programming for Computational Biology (Python)** · Author: Prateek Paul · Last updated: YYYY-MM-DD

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M02_File_Handling/M02C_Biopython_SeqIO_GenBank.ipynb)

⏱ ~90 min · Difficulty: ★★☆ · Prerequisites: M02A, M02B
```

### Setup cell (copy-paste)

```python
# --- Setup -------------------------------------------------------
import sys, os
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    !pip -q install biopython seaborn
    !git clone -q https://github.com/meprateekpaul/ProgrammingCB.git
    ROOT = Path("ProgrammingCB")
else:
    ROOT = Path.cwd().parents[1]          # modules/MXX_*/ -> repo root

DATA_DIR = ROOT / "data"
OUT_DIR  = ROOT / "outputs" / "M02C"      # <-- change per notebook
OUT_DIR.mkdir(parents=True, exist_ok=True)

import Bio
print("Python", sys.version.split()[0], "| Biopython", Bio.__version__)
```

### Exercise cell pattern (exercise notebook)

```python
# Ex 1B.3 — GC content
# Write gc_content(seq) returning GC % rounded to 2 decimals.
# Input : "ATGCGTACGTT"   Expected: 45.45

def gc_content(seq: str) -> float:
    # TODO: your code here
    ...
```

```python
# ✅ Test — run me. No output means you passed.
assert gc_content("ATGCGTACGTT") == 45.45
assert gc_content("gggccc") == 100.0, "Hint: handle lowercase"
assert gc_content("") == 0.0, "Hint: handle empty strings"
print("Ex 1B.3 passed ✔")
```

The solution notebook is identical but with the `TODO` replaced by the reference answer **and** an explanation markdown cell after it (why this approach, complexity, alternative one-liner).

---

## 5. Module-by-module content plan

Notation: 🔁 = reuse/refactor existing notebook · 🆕 = new content to write · 📦 = data file needed (see §6)

---

### Module 0 — Setup & Orientation

**Notebook:** `M00_Setup_and_Orientation.ipynb` 🆕 · ~45 min

| Section | Content |
|---|---|
| 0.1 Why programming for biology? | Scale of data (genome sizes, SRA growth), reproducibility, automation |
| 0.2 Environment | Local (Anaconda / venv) vs Google Colab; `requirements.txt`; verify installs |
| 0.3 Jupyter essentials | Cells, kernel restart, `?`/`help()`, magic commands `%timeit`, `%%writefile` |
| 0.4 Repo tour | How to clone, where data lives, how to run tests, how to submit |
| 0.5 Git in 10 minutes (optional) | `clone`, `pull`, forking for submissions |
| ✏️ Check | Run a cell that imports every library and prints versions |

---

### Module 1 — Basics of Python

**Syllabus coverage:** Python basics, Strings, Lists, Dictionaries, Loops, Conditional statements, Sequence manipulations (reverse complement, translation, GC content), string slicing, Filtering sequences, ORF extraction, Exon and intron extraction, string-based calculations.

#### M01A · Core Python 🔁 (from T1, first half) · ~2 h

| Section | Topics | Biology example |
|---|---|---|
| 1A.1 Variables & types | int, float, str, bool, `type()`, casting | Store sequence length, Tm, is_coding flag |
| 1A.2 Operators | Arithmetic, comparison, logical, membership (`in`) | `"ATG" in seq` |
| 1A.3 Strings | Indexing, **slicing** (`[start:stop:step]`), methods (`upper`, `count`, `find`, `replace`, `split`, `join`), f-strings | Codon at position i; reverse with `[::-1]` |
| 1A.4 Lists | Create, index, slice, append/extend/insert/remove, sort, list comprehension | List of codons; list of reads |
| 1A.5 Tuples & sets | Immutability; set ops (union, intersection, difference) | Unique k-mers; shared motifs between two seqs |
| 1A.6 Dictionaries | Keys/values, `.get()`, `.items()`, dict comprehension, nested dicts | Codon table; nucleotide counts |
| 1A.7 Conditionals | `if/elif/else`, nested, ternary | Purine vs pyrimidine; valid base check |
| 1A.8 Loops | `for`, `while`, `range`, `enumerate`, `zip`, `break/continue` | Walk a sequence by codons |
| 1A.9 Functions | `def`, parameters, defaults, return, docstrings, scope | `count_bases(seq)` |
| ⚠️ Common mistakes | Off-by-one in slicing, mutating list while iterating, `=` vs `==` | |

Practice: 15 exercises (5 ★, 6 ★★, 4 ★★★) — reuse best ones from T1 Q1–Q30.

#### M01B · Sequence Manipulation 🔁 (T1 second half + T3) · ~2 h

| Section | Must include | Function students write |
|---|---|---|
| 1B.1 Validation | Allowed alphabet, case handling | `is_valid_dna(seq)` |
| 1B.2 Composition | Base counts, **GC content**, AT/GC skew | `gc_content(seq)`, `gc_skew(seq)` |
| 1B.3 Complement & **reverse complement** | Dict mapping, `str.maketrans`, slicing | `reverse_complement(seq)` |
| 1B.4 Transcription | DNA→RNA | `transcribe(seq)` |
| 1B.5 **Translation** | Codon table dict, reading frames, stop handling | `translate(seq, frame=0)` |
| 1B.6 **String-based calculations** | Molecular weight, Tm (Wallace rule; GC-based for >13 nt), Hamming distance | `tm_wallace(seq)`, `mol_weight(seq)` |
| 1B.7 Motifs & k-mers | `find` loop, overlapping vs non-overlapping, k-mer frequency dict | `find_motif(seq, motif)`, `kmer_count(seq, k)` |
| 1B.8 **Filtering sequences** | List comprehension + conditions on length, GC, motif presence | `filter_seqs(seqs, min_len, min_gc)` |

#### M01C · ORFs, Exons & Introns 🔁/🆕 · ~1.5 h

| Section | Content |
|---|---|
| 1C.1 Gene structure refresher | Diagram: promoter → 5′UTR → exon/intron → 3′UTR; GT-AG rule |
| 1C.2 **ORF extraction** | Single frame → 3 forward frames → 6 frames (using reverse complement); min length filter; nested ORFs |
| 1C.3 **Exon extraction** | Given coordinate list `[(start, end), …]`, slice and join → mRNA/CDS |
| 1C.4 **Intron extraction** | Gaps between consecutive exons; validate GT…AG; compute intron lengths |
| 1C.5 0-based vs 1-based coordinates | Python vs GenBank/GFF conventions — the #1 source of bugs |
| ★★★ Challenge | Given a gene + exon coordinates: output CDS, protein, intron list, and check every intron starts GT / ends AG |

📦 `data/sequences/toy_gene_with_introns.txt`, `data/tables/toy_exon_coordinates.tsv`

#### M01D · Practice Problems 🔁 (T3 Q1–Q10 + T1 leftovers) · lab session

Pure problem set, no new theory. Order by difficulty. Include the existing enzyme-motif classifier, Tm, k-mer, ORF and consensus problems.

#### M01E · Enrichment: Sequence Alignment 🔁 (T2) · optional

Keep as-is; label clearly "Optional / not examined". Add a final cell comparing your NW score with `Bio.Align.PairwiseAligner` (forward-link to Module 2).

---

### Module 2 — File Handling & Biopython

**Syllabus coverage:** Reading text files (read, readlines, for loop), Writing and appending, FASTA reading/writing/splitting; BioPython, Bio, SeqIO, FASTA, GenBank, MultiFasta, Extracting Features from GenBank, Bio.SeqUtils, format conversions.

#### M02A · Text Files in Python 🔁 (T6 §1–2) · ~1.5 h

| Section | Must include |
|---|---|
| 2A.1 File paths | Relative vs absolute; `pathlib.Path`; why `DATA_DIR` |
| 2A.2 Opening files | `open()` modes table: `r`, `w`, `a`, `x`, `r+`, `b`; encoding |
| 2A.3 **Three ways to read** | `.read()` vs `.readlines()` vs `for line in f` — table of memory use & when to use each |
| 2A.4 `with` statement | Why context managers; what happens on exceptions |
| 2A.5 **Writing & appending** | `.write()`, `.writelines()`, `print(..., file=f)`; `w` overwrites vs `a` appends (demo the danger) |
| 2A.6 Cleaning lines | `.strip()`, skipping blanks/comments, splitting TSV |
| 2A.7 Error handling | `try/except FileNotFoundError`; `os.path.exists` / `Path.exists()` |
| Practice | Reuse T6 Q1–Q20 (count lines, filter lines, merge files, reverse content…) |

#### M02B · FASTA by Hand 🔁 (T6 §3–4 + T4) · ~1.5 h

| Section | Must include |
|---|---|
| 2B.1 FASTA format spec | Header `>`, wrapped sequence lines, multi-FASTA |
| 2B.2 **Reading FASTA** | Parser → `dict{header: seq}`; handle wrapped lines |
| 2B.3 **Writing FASTA** | Line-wrap at 60/70 chars helper |
| 2B.4 **Splitting a multi-FASTA** | One file per record; split into chunks of N records |
| 2B.5 Filter & transform | Write only records with GC>50 %; write reverse complements |
| 2B.6 FASTQ (brief) | 4-line structure; Phred+33 decoding; mean quality (from T4) |
| 2B.7 Why not hand-parse in real life? | Edge cases → motivates Biopython |

📦 `multi_sample.fasta` (10–20 records, mixed lengths/GC), `reads_small.fastq`

#### M02C · Biopython: SeqIO, GenBank & SeqUtils 🔁 (T7) · ~2 h

| Section | Must include |
|---|---|
| 2C.1 Biopython overview | Package map: `Bio.Seq`, `Bio.SeqRecord`, `Bio.SeqIO`, `Bio.SeqUtils`, `Bio.Entrez`, `Bio.PDB`, `Bio.KEGG` |
| 2C.2 `Seq` object | `.complement()`, `.reverse_complement()`, `.transcribe()`, `.translate(to_stop=True, table=11)` |
| 2C.3 `SeqRecord` | `.id`, `.name`, `.description`, `.seq`, `.annotations`, `.features` |
| 2C.4 **`SeqIO.read` vs `SeqIO.parse`** | Single vs **MultiFASTA**; `SeqIO.to_dict`, `SeqIO.index` for big files |
| 2C.5 **Writing** | `SeqIO.write`; creating SeqRecords from scratch |
| 2C.6 **GenBank files** | Reading `.gb`; annotations dict; organism, taxonomy |
| 2C.7 **Extracting features** | Loop `record.features`; filter `feature.type == "CDS"`; `qualifiers["gene"]`, `["product"]`, `["translation"]`; `feature.location`, `feature.extract(record.seq)`; strand handling |
| 2C.8 **`Bio.SeqUtils`** | `gc_fraction`, `molecular_weight`, `MeltingTemp`, `ProtParam.ProteinAnalysis` (pI, instability, aromaticity) |
| 2C.9 **Format conversions** | `SeqIO.convert` GenBank→FASTA, FASTA→tab; FASTQ→FASTA; table of supported formats |
| ★★★ Challenge | From a bacterial GenBank: export all CDS proteins to FASTA, and a TSV of gene, product, length, GC |

📦 `ecoli_lac_operon.gb`, `tp53_human.gb`, `insulin_protein.gp`

---

### Module 3 — Object-Oriented Programming

**Syllabus coverage:** Classes and Objects, Encapsulation, Inheritance, Polymorphism, Abstraction; Access modifiers (public, private, protected); theoretical and practical exercises.

#### M03A · Classes & Objects 🔁 (T8 §1–2) · ~1.5 h

| Section | Must include |
|---|---|
| 3A.1 Procedural vs OOP | Same task (sequence stats) written both ways |
| 3A.2 Class & object | Blueprint vs instance; `class DNASequence:` |
| 3A.3 `__init__` & `self` | Instance attributes; validation in constructor |
| 3A.4 Instance vs class attributes | `codon_table` as class attribute shared by all |
| 3A.5 Methods | `gc_content()`, `reverse_complement()` returning new objects |
| 3A.6 Dunder methods | `__str__`, `__repr__`, `__len__`, `__eq__`, `__add__` (concatenate sequences) |
| 3A.7 `@classmethod` & `@staticmethod` | `DNASequence.from_fasta(path)`; `is_valid_base(b)` |

#### M03B · Four Pillars & Access Modifiers 🔁/🆕 (T8 §3–5 + new) · ~2 h

| Section | Must include | Biology example |
|---|---|---|
| 3B.1 **Encapsulation** | Bundling data + behaviour; validating setters | `Protein` whose sequence can't be set to invalid letters |
| 3B.2 **Access modifiers** 🆕 | Table below; name mangling demo (`obj._Class__attr`); "consenting adults" convention | `Patient` record: public `id`, `_protected` lab values, `__private` identifier |
| 3B.3 `@property` 🆕 | Getter/setter/deleter; read-only computed attributes | `seq.gc` as property |
| 3B.4 **Inheritance** | Base/derived, `super().__init__`, method resolution order, multiple inheritance (brief) | `Organism → Bacterium / Eukaryote → Human` |
| 3B.5 **Polymorphism** | Method overriding; duck typing; operator overloading | `Cell.divide()` for `ProkaryoticCell` vs `EukaryoticCell` |
| 3B.6 **Abstraction** 🆕 | `from abc import ABC, abstractmethod`; can't instantiate abstract class; interface design | `abstract class BiologicalSequence` with `alphabet` & `translate()` → `DNA`, `RNA`, `Protein` |

Access modifier table to include in the notebook:

| Modifier | Syntax | Accessible from | Enforced? |
|---|---|---|---|
| Public | `self.name` | Anywhere | — |
| Protected | `self._name` | Class + subclasses (by convention) | No — convention only |
| Private | `self.__name` | Class only (name-mangled to `_ClassName__name`) | Partially (mangling) |

**Theory questions (short-answer, for quizzes):** 10 conceptual Qs, e.g. "Why does Python not truly enforce private?", "Difference between abstraction and encapsulation?", "What is the MRO of `class C(A, B)`?"

#### M03C · OOP Practice & Mini-Project 🔁 (T8 20 Qs) · lab

- Reorder the existing 20 practice questions by pillar and difficulty.
- **Mini-project — "Bio Sequence Toolkit":**
  1. `BiologicalSequence(ABC)` with abstract `alphabet`, `molecular_weight()`.
  2. `DNA`, `RNA`, `Protein` subclasses; `DNA.transcribe() -> RNA`, `RNA.translate() -> Protein`.
  3. Private `__id`, protected `_source_file`, public `seq`.
  4. `SequenceCollection` class holding many sequences: `__len__`, `__iter__`, `filter_by_length()`, `to_fasta(path)`.
  5. Load `multi_sample.fasta` into the collection and print a summary table.
- Provide a test cell with ~15 asserts so students self-check.

---

### Module 4 — Data Visualisation

**Syllabus coverage:** Biological plots and their applications; Matplotlib and Seaborn; Bar, Histogram, Pie, Box, Heatmap, Violin; Labels & Titles, Legends, Colour Palettes, Annotations.

#### M04A · Biological Plots & Their Applications 🔁 (T9 catalogue) · ~45 min theory

- Keep the existing "field → topics → plots" catalogue (genomics, proteomics, phylogenetics, …).
- Add a **"choose the right chart" decision table**:

| Question you're asking | Plot | Biology example |
|---|---|---|
| Compare a value across categories | Bar | Gene count per chromosome |
| Distribution of one variable | Histogram | Read length / gene length distribution |
| Parts of a whole (few categories) | Pie | Nucleotide composition; variant class proportions |
| Distribution across groups, with outliers | Box | Expression of a gene across tissues |
| Distribution shape across groups | Violin | Single-cell expression per cluster |
| Matrix of values | Heatmap | Gene × sample expression; correlation matrix |
| Relationship between two variables | Scatter | Expression vs GC; volcano plot |

- Section on **bad plots** (3D pies, rainbow colormaps, truncated axes) and colour-blind-safe palettes.

#### M04B · Matplotlib 🔁/🆕 · ~2 h

For **each** of the six required plot types, a section containing: (1) the biology dataset, (2) minimal code, (3) a fully customised version, (4) an exercise.

| Section | Plot | Dataset 📦 |
|---|---|---|
| 4B.0 Anatomy | Figure, Axes, `plt.subplots`, OO vs pyplot interface, saving (`dpi`, `bbox_inches`) | — |
| 4B.1 **Bar** | Vertical, horizontal, grouped, stacked, error bars | `genes_per_chromosome.csv` |
| 4B.2 **Histogram** | `bins`, density, overlaid histograms with `alpha` | GC% of records in `multi_sample.fasta` |
| 4B.3 **Pie** | `autopct`, `explode`, donut variant | Base composition of TP53 |
| 4B.4 **Box** | Grouped boxes, notches, showing outliers | `expression_tissues.csv` |
| 4B.5 **Violin** | `plt.violinplot`, showing medians | same |
| 4B.6 **Heatmap** | `imshow` + `colorbar`, tick labels, annotate cells | `expression_matrix.csv` |
| 4B.7 **Customisation** | **Labels & titles**, **legends** (location, outside plot), **colour palettes/colormaps**, **annotations** (`ax.annotate` with arrows, `ax.text`), multi-panel figures | |

#### M04C · Seaborn & Publication Styling 🔁/🆕 · ~1.5 h

| Section | Content |
|---|---|
| 4C.1 Why Seaborn | Tidy (long) data, pandas integration; `melt` from wide to long |
| 4C.2 Same 6 plots in Seaborn | `barplot`, `histplot`/`kdeplot`, (pie → matplotlib), `boxplot`, `violinplot`, `heatmap(annot=True)`, `clustermap` |
| 4C.3 `hue`, `col`, `row` | Faceting by condition |
| 4C.4 **Palettes** | `sns.color_palette`, qualitative vs sequential vs diverging; `viridis`, `colorblind` |
| 4C.5 Themes | `set_theme`, `context="paper"/"talk"` |
| 4C.6 Bio showcase | Volcano plot with annotated top genes; clustered expression heatmap |
| ★★★ Challenge | Reproduce a given target figure exactly (provide PNG) |

---

### Module 5 — Accessing and Querying Databases & Web Scraping

**Syllabus coverage:** Fetching sequences, advanced searches, saving data (GenBank, UniProt, PDB, NCBI Entrez, KEGG); FASTA, GenBank, PDB formats; best practices, API keys & email IDs; Web scraping fundamentals, legal & ethical considerations, Requests & BeautifulSoup; biology scraping tasks as HW.

> Merge **T5 + T10** into M05A/M05B; rewrite **T11** into M05D/M05E.

#### M05A · NCBI Entrez: GenBank & PubMed 🔁 · ~2 h

| Section | Must include |
|---|---|
| 5A.1 Database landscape | Table: NCBI (Nucleotide, Protein, Gene, PubMed, SRA), UniProt, PDB, KEGG — what each stores, IDs (accession formats) |
| 5A.2 Entrez setup | `Entrez.email` (**mandatory**), `Entrez.api_key` (loaded from env, never hard-coded) |
| 5A.3 E-utilities | `einfo`, `esearch`, `efetch`, `esummary`, `elink` — what each does (table) |
| 5A.4 **Fetching sequences** | `efetch(db="nucleotide", id=..., rettype="fasta"/"gb", retmode="text")` → `SeqIO.read` |
| 5A.5 **Advanced searches** | Field tags: `TP53[Gene] AND Homo sapiens[Organism] AND refseq[filter]`; date ranges; `retmax`; `usehistory="y"` for large result sets |
| 5A.6 PubMed | Search, fetch abstracts (`rettype="medline"`), parse with `Bio.Medline` |
| 5A.7 **Saving data** | Write fetched records to `outputs/` as FASTA/GenBank; caching (don't re-download if file exists) |
| 5A.8 GenBank format deep-dive | Annotated LOCUS/DEFINITION/FEATURES/ORIGIN screenshot |

#### M05B · UniProt, PDB & KEGG 🔁/🆕 · ~2 h

| Section | Must include |
|---|---|
| 5B.1 **UniProt** | REST API (`https://rest.uniprot.org/uniprotkb/search?query=...&format=tsv&fields=...`) with `requests`; fetching FASTA; parsing TSV into pandas; `SeqIO.read(..., "swiss")` for UniProt text format |
| 5B.2 **PDB** | `Bio.PDB.PDBList().retrieve_pdb_file`; `PDBParser`/`MMCIFParser`; SMCRA hierarchy (Structure→Model→Chain→Residue→Atom); count residues, extract sequence per chain (`PPBuilder`); RCSB search API (brief) |
| 5B.3 **PDB file format** | ATOM/HETATM columns explained; PDB vs mmCIF |
| 5B.4 **KEGG** | `Bio.KEGG.REST`: `kegg_list`, `kegg_find`, `kegg_get`; get genes in a pathway (e.g. hsa04115 p53 signalling); parse with `Bio.KEGG.KGML` (optional) |
| 5B.5 Integrated example | Gene symbol → NCBI Gene → UniProt accession → PDB structures → KEGG pathways for **TP53** |
| Practice | Merge existing GenBank / UniProt / PDB / Entrez practice question sets from T5/T10 |

#### M05C · Best Practices in Bioinformatics Programming 🆕 · ~1 h

| Topic | Content |
|---|---|
| Why email & API key | NCBI policy: identifies you, lets NCBI contact you before blocking; API key raises allowed request rate (≈3 → 10 requests/s) |
| Getting an NCBI API key | Steps: NCBI account → Settings → API Key Management |
| **Storing secrets** | `.env` file + `python-dotenv`; `os.environ["NCBI_API_KEY"]`; `.env` in `.gitignore`; Colab secrets; **never commit keys** (show what a leaked key on GitHub looks like) |
| Rate limiting | `time.sleep`, batching IDs (comma-separated `id=`), `usehistory` + `retstart`/`retmax` |
| Robust requests | `try/except`, retries with back-off, checking `response.status_code`, timeouts |
| Reproducibility | Record accession *versions* (NM_000546.6), date fetched, tool versions; cache raw downloads |
| Code hygiene | Functions with docstrings, constants at top, no hard-coded paths, logging vs print |

Exercise: refactor a deliberately "bad" script (hard-coded key, no sleep, no error handling) into a good one.

#### M05D · Web Scraping Fundamentals 🔁/🆕 (from T11) · ~2 h

| Section | Must include |
|---|---|
| 5D.1 What & when | API first, scraping last — decision flow: *Is there an API / bulk download? → use it. Else → check terms → scrape politely* |
| 5D.2 **Legal & ethical considerations** | `robots.txt` (and `urllib.robotparser`), Terms of Service, copyright & database rights, personal/clinical data (privacy), server load, identifying User-Agent, citing the source |
| 5D.3 HTTP basics | URL, GET/POST, status codes, headers, query params |
| 5D.4 **`requests`** | `requests.get(url, params=..., headers=..., timeout=10)`; `.text`, `.json()`, `.status_code` |
| 5D.5 HTML structure | Tags, attributes, DOM tree, browser DevTools "Inspect" |
| 5D.6 **BeautifulSoup** | `BeautifulSoup(html, "lxml")`; `find`, `find_all`, `select` (CSS selectors); `.get_text()`, `["href"]`; tables → list of dicts → pandas (`pd.read_html` shortcut) |
| 5D.7 Pagination & politeness | Loop pages with `time.sleep`; stop conditions |
| 5D.8 Offline practice | Parse saved HTML pages in `data/html/` so class doesn't depend on live websites |
| Appendix | String-method scraping & MechanicalSoup forms (keep from T11, optional) |

#### M05E · Web Scraping Homework 🔁 (T11 tasks) · homework

Each task specifies: **target source**, **API alternative (if any)**, **fields to extract**, **output file**, **ethics note**.

| HW | Task | Output |
|---|---|---|
| HW1 | **Gene expression data** — expression summary for 5 genes (e.g. GEO dataset page / Expression Atlas) | `gene_expression.csv` |
| HW2 | **Protein information** — name, length, function, subcellular location for 10 UniProt IDs | `protein_info.csv` |
| HW3 | **Clinical trials** — trials for a disease (title, phase, status, start date); prefer the ClinicalTrials.gov API | `clinical_trials.csv` |
| HW4 | **Taxonomy** — lineage for 10 species from NCBI Taxonomy | `taxonomy.csv` |
| HW5 | **Pathways** — genes in 3 KEGG/Reactome pathways; overlap between them | `pathway_genes.csv` + Venn/upset plot |
| HW6 | **Literature review** — 50 PubMed abstracts for a query; top keywords; publications per year bar chart | `pubmed_abstracts.csv` + plot |

Deliverable per HW: notebook + CSV + 1 plot + a 3-line "ethics statement" (robots.txt checked? API used? rate limit?).

---

### Module 6 — os, NumPy & pandas (Assignment)

**Notebook:** `M06_Assignment.ipynb` 🆕 · self-study ~6 h · graded

Structure: short primer per library (theory + 3–4 worked examples) followed by graded tasks.

#### Part A — `os` / `pathlib` / `shutil`

| Primer | Graded tasks |
|---|---|
| `os.getcwd`, `os.listdir`, `os.path.join/exists/splitext/getsize`, `os.makedirs`, `os.walk`, `shutil.copy/move`; `pathlib` equivalents and `glob` | A1. Walk `data/` and report every FASTA with size and record count. A2. Organise a messy folder: move files into `fasta/`, `genbank/`, `tables/` by extension. A3. Batch-rename `sample1.fa` → `S001.fasta`. |

#### Part B — NumPy

| Primer | Graded tasks |
|---|---|
| Arrays vs lists, `dtype`, shape, indexing/slicing, boolean masks, vectorised ops, broadcasting, `mean/std/axis`, `np.log2`, random seeds | B1. One-hot encode a DNA sequence into a (L × 4) array. B2. Sliding-window GC content with vectorised ops; compare speed with a loop (`%timeit`). B3. Log2 fold-change and z-score normalisation of an expression matrix. B4. Build a nucleotide position-frequency matrix from aligned sequences. |

#### Part C — pandas

| Primer | Graded tasks |
|---|---|
| Series/DataFrame, `read_csv`, `head/info/describe`, `loc/iloc`, filtering, `sort_values`, `groupby/agg`, `merge`, `melt/pivot`, missing values, `to_csv` | C1. Load `expression_matrix.csv`; filter genes with mean > threshold; top 10 variable genes. C2. Merge expression with `gene_annotation.csv`; group by chromosome. C3. Convert FASTA → DataFrame (id, length, GC) and export. C4. Tidy (melt) the matrix and feed it to a Seaborn plot (links back to M04). |

Grading: auto-tests (60 %) + code quality/comments (20 %) + short written interpretations (20 %).

---

### Capstone (optional)

**`Capstone_Gene_Report_Pipeline.ipynb`** — ties every module together.

> Input: a gene symbol (e.g. `BRCA1`). Output: a folder with a FASTA, a GenBank, a CSV of features, 3 plots, and a markdown report.

| Step | Module used |
|---|---|
| Validate input; fetch GenBank & FASTA via Entrez (with API key from `.env`) | M5A, M5C |
| Parse with SeqIO; extract CDS/exons; compute GC, ORFs, protein properties | M1, M2 |
| Wrap logic in a `GeneReport` class with private/protected attributes | M3 |
| Fetch UniProt function + PDB IDs + KEGG pathways | M5B |
| Store results in pandas; organise output dirs with `os`/`pathlib` | M6 |
| Plot: exon length bar, GC sliding window, amino-acid composition | M4 |
| Write a markdown report | M2 (file writing) |

---

## 6. Data files to create

All go in `data/` with an entry in `data/README.md` (source, accession+version, date downloaded, licence).

| File | Folder | Used in | How to create |
|---|---|---|---|
| `toy_gene_with_introns.txt` | sequences | M1C | Hand-crafted ~300 nt with 3 exons, GT-AG introns |
| `toy_exon_coordinates.tsv` | tables | M1C | Matching coordinates (0-based, half-open) |
| `dna_sequences.txt` | sequences | M2A | Keep existing |
| `multi_sample.fasta` | sequences | M2B, M3C, M4B | 15 records; mix of lengths and GC; 1 with lowercase, 1 with N's |
| `reads_small.fastq` | sequences | M2B | 20 reads with varied quality |
| `tp53_human_mrna.fasta` | sequences | Thread | Entrez: NM_000546 |
| `tp53_human.gb` | genbank | M2C | Entrez: NM_000546 GenBank |
| `ecoli_lac_operon.gb` | genbank | M2C | Entrez: e.g. J01636 |
| `insulin_protein.gp` | genbank | M2C | Rename existing `example4.gp` if it's insulin |
| `1tup.pdb` / `1tup.cif` | structures | M5B | p53–DNA complex from RCSB (offline backup) |
| `genes_per_chromosome.csv` | tables | M4B | Counts per human chromosome |
| `expression_tissues.csv` | tables | M4B/C | Long format: gene, tissue, replicate, TPM (simulated is fine; state so) |
| `expression_matrix.csv` | tables | M4, M6 | 50 genes × 8 samples (2 conditions × 4 reps) |
| `gene_annotation.csv` | tables | M6 | gene, chromosome, start, end, biotype |
| `differential_expression.csv` | tables | M4C (volcano) | gene, log2FC, pvalue |
| `uniprot_sample.html`, `pubmed_sample.html`, `table_sample.html` | html | M5D | Saved pages for offline scraping |

Provide a script `data/build_data.py` that regenerates the simulated tables with a fixed random seed and downloads the real records (so data is reproducible).

---

## 7. Assessment plan

| Component | Weight | Covers | Format |
|---|---|---|---|
| Lab exercises (weekly) | 20 % | M1–M5 | Completed exercise notebooks; auto-graded asserts |
| Quiz 1 | 10 % | M1–M2 | MCQ + "predict the output" + short code |
| Quiz 2 | 10 % | M3–M4 | Incl. OOP theory Qs from M3B |
| Scraping homework | 15 % | M5D–E | 2–3 HW tasks of student's choice from M5E |
| os/NumPy/pandas assignment | 15 % | M6 | Graded notebook |
| End-term exam | 30 % | All | Practical coding exam on unseen biological data |
| Capstone (bonus / alternative) | +5–10 % | All | Project + 5-min demo |

*(Adjust weights to institutional norms.)*

**Rubric dimensions (labs/HW):** correctness (tests pass) · biological correctness (frames, coordinates, units) · code readability (names, functions, comments) · reproducibility (paths, no hard-coded keys, runs top-to-bottom) · interpretation (1–3 sentence explanation of result).

---

## 8. Suggested teaching schedule

(14-week semester, 1 lecture + 1 lab per week)

| Week | Lecture | Lab | Due |
|---|---|---|---|
| 1 | M00 Setup; M01A Core Python (1/2) | M01A exercises | — |
| 2 | M01A (2/2); M01B Sequence manipulation | M01B | — |
| 3 | M01C ORFs/exons/introns | M01D practice set | Lab 1 |
| 4 | M02A Text files; M02B FASTA by hand | M02A/B | **Quiz 1 (M1)** |
| 5 | M02C Biopython | M02C challenge | Lab 2 |
| 6 | M03A Classes & objects | M03A | — |
| 7 | M03B Pillars & access modifiers | M03C mini-project | Lab 3; **release M06 assignment** |
| 8 | M04A Plot theory; M04B Matplotlib | M04B | — |
| 9 | M04C Seaborn | M04C challenge | Lab 4; **Quiz 2 (M3–M4)** |
| 10 | M05A Entrez | M05A | — |
| 11 | M05B UniProt/PDB/KEGG; M05C Best practices | M05B/C | Lab 5 |
| 12 | M05D Web scraping | M05D offline practice; **release M05E HW** | **M06 assignment due** |
| 13 | Capstone walkthrough / revision | Capstone work | **Scraping HW due** |
| 14 | Revision | Mock exam | End-term |

---

## 9. Authoring workflow & quality checklist

### Workflow for building each notebook

```
1. Plan     → fill the section table for the notebook (from §5) as a GitHub Issue
2. Data     → add/confirm required files in data/ + data/README.md entry
3. Solution → write the SOLUTION notebook first (all code working)
4. Tests    → add assert cells under every exercise
5. Strip    → copy to exercise notebook; replace answers with `# TODO` / `...`
6. Run      → Kernel → Restart & Run All on both (exercise should fail only at TODOs)
7. Review   → checklist below; peer/TA review via Pull Request
8. Publish  → merge to main; update README module table + Colab badge
```

**Tip:** keep one source notebook with tagged solution cells and generate the student version automatically (e.g. `nbgrader`, or a tiny script that removes cells tagged `solution` and inserts `# TODO`). This prevents exercise/solution drift.

### Per-notebook quality checklist

- [ ] Header cell with title, author, date, Colab badge, time, difficulty, prerequisites
- [ ] 3–6 measurable learning outcomes
- [ ] Setup cell uses `DATA_DIR` / `OUT_DIR`; no absolute personal paths
- [ ] Every concept: theory → worked example → ✏️ try-it → ⚠️ common mistakes
- [ ] Every exercise: clear input, expected output, TODO cell, assert test cell
- [ ] Exercises graded ★ / ★★ / ★★★
- [ ] Biology is correct (reading frames, strand, 0- vs 1-based coordinates, units)
- [ ] All writes go to `outputs/`, never into `data/`
- [ ] Network cells: `Entrez.email` set, API key from env, `time.sleep`, cached to file
- [ ] Runs top-to-bottom on a fresh kernel in < 5 min (solution version)
- [ ] Runs on Google Colab
- [ ] Summary/cheat-sheet table at the end
- [ ] References / further reading
- [ ] Matching solution notebook exists in `solutions/`
- [ ] Outputs cleared before commit in exercise notebooks (`nbstripout` recommended)

### CI: `.github/workflows/test-notebooks.yml`

```yaml
name: Test solution notebooks
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -r requirements.txt
      - name: Execute all solution notebooks (offline ones)
        env:
          NCBI_EMAIL: ${{ secrets.NCBI_EMAIL }}
          NCBI_API_KEY: ${{ secrets.NCBI_API_KEY }}
        run: |
          pytest --nbval-lax modules/*/solutions/*.ipynb \
                 --ignore-glob="modules/M05_*/solutions/*"   # network notebooks tested manually
```

---

## 10. Migration plan (old → new)

| Old file | Action | New file(s) |
|---|---|---|
| `Tutorial_1_BioComputing_Basics` (+ solution) | Split by topic | `M01A_Core_Python`, `M01B_Sequence_Manipulation` |
| `Tutorial_3_BioComputing_Intermediate` (+ solution) | Move problems | `M01B` (Tm, k-mers), `M01C` (ORFs), `M01D` (rest) |
| `Tutorial_2_Sequence_Alignment` (+ solution) | Rename, mark optional | `M01E_Enrichment_Sequence_Alignment` |
| `Tutorial_6_FileHandling_Part1` | Split | `M02A_Text_Files`, `M02B_FASTA_by_Hand` |
| `Tutorial_4_FASTA_FASTQ` (+ solution) | Merge into | `M02B_FASTA_by_Hand` (FASTQ section) |
| `Tutorial_7_FileHandling_Part2` | Rename + extend (SeqUtils, ProtParam, conversions table) | `M02C_Biopython_SeqIO_GenBank` |
| `Tutorial_8_OOPs` | Split + add access modifiers, `@property`, ABC | `M03A`, `M03B`, `M03C` |
| `Tutorial_9_DataVisualization` | Split + add hist/pie/customisation + Seaborn | `M04A`, `M04B`, `M04C` |
| `Tutorial_5_Biological_Databases` + `Tutorial_10_BiologicalDB` | **Merge** (dedupe) + add UniProt REST, KEGG genes-in-pathway | `M05A`, `M05B` |
| — | New | `M05C_Best_Practices_API_Keys` |
| `Tutorial_11_WebScraping` | Rewrite core around Requests+BS4; tasks → HW | `M05D`, `M05E` |
| — | New | `M00_Setup`, `M06_Assignment`, `Capstone` |
| `Exercises/Data/Class1_FileHandeling*.ipynb` | **Delete** (duplicates) | — |
| `Exercises/Data/output*.fasta`, `output.gb`, `modified_output.fasta`, `new_file.txt`, `example_converted.fasta`, `protein_output.fasta` | **Delete** (generated) | regenerated into `outputs/` |
| Remaining `Exercises/Data/*` | Move & rename descriptively | `data/sequences/`, `data/genbank/` |

**Order of work (suggested):**
1. Repo hygiene: `requirements.txt`, `.gitignore`, `data/` move, delete duplicates/outputs.
2. Template + M00.
3. M01 → M02 (highest reuse, fastest wins).
4. M03 (add missing access modifiers/abstraction).
5. M05A–C (merge T5/T10; add best practices) — needed early because it has the most broken-link risk.
6. M04, M05D–E.
7. M06 assignment, solutions for everything, CI.
8. Capstone, cheatsheets, quizzes.

### README update

Replace the current tutorial list with a module table:

```markdown
| Module | Notebooks | Open in Colab |
|---|---|---|
| M01 Python Basics | [A](modules/...) · [B](...) · [C](...) · [D](...) | [![Colab](badge)](link) |
| … | … | … |
```

---

## 11. References

1. **SummarySheet** (course Drive folder) — extra PDFs for quick reference.
2. Real Python — https://realpython.com/ (Python basics, file I/O, OOP, requests, BeautifulSoup, pandas, NumPy tutorials)
3. Biopython — https://biopython.org/ and the *Biopython Tutorial & Cookbook* (SeqIO, Entrez, PDB, KEGG chapters)
4. NCBI E-utilities documentation (Entrez Programming Utilities Help) and NCBI API key guidance
5. UniProt REST API documentation — https://www.uniprot.org/help/api
6. RCSB PDB documentation (file formats, APIs) — https://www.rcsb.org/
7. KEGG REST API — https://www.kegg.jp/kegg/rest/keggapi.html
8. Matplotlib gallery — https://matplotlib.org/stable/gallery/ · Seaborn tutorial — https://seaborn.pydata.org/tutorial.html
9. Beautiful Soup docs — https://www.crummy.com/software/BeautifulSoup/bs4/doc/ · Requests docs — https://requests.readthedocs.io/
10. pandas user guide — https://pandas.pydata.org/docs/user_guide/ · NumPy for absolute beginners — https://numpy.org/doc/stable/user/absolute_beginners.html
11. Topic-specific references are listed in the "Further reading" cell of each notebook.

---
*Maintainer: Prateek Paul · Licence: MIT · Update this plan whenever a module's scope changes.*
