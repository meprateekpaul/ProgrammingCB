# Programming for Computational Biology (PCB) — Python
## Course Syllabus

**Course Code / Title:** Programming for Computational Biology (Python)  
**Instructor / Maintainer:** Prateek Paul (prateekp@iiitd.ac.in)  
**Repository:** [meprateekpaul/ProgrammingCB](https://github.com/meprateekpaul/ProgrammingCB)  
**Target Audience:** Undergraduate & Graduate students in Computational Biology, Bioinformatics, and Quantitative Life Sciences.

---

### Course Description
This course provides a rigorous, hands-on foundation in Python programming tailored specifically for modern computational biology and bioinformatics. Moving systematically from core language syntax and sequence manipulation to object-oriented domain modeling, high-throughput file processing (FASTA, FASTQ, GenBank), publication-grade data visualization, programmatic database querying (NCBI Entrez, UniProt, RCSB PDB, KEGG), polite web scraping, and vectorised scientific computing (`numpy`, `pandas`), students gain end-to-end computational fluency.

A unified biological thread (analyzing real human genes such as **TP53**, **INS**, **HBB**, and *E. coli* **lacZ**) connects all modules, allowing students to experience the same biological entity across multiple computational abstractions.

---

### Prerequisites
- High-school biology (DNA/RNA transcription, genetic code, basic genetics).
- No prior programming experience required (Module 0 provides complete setup and environment orientation).

---

### Module Overview

#### Module 0: Setup & Orientation
- Computing in biology: scale, reproducibility, and automation.
- Local environments (Anaconda, venv) vs Google Colab.
- Jupyter Lab essentials, shortcuts, and repo orientation.
- Git & GitHub workflow overview.

#### Module 1: Python Basics & Biological Strings
- Core Python: variables, numeric types, boolean logic, conditionals.
- Strings: slicing, nucleotide methods, immutability, formatting.
- Collections: lists, tuples, sets, dictionaries (codon translation maps).
- Control flow: loops, iteration over sequence windows, list/dict comprehensions.
- Functions: scope, documentation, modularity.
- Biological operations: GC content, AT/GC skew, reverse complement, transcription, translation.
- Gene structure: reading frames, ORF identification, exon/intron extraction with 0-based coordinates.
- *Enrichment:* Global & local sequence alignment fundamentals (Needleman-Wunsch & Smith-Waterman).

#### Module 2: File Handling & Biopython
- Native Python file I/O: paths (`pathlib`), context managers (`with`), memory tradeoffs (`read` vs `readlines` vs chunked iteration).
- Reading, writing, and splitting multi-FASTA files by hand.
- FASTQ format parsing and Phred quality score calculation.
- Biopython foundation: `Bio.Seq`, `Bio.SeqRecord`, `Bio.SeqIO`.
- GenBank record parsing, feature extraction (`CDS`, gene products, locations, qualifiers).
- `Bio.SeqUtils`: molecular weight, melting temperature calculation, `ProtParam.ProteinAnalysis`.
- Biological format conversions (GenBank ↔ FASTA ↔ Tabular).

#### Module 3: Object-Oriented Programming (OOP)
- Classes and instances: attributes, methods, `__init__`, and `self`.
- Magic (dunder) methods: `__str__`, `__repr__`, `__len__`, `__add__`, `__eq__`.
- Class methods (`@classmethod`) and static utilities (`@staticmethod`).
- The Four Pillars of OOP:
  - **Encapsulation:** private (`__attr`), protected (`_attr`), public attributes, `@property` getters/setters.
  - **Inheritance:** base classes, subclassing, `super()`, method resolution order (MRO).
  - **Polymorphism:** method overriding, duck typing, operator overloading.
  - **Abstraction:** abstract base classes (`abc.ABC`), `@abstractmethod` interface enforcement.
- Mini-Project: Building a modular `Bio Sequence Toolkit`.

#### Module 4: Biological Data Visualisation
- Chart selection theory for biological questions.
- Matplotlib: Figure and Axes architecture, subplots, publication styling.
- Core biological plots:
  - Bar charts: gene counts across chromosomes.
  - Histograms & KDE: sequence length and GC distributions.
  - Pie and donut charts: base composition and categorical breakdowns.
  - Box plots & Violin plots: gene expression distributions across tissues.
  - Heatmaps & clustered heatmaps: multi-gene expression matrices.
- Seaborn: tidy data representation, colorblind-safe palettes, faceting (`hue`, `col`, `row`).
- Publication polish: legends, annotations, figure resolution (`dpi`), and vector exports.

#### Module 5: Biological Databases & Web Scraping
- Landscape of biological databases: NCBI, UniProt, RCSB PDB, KEGG.
- NCBI Entrez programmatic utilities via `Bio.Entrez`: `esearch`, `efetch`, `esummary`, `elink`.
- UniProt REST API (`rest.uniprot.org`) querying with `requests` and `pandas`.
- Protein structural data: RCSB PDB file retrieval, mmCIF, and `Bio.PDB` hierarchy (SMCRA).
- Pathway querying with `Bio.KEGG.REST`.
- Best practices: API keys, email identification, rate limiting, and defensive HTTP request retries.
- Web scraping fundamentals: HTTP headers, status codes, HTML DOM structure.
- Polite scraping with `BeautifulSoup` (BS4): `robots.txt` compliance, ethics, rate limits, table parsing.
- Practical homework: extracting public biological metadata across multiple portals.

#### Module 6: Vectorised Computing & Data Science (`os`, `numpy`, `pandas`)
- File system automation: `os.walk`, batch file renaming, directory tree manipulation.
- NumPy: N-dimensional arrays, vectorisation, broadcasting, DNA one-hot encoding, sliding windows.
- Pandas: Series, DataFrames, expression matrix manipulation, filtering, aggregation, merging, tidying (`melt`).
- End-to-end graded assignment integrating all three libraries.

#### Capstone Project: Automated Gene Report Pipeline
- End-to-end pipeline accepting a gene symbol (e.g., `TP53`, `BRCA1`).
- Automatic sequence and metadata retrieval (Entrez / UniProt).
- Object-oriented gene data encapsulation.
- Feature extraction, statistical summarization, multi-panel figure generation.
- Automated generation of a publication-ready Markdown/PDF report.

---

### Assessment Scheme
| Component | Weight | Scope |
|---|---|---|
| Weekly Lab Exercises | 20% | Auto-graded test asserts across Modules 1–5 |
| Quiz 1 | 10% | Python Basics & File Handling (M1–M2) |
| Quiz 2 | 10% | OOP & Visualization (M3–M4) |
| Web Scraping Homework | 15% | Real-world biological data extraction & ethics statement (M5) |
| NumPy & Pandas Assignment | 15% | Graded data science tasks (M6) |
| End-Term Practical Exam | 30% | Hands-on coding on unseen biological data |
| Capstone Project (Bonus) | +5–10% | Gene Report Pipeline & code review |

---
*For repository guidelines, notebook authoring templates, and contribution standards, refer to [COURSE_PLAN.md](COURSE_PLAN.md).*
