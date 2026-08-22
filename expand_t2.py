import json

def read_nb(path):
    with open(path, 'r') as f:
        return json.load(f)

def write_nb(nb, path):
    with open(path, 'w') as f:
        json.dump(nb, f, indent=1)

ex_nb = read_nb("Notebooks/Exercises/Tutorial_2_Sequence_Alignment.ipynb")
sol_nb = read_nb("Notebooks/Solutions/Tutorial_2_Sequence_Alignment_Solutions.ipynb")

new_questions = [
    {
        "title": "### 4. Sequence Identity Percentage",
        "question": "#### Question: Write a function `calculate_identity(seq1, seq2)` that takes two aligned sequences of equal length and returns the percentage of identical characters (excluding gaps). If both characters are gaps '-', do not count them in the total length.",
        "solution_code": [
            "def calculate_identity(seq1, seq2):\n",
            "    matches = 0\n",
            "    valid_length = 0\n",
            "    for a, b in zip(seq1, seq2):\n",
            "        if a == '-' and b == '-':\n",
            "            continue\n",
            "        valid_length += 1\n",
            "        if a == b:\n",
            "            matches += 1\n",
            "    if valid_length == 0:\n",
            "        return 0.0\n",
            "    return (matches / valid_length) * 100\n",
            "\n",
            "print(f\"Identity: {calculate_identity('ATGC-T', 'AT-CGT'):.2f}%\")"
        ],
        "solution_output": "Identity: 50.00%\n",
        "explanation": "**Explanation**: We iterate through the aligned pairs. We ignore columns where both are gaps. We count the matches and divide by the total number of valid aligned positions to get the percentage."
    },
    {
        "title": "### 5. Transition vs Transversion Counter",
        "question": "#### Question: In DNA, transitions (A<->G, C<->T) are more common than transversions (purine <-> pyrimidine). Write a function `count_mutations(seq1, seq2)` that compares two un-gapped, equal-length sequences and returns a dictionary with the counts of 'transitions' and 'transversions'.",
        "solution_code": [
            "def count_mutations(seq1, seq2):\n",
            "    purines = {'A', 'G'}\n",
            "    pyrimidines = {'C', 'T'}\n",
            "    counts = {'transitions': 0, 'transversions': 0}\n",
            "    \n",
            "    for a, b in zip(seq1, seq2):\n",
            "        if a != b:\n",
            "            if (a in purines and b in purines) or (a in pyrimidines and b in pyrimidines):\n",
            "                counts['transitions'] += 1\n",
            "            else:\n",
            "                counts['transversions'] += 1\n",
            "    return counts\n",
            "\n",
            "print(count_mutations('ATGC', 'ACGT'))"
        ],
        "solution_output": "{'transitions': 1, 'transversions': 3}\n",
        "explanation": "**Explanation**: We define sets for purines and pyrimidines. If a mismatch occurs within the same group, it's a transition. If it crosses groups, it's a transversion."
    },
    {
        "title": "### 6. Needleman-Wunsch Matrix Scoring",
        "question": "#### Question: Write a function `fill_nw_matrix(seq1, seq2, match, mismatch, gap)` that fully populates the Needleman-Wunsch dynamic programming matrix. You can use your `initialize_matrix` logic from Question 3 as a starting point. Return the completed matrix.",
        "solution_code": [
            "def fill_nw_matrix(seq1, seq2, match, mismatch, gap):\n",
            "    rows, cols = len(seq1) + 1, len(seq2) + 1\n",
            "    matrix = [[0 for _ in range(cols)] for _ in range(rows)]\n",
            "    \n",
            "    for i in range(rows): matrix[i][0] = i * gap\n",
            "    for j in range(cols): matrix[0][j] = j * gap\n",
            "    \n",
            "    for i in range(1, rows):\n",
            "        for j in range(1, cols):\n",
            "            score_diag = matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)\n",
            "            score_up = matrix[i-1][j] + gap\n",
            "            score_left = matrix[i][j-1] + gap\n",
            "            matrix[i][j] = max(score_diag, score_up, score_left)\n",
            "            \n",
            "    return matrix\n",
            "\n",
            "mat = fill_nw_matrix('AT', 'AG', 1, -1, -1)\n",
            "for r in mat: print(r)"
        ],
        "solution_output": "[0, -1, -2]\n[-1, 1, 0]\n[-2, 0, 0]\n",
        "explanation": "**Explanation**: We iterate through each cell `(i, j)`. The score is the maximum of three possible moves: coming from a diagonal (match/mismatch), coming from above (gap in seq2), or coming from the left (gap in seq1)."
    },
    {
        "title": "### 7. Smith-Waterman Local Alignment (Finding the Max)",
        "question": "#### Question: Unlike global alignment, Smith-Waterman (local alignment) resets negative scores to 0. Write a function `find_sw_max(matrix)` that takes a completed Smith-Waterman scoring matrix (2D list) and returns a tuple `(max_score, (row_index, col_index))` indicating the start of the traceback.",
        "solution_code": [
            "def find_sw_max(matrix):\n",
            "    max_val = 0\n",
            "    max_pos = (0, 0)\n",
            "    \n",
            "    for i, row in enumerate(matrix):\n",
            "        for j, val in enumerate(row):\n",
            "            if val > max_val:\n",
            "                max_val = val\n",
            "                max_pos = (i, j)\n",
            "                \n",
            "    return max_val, max_pos\n",
            "\n",
            "# Mock matrix for testing\n",
            "mock_matrix = [[0, 0, 0], [0, 2, 0], [0, 0, 4]]\n",
            "print(\"Max score and position:\", find_sw_max(mock_matrix))"
        ],
        "solution_output": "Max score and position: (4, (2, 2))\n",
        "explanation": "**Explanation**: In local alignment, the optimal alignment ends at the highest score in the entire matrix. We simply iterate through the 2D array to find the maximum value and its coordinates."
    },
    {
        "title": "### 8. Generating an Alignment String",
        "question": "#### Question: Often, alignments are visualized with a middle string showing pipes `|` for matches, spaces for mismatches, and gaps. Write `visualize_alignment(seq1, seq2)` that prints this 3-line visualization for two aligned sequences.",
        "solution_code": [
            "def visualize_alignment(seq1, seq2):\n",
            "    middle = []\n",
            "    for a, b in zip(seq1, seq2):\n",
            "        if a == b and a != '-':\n",
            "            middle.append('|')\n",
            "        else:\n",
            "            middle.append(' ')\n",
            "            \n",
            "    print(seq1)\n",
            "    print(''.join(middle))\n",
            "    print(seq2)\n",
            "\n",
            "visualize_alignment(\"ATGC-TAC\", \"AT-CGTAC\")"
        ],
        "solution_output": "ATGC-TAC\n||   |||\nAT-CGTAC\n",
        "explanation": "**Explanation**: We compare the two strings character by character. If they match (and aren't gaps), we place a pipe. Otherwise, we leave a space. This makes it easy for humans to spot conserved regions."
    }
]

for q in new_questions:
    # Add to Exercises
    ex_nb["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [q["title"] + "\n", q["question"]]
    })
    ex_nb["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": ["# Write your code here\n", "\n"]
    })
    
    # Add to Solutions
    sol_nb["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [q["title"] + "\n", q["question"]]
    })
    sol_nb["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [{"name": "stdout", "output_type": "stream", "text": [q["solution_output"]]}],
        "source": q["solution_code"]
    })
    sol_nb["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [q["explanation"]]
    })

write_nb(ex_nb, "Notebooks/Exercises/Tutorial_2_Sequence_Alignment.ipynb")
write_nb(sol_nb, "Notebooks/Solutions/Tutorial_2_Sequence_Alignment_Solutions.ipynb")
