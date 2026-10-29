# Data Provenance and Descriptions

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
