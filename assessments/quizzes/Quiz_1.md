# Quiz 1 — Python Basics & File Handling
**Course:** Programming for Computational Biology (Python)  
**Covers:** Module 1 (Core Python, Sequences, ORFs/Exons) & Module 2 (File Handling, FASTA, Biopython)  
**Time Allowed:** 45 minutes · **Total Marks:** 30

---

### Part A: Multiple Choice Questions (10 Marks, 1 Mark Each)

1. Given `seq = "ATGCGATCG"`, what is the result of `seq[1:7:2]`?
   - A) `"TGC"`
   - B) `"TCA"`
   - C) `"TGA"`
   - D) `"TCG"`

2. Which built-in function or method creates a one-to-one translation table suitable for `str.translate()`?
   - A) `dict.fromkeys()`
   - B) `str.maketrans()`
   - C) `str.replace()`
   - D) `chr.translate()`

3. If a 1-based GenBank feature spans from nucleotide position 100 to 250 inclusive, how should this interval be sliced in Python (0-based, half-open)?
   - A) `seq[100:250]`
   - B) `seq[99:250]`
   - C) `seq[99:249]`
   - D) `seq[100:251]`

4. When reading a multi-gigabyte FASTA file on a memory-constrained machine, which approach is best practice?
   - A) `SeqIO.to_dict(SeqIO.parse(f, "fasta"))`
   - B) `f.readlines()`
   - C) Iterating line-by-line with a `for line in f:` generator loop or `SeqIO.parse()`
   - D) `f.read()`

5. In FASTQ format, what does the Phred quality character `I` (ASCII value 73) correspond to in standard Phred+33 encoding?
   - A) Q = 33 (p_error ≈ 1 in 2,000)
   - B) Q = 40 (p_error = 0.0001, 99.99% accuracy)
   - C) Q = 73 (impossible score)
   - D) Q = 10 (p_error = 0.1)

6. Which Biopython method extracts the translated amino acid sequence of a `Seq` object and terminates at the first in-frame stop codon?
   - A) `seq.translate(stop=True)`
   - B) `seq.translate(to_stop=True)`
   - C) `seq.to_protein()`
   - D) `seq.transcribe().translate()`

7. What is the fundamental difference between `SeqIO.read()` and `SeqIO.parse()` in Biopython?
   - A) `read()` is for GenBank; `parse()` is for FASTA.
   - B) `read()` returns a single `SeqRecord` (raises error if >1 record exists); `parse()` returns an iterator over records.
   - C) `read()` loads metadata only; `parse()` loads sequence data.
   - D) There is no difference; they are aliases.

8. In canonical eukaryotic splicing, what two-letter motifs delineate the 5' donor and 3' acceptor sites of introns?
   - A) AG ... GT
   - B) AT ... TA
   - C) GT ... AG
   - D) GC ... CG

9. What does `feature.location.strand` return for a feature annotated on the reverse complement strand in Biopython?
   - A) `0`
   - B) `1`
   - C) `-1`
   - D) `"-"`

10. Which mode should be passed to Python's `open()` function to append new sequence records without erasing existing contents?
    - A) `"w"`
    - B) `"r+"`
    - C) `"a"`
    - D) `"x"`

---

### Part B: Predict the Output (10 Marks, 2 Marks Each)

11. What will the following code print?
```python
dna = "ATGCATGC"
counts = {base: dna.count(base) for base in "ACGT"}
print(counts["G"] / len(dna))
```

12. What is the output of the following sequence reverse complement one-liner?
```python
seq = "ATGC"
tr = str.maketrans("ACGT", "TGCA")
print(seq.translate(tr)[::-1])
```

13. What will this file manipulation code write to `output.txt`?
```python
lines = [">seq1\n", "ATGC\n", ">seq2\n", "GCTA\n"]
headers = [line.strip()[1:] for line in lines if line.startswith(">")]
print("-".join(headers))
```

14. What does the following generator expression compute?
```python
quals = "!*5I"  # ASCII values: 33, 42, 53, 73
scores = [ord(c) - 33 for c in quals]
print(sum(scores) / len(scores))
```

15. What is the value of `len(orfs)`?
```python
seq = "ATGAAATAAATGCCC"
# Reading frame 0
codons = [seq[i:i+3] for i in range(0, len(seq)-2, 3)]
starts = [i for i, c in enumerate(codons) if c == "ATG"]
print(len(starts))
```

---

### Part C: Code Writing (10 Marks)

16. **(5 Marks)** Write a function `extract_exons(genomic_seq, coordinates)`:
    - `genomic_seq`: A string of genomic DNA.
    - `coordinates`: A list of tuples `[(start_1, end_1), (start_2, end_2), ...]`, 0-based half-open coordinates.
    - Returns: The spliced mRNA coding sequence (concatenated exons).
    - Handle edge cases: return empty string if coordinates is empty.

17. **(5 Marks)** Write a function `parse_fasta_simple(filepath)` without using Biopython:
    - Reads a FASTA file.
    - Returns a dictionary `{header: sequence}` where multiline sequences are concatenated and whitespace stripped.
