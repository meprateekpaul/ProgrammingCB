# Grading Rubric — Weekly Lab Exercises
**Course:** Programming for Computational Biology (Python)

Each weekly laboratory notebook submission is evaluated on a 100-point scale across 5 core dimensions:

| Dimension | Weight | Exemplary (90–100%) | Competent (70–89%) | Needs Improvement (<70%) |
|---|---|---|---|---|
| **1. Functional Correctness & Asserts** | 35% | All unit test assertions pass cleanly without modification. Code handles edge cases (empty strings, N-bases, lowercase). | 80%+ of test asserts pass. Minor failure on unusual edge cases. | Multiple failed assertions; code raises unhandled exceptions. |
| **2. Biological Accuracy & Conventions** | 25% | Accurate reading frames, strict 0-based coordinate handling, correct strand logic (+/-), canonical GT-AG splicing rules followed. | Correct core biology with minor coordinate off-by-one errors or unhandled terminal stop codons. | Major biological fallacies (e.g., translating non-triplet length without frame shift check, inverted complementary mapping). |
| **3. Code Quality & Modularity** | 15% | Clear variable names (`seq`, `exon_coords`, not `s`, `x`), type hints, informative docstrings, modular helper functions. | Understandable code with occasional magic numbers or lack of docstrings. | Monolithic repetitive code, poor naming, dead or commented-out code clutter. |
| **4. Reproducibility & Environment** | 15% | All file I/O uses relative `DATA_DIR` and `OUT_DIR`. Notebook runs completely from start to finish via "Restart & Run All". | Works with minor manual path tweaking; writes to directory root instead of `outputs/`. | Hard-coded absolute paths specific to student's local machine; notebook fails top-to-bottom run. |
| **5. Scientific Interpretation** | 10% | 1–3 concise sentences explaining the biological significance of calculated values, distributions, or findings. | Brief summary provided without connecting back to biological hypothesis. | Missing interpretations or incorrect biological deductions. |
