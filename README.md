# Programming for Computational Biology (PCB) — Python 🧬💻

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Biopython](https://img.shields.io/badge/Biopython-1.83%2B-green.svg)](https://biopython.org/)
[![CI: Test Solution Notebooks](https://github.com/meprateekpaul/ProgrammingCB/actions/workflows/test-notebooks.yml/badge.svg)](https://github.com/meprateekpaul/ProgrammingCB/actions/workflows/test-notebooks.yml)

Welcome to the **Programming for Computational Biology** course repository! This curriculum offers a comprehensive, hands-on journey through scientific computing in modern bioinformatics—from core syntax and sequence mechanics to object-oriented domain modeling, high-throughput file parsers (FASTA/FASTQ/GenBank), publication-grade visualization, programmatic database mining (NCBI Entrez, UniProt, RCSB PDB, KEGG), polite web scraping, and vectorised data science (`numpy`, `pandas`).

---

## 🧭 Course Blueprint & Continuous Biological Thread

A central design pillar of this curriculum is **biological continuity**. Rather than using detached toy problems, students follow the same canonical set of genes throughout the entire semester:
- **Human TP53** (Tumor protein p53 — master guardian of the genome)
- **Human INS** (Insulin — preproprotein processing and peptide hormones)
- **Human HBB** (Hemoglobin subunit beta — genetic variants & structural biology)
- **E. coli lacZ** (β-galactosidase — classic operon regulation and bacterial genomics)

Students analyze these entities progressively as **character strings** (Module 1), **structured disk files** (Module 2), **custom domain objects** (Module 3), **publication figures** (Module 4), **remote database records** (Module 5), and **matrix entries** (Module 6).

---

## 📚 Curriculum Structure

All modules are structured in `modules/`, with student exercises in the module folder and reference solutions in `solutions/`. Every notebook includes a **one-click Google Colab badge** and self-contained environment setup.

| Module | Title | Notebooks | Level | Colab Link |
|---|---|---|---|---|
| **M00** | **Setup & Orientation** | [M00_Setup_and_Orientation](modules/M00_Setup/M00_Setup_and_Orientation.ipynb) | ★☆☆ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M00_Setup/M00_Setup_and_Orientation.ipynb) |
| **M01** | **Python Basics & Sequences** | [1A: Core Python](modules/M01_Python_Basics/M01A_Core_Python.ipynb) · [1B: Sequence Manipulation](modules/M01_Python_Basics/M01B_Sequence_Manipulation.ipynb) · [1C: ORFs, Exons & Introns](modules/M01_Python_Basics/M01C_ORFs_Exons_Introns.ipynb) · [1D: Practice Problems](modules/M01_Python_Basics/M01D_Practice_Problems.ipynb) · [1E: Enrichment: Alignment](modules/M01_Python_Basics/M01E_Enrichment_Sequence_Alignment.ipynb) | ★★☆ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M01_Python_Basics/M01A_Core_Python.ipynb) |
| **M02** | **File Handling & Biopython** | [2A: Text Files](modules/M02_File_Handling/M02A_Text_Files.ipynb) · [2B: FASTA by Hand & FASTQ](modules/M02_File_Handling/M02B_FASTA_by_Hand.ipynb) · [2C: Biopython SeqIO & GenBank](modules/M02_File_Handling/M02C_Biopython_SeqIO_GenBank.ipynb) | ★★☆ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M02_File_Handling/M02A_Text_Files.ipynb) |
| **M03** | **Object-Oriented Programming** | [3A: Classes & Objects](modules/M03_OOP/M03A_Classes_and_Objects.ipynb) · [3B: Four Pillars & Access Modifiers](modules/M03_OOP/M03B_Four_Pillars_and_Access_Modifiers.ipynb) · [3C: OOP Practice & Mini-Project](modules/M03_OOP/M03C_OOP_Practice_and_Mini_Project.ipynb) | ★★★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M03_OOP/M03A_Classes_and_Objects.ipynb) |
| **M04** | **Biological Data Visualisation** | [4A: Biological Plots Theory](modules/M04_Visualisation/M04A_Biological_Plots_Theory.ipynb) · [4B: Matplotlib](modules/M04_Visualisation/M04B_Matplotlib.ipynb) · [4C: Seaborn & Styling](modules/M04_Visualisation/M04C_Seaborn_and_Styling.ipynb) | ★★☆ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M04_Visualisation/M04A_Biological_Plots_Theory.ipynb) |
| **M05** | **Databases & Web Scraping** | [5A: NCBI Entrez & PubMed](modules/M05_Databases_and_Scraping/M05A_Entrez_GenBank_PubMed.ipynb) · [5B: UniProt, PDB & KEGG](modules/M05_Databases_and_Scraping/M05B_UniProt_PDB_KEGG.ipynb) · [5C: Best Practices & API Keys](modules/M05_Databases_and_Scraping/M05C_Best_Practices_API_Keys.ipynb) · [5D: Web Scraping Fundamentals](modules/M05_Databases_and_Scraping/M05D_Web_Scraping_Fundamentals.ipynb) · [5E: Web Scraping Homework](modules/M05_Databases_and_Scraping/M05E_Web_Scraping_Homework.ipynb) | ★★★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M05_Databases_and_Scraping/M05A_Entrez_GenBank_PubMed.ipynb) |
| **M06** | **os, NumPy & pandas** | [M06_Assignment (Graded Notebook)](modules/M06_os_NumPy_pandas/M06_Assignment.ipynb) | ★★★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/M06_os_NumPy_pandas/M06_Assignment.ipynb) |
| **Capstone** | **Automated Gene Report** | [Capstone_Gene_Report_Pipeline](modules/Capstone/Capstone_Gene_Report_Pipeline.ipynb) | ★★★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meprateekpaul/ProgrammingCB/blob/main/modules/Capstone/Capstone_Gene_Report_Pipeline.ipynb) |

---

## ⚡ Quick Start

### 1. Local Setup with Conda (Recommended)
```bash
git clone https://github.com/meprateekpaul/ProgrammingCB.git
cd ProgrammingCB

# Create and activate environment
conda env create -f environment.yml
conda activate pcb

# Launch JupyterLab
jupyter lab
```

### 2. Local Setup with Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

### 3. Google Colab
Click any of the **Open in Colab** badges in the table above. The setup cell at the top of each notebook automatically clones the repository and mounts required datasets in `data/`.

---

## 📂 Repository Organization

```text
ProgrammingCB/
├── README.md                     # Landing page: course overview & module directory
├── COURSE_PLAN.md                # Comprehensive course blueprint & authoring guide
├── SYLLABUS.md                   # Student-facing course syllabus
├── LICENSE                       # MIT License
├── requirements.txt              # Standard pip dependencies
├── environment.yml               # Conda environment definition
├── .gitignore                    # Ignores outputs/, caches, and credentials
│
├── data/                         # Crated, read-only biological datasets
│   ├── README.md                 # Full provenance and accession metadata
│   ├── build_data.py             # Reproducible data generation & download script
│   ├── sequences/                # FASTA, FASTQ, and raw sequence files
│   ├── genbank/                  # RefSeq GenBank and GenPept files
│   ├── structures/               # PDB and mmCIF coordinate models
│   ├── tables/                   # Gene annotation, counts, and expression tables
│   └── html/                     # Mock pages for offline web scraping practice
│
├── modules/                      # Curriculum core modules
│   ├── M00_Setup/
│   ├── M01_Python_Basics/
│   ├── M02_File_Handling/
│   ├── M03_OOP/
│   ├── M04_Visualisation/
│   ├── M05_Databases_and_Scraping/
│   ├── M06_os_NumPy_pandas/
│   └── Capstone/
│
├── assessments/                  # Quizzes & grading rubrics
│   ├── quizzes/                  # Quiz 1 and Quiz 2 question papers
│   └── rubrics/                  # Rubrics for Labs, Homework, and Capstone
│
├── cheatsheets/                  # Quick-reference summary cards for Modules 1–6
│
└── outputs/                      # (Git-ignored) Target directory for student code exports
```

---

## 📊 Assessments & Grading
Detailed assessment information, quizzes, and rubrics are available in the [assessments/](assessments/) directory:
- [Student Syllabus](SYLLABUS.md)
- [Quiz 1: Python Basics & File Handling](assessments/quizzes/Quiz_1.md)
- [Quiz 2: OOP & Visualisation](assessments/quizzes/Quiz_2.md)
- [Weekly Lab Rubric](assessments/rubrics/Rubric_Lab.md)
- [Web Scraping Homework Rubric](assessments/rubrics/Rubric_Homework.md)
- [Capstone Project Rubric](assessments/rubrics/Rubric_Capstone.md)

---

## 👤 Author & Maintainer
**Prateek Paul**  
- 🏛️ PhD Researcher in Computational Biology, IIIT Delhi  
- ✉️ Email: `prateekp@iiitd.ac.in`  
- 🌐 Portfolio: [meprateekpaul.github.io](https://meprateekpaul.github.io/)  
- 💼 LinkedIn: [linkedin.com/in/prateekpaulpro](https://www.linkedin.com/in/prateekpaulpro/)  
- 🐙 GitHub: [@meprateekpaul](https://github.com/meprateekpaul)

---

## 📄 License
This repository and its educational materials are distributed under the [MIT License](LICENSE).
