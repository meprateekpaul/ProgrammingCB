# Grading Rubric — Capstone Gene Report Pipeline
**Course:** Programming for Computational Biology (Python)

The Capstone synthesizes every module of the curriculum into an automated bioinformatics pipeline. Given a single gene symbol (e.g. `TP53`, `BRCA1`), the script builds an end-to-end report.

| Criteria | Weight | Details |
|---|---|---|
| **Pipeline Architecture & Integration** | 30% | Seamlessly integrates data acquisition (NCBI Entrez / UniProt REST), parsing (`Bio.SeqIO`), OOP abstraction, tabular wrangling (`pandas`), and plotting (`matplotlib`/`seaborn`). |
| **Object-Oriented Design** | 25% | Encapsulates gene metadata, sequences, and analytics within well-structured classes. Adheres to encapsulation (public/protected/private), properties, and clear method boundaries. |
| **Data Visualization & Polish** | 20% | Generates a 3-panel figure: (1) exon length / gene structure, (2) sliding-window GC content, and (3) amino acid composition. Fully labeled with titles, legends, and publication themes. |
| **Defensive Programming & Security** | 15% | Uses `.env` for API keys, respects rate limits (`time.sleep`), caches downloads to prevent re-querying, gracefully handles network timeouts and missing annotations. |
| **Final Automated Report** | 10% | Automatically generates a structured Markdown report summarizing gene biology, sequence statistics, pathways, and embedded figures in an isolated output folder. |
