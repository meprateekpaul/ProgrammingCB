import json

notebook_ex = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## This notebook is created by Prateek Paul.\n",
    "* Email: prateekp@iiitd.ac.in\n",
    "* LinkedIn: [linkedin.com/in/prateekpaulpro/](https://linkedin.com/in/prateekpaulpro/)\n",
    "\n",
    "Disclaimer: \n",
    "The code and content in this notebook are intended solely for educational purposes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bio Computing Course - Tutorial 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Topic: Working with FASTA and FASTQ Formats\n",
    "### Welcome to Tutorial 4! Handling standard bioinformatics file formats is a crucial skill. In this tutorial, we will write custom parsers for FASTA and FASTQ files without using external libraries like Biopython."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Basic FASTA Parser\n",
    "#### Question: A FASTA file consists of a header line starting with '>' followed by sequence lines. Write a function `parse_fasta(fasta_string)` that takes a multi-line string in FASTA format and returns a dictionary where keys are sequence IDs and values are the concatenated sequence strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code here\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. FASTQ Quality Score Conversion\n",
    "#### Question: FASTQ files store quality scores as ASCII characters. The most common encoding is Phred+33. Write a function `char_to_phred(char)` that takes a single ASCII character and returns its numerical Phred quality score (subtract 33 from its ASCII integer value)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code here\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Calculating Average Quality\n",
    "#### Question: Given a string of FASTQ quality characters (e.g., `IIIIIIIIIJJJ`), write a function `average_quality(qual_string)` that calculates the average Phred score for the sequence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write your code here\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

notebook_sol = json.loads(json.dumps(notebook_ex))

notebook_sol["cells"][4]["source"] = [
    "def parse_fasta(fasta_string):\n",
    "    sequences = {}\n",
    "    current_id = None\n",
    "    current_seq = []\n",
    "    \n",
    "    for line in fasta_string.strip().split('\\n'):\n",
    "        line = line.strip()\n",
    "        if line.startswith('>'):\n",
    "            if current_id:\n",
    "                sequences[current_id] = ''.join(current_seq)\n",
    "            current_id = line[1:] # Remove '>'\n",
    "            current_seq = []\n",
    "        else:\n",
    "            current_seq.append(line)\n",
    "            \n",
    "    if current_id:\n",
    "        sequences[current_id] = ''.join(current_seq)\n",
    "        \n",
    "    return sequences\n",
    "\n",
    "sample_fasta = \"\"\">\n",
    ">Seq1\n",
    "ATGC\n",
    "CGTA\n",
    ">Seq2\n",
    "GGGG\n",
    "AAAA\n",
    "\"\"\"\n",
    "print(parse_fasta(sample_fasta))"
]
notebook_sol["cells"].insert(5, {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Explanation**: The parser iterates line by line. When it hits a `>`, it saves the *previous* accumulated sequence (if it exists) into the dictionary, and starts tracking a new ID. Non-header lines are appended to a list, which is joined into a single string when the record finishes."
   ]
})

notebook_sol["cells"][7]["source"] = [
    "def char_to_phred(char):\n",
    "    return ord(char) - 33\n",
    "\n",
    "print(\"ASCII 'I' is Phred score:\", char_to_phred('I'))\n",
    "print(\"ASCII '!' is Phred score:\", char_to_phred('!'))"
]
notebook_sol["cells"].insert(8, {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Explanation**: FASTQ uses ASCII offset by 33 to represent quality scores compactly as single characters. The `ord()` function in Python returns the integer ASCII value of a character."
   ]
})

notebook_sol["cells"][10]["source"] = [
    "def average_quality(qual_string):\n",
    "    scores = [ord(char) - 33 for char in qual_string]\n",
    "    return sum(scores) / len(scores)\n",
    "\n",
    "qual = \"IIIII!!!!!\"\n",
    "print(\"Average Quality:\", average_quality(qual))"
]
notebook_sol["cells"].insert(11, {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Explanation**: We use a list comprehension to convert the entire string into a list of integers, then divide the sum by the length to get the mean. This is crucial for filtering out low-quality sequencing reads."
   ]
})

with open("Notebooks/Exercises/Tutorial_4_FASTA_FASTQ.ipynb", "w") as f:
    json.dump(notebook_ex, f, indent=1)

with open("Notebooks/Solutions/Tutorial_4_FASTA_FASTQ_Solutions.ipynb", "w") as f:
    json.dump(notebook_sol, f, indent=1)
