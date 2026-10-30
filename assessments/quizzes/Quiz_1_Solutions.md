# Quiz 1 — Python Basics & File Handling (Answer Key & Solutions)
**Course:** Programming for Computational Biology (Python)  
**Covers:** Module 1 (Core Python, Sequences, ORFs/Exons) & Module 2 (File Handling, FASTA, Biopython)  
**Total Marks:** 30

---

### Part A: Multiple Choice Questions (10 Marks, 1 Mark Each)

1. **Answer: B (`"TCA"`)**  
   *Explanation:* `seq[1:7:2]` slices string `"ATGCGATCG"` starting at index 1 (`'T'`), ending before index 7 (`'C'`), with step 2. This selects indices 1 (`'T'`), 3 (`'C'`), and 5 (`'A'`), yielding `"TCA"`.

2. **Answer: B (`str.maketrans()`)**  
   *Explanation:* `str.maketrans(from_chars, to_chars)` produces an integer-mapped translation table consumed by `str.translate()`.

3. **Answer: B (`seq[99:250]`)**  
   *Explanation:* Python uses 0-based indexing and half-open intervals `[start, end)`. A 1-based inclusive range `100..250` converts to 0-based `100 - 1 = 99` and end coordinate `250` (which excludes 250 in half-open notation, thus capturing index 249, the 250th base).

4. **Answer: C (`Iterating line-by-line with a for line in f: generator loop or SeqIO.parse()`)**  
   *Explanation:* Both `read()` and `readlines()` load the entire multi-gigabyte file into memory at once, risking out-of-memory errors. Generator iterators process one record at a time with $O(1)$ memory overhead.

5. **Answer: B (`Q = 40 (p_error = 0.0001, 99.99% accuracy)`)**  
   *Explanation:* In Sanger/Illumina 1.8+ Phred+33 format, $Q = \text{ord}(c) - 33$. For ASCII `'I'` ($\text{ord} = 73$), $Q = 73 - 33 = 40$. Probability of error $p = 10^{-Q/10} = 10^{-4} = 0.0001$.

6. **Answer: B (`seq.translate(to_stop=True)`)**  
   *Explanation:* `Bio.Seq.translate(to_stop=True)` instructs Biopython to cease translation upon reaching the first stop codon (`*`), omitting subsequent translated codons.

7. **Answer: B (`read() returns a single SeqRecord (raises error if >1 record exists); parse() returns an iterator over records.`)**  
   *Explanation:* `SeqIO.read()` is designed for single-record files and validates that exactly one record exists. `SeqIO.parse()` returns an iterator yielding multiple records.

8. **Answer: C (`GT ... AG`)**  
   *Explanation:* The Chambon rule states that nearly all eukaryotic nuclear pre-mRNAs feature canonical 5' splice donor dinucleotide `GU` (`GT` in DNA) and 3' splice acceptor dinucleotide `AG`.

9. **Answer: C (`-1`)**  
   *Explanation:* Biopython conventions assign `+1` for forward strand, `-1` for reverse complement strand, and `0` / `None` for unstranded features.

10. **Answer: C (`"a"`)**  
    *Explanation:* Mode `"a"` (append) places the file pointer at the end of the file, preserving existing data. Mode `"w"` truncates/erases the file before writing.

---

### Part B: Predict the Output (10 Marks, 2 Marks Each)

11. **Output:** `0.25`  
    *Explanation:* `"ATGCATGC"` has length 8. Base `'G'` occurs 2 times. $2 / 8 = 0.25$.

12. **Output:** `'GCAT'`  
    *Explanation:* `str.maketrans("ACGT", "TGCA")` complements `"ATGC"` to `"TACG"`. Slicing `[::-1]` reverses it to `"GCAT"`.

13. **Output:** `'seq1-seq2'`  
    *Explanation:* Header lines start with `">"`. `line.strip()[1:]` extracts `"seq1"` and `"seq2"`. `"-".join(...)` produces `"seq1-seq2"`.

14. **Output:** `17.25`  
    *Explanation:* The characters `'!'`, `'*'`, `'5'`, `'I'` have ASCII values 33, 42, 53, 73. Subtracting 33 gives Phred quality scores $[0, 9, 20, 40]$. The average is $(0 + 9 + 20 + 40) / 4 = 69 / 4 = 17.25$.

15. **Output:** `2`  
    *Explanation:* Codons in frame 0 are `['ATG', 'AAA', 'TAA', 'ATG', 'CCC']`. Codons matching `'ATG'` occur at indices 0 and 3. `len(starts)` is 2.

---

### Part C: Code Writing (10 Marks)

16. **extract_exons Solution (5 Marks):**
```python
def extract_exons(genomic_seq: str, coordinates: list[tuple[int, int]]) -> str:
    """
    Concatenate exon slices from genomic DNA using 0-based half-open coordinates.
    """
    if not coordinates:
        return ""
    return "".join(genomic_seq[start:end] for start, end in coordinates)
```

17. **parse_fasta_simple Solution (5 Marks):**
```python
def parse_fasta_simple(filepath: str) -> dict[str, str]:
    """
    Parse a FASTA file into a dictionary of {header: sequence} without Biopython.
    """
    sequences = {}
    current_header = None
    seq_parts = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = "".join(seq_parts)
                current_header = line[1:].strip()
                seq_parts = []
            else:
                seq_parts.append(line)
        if current_header is not None:
            sequences[current_header] = "".join(seq_parts)
            
    return sequences
```
