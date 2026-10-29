# Module 5 Cheatsheet — Databases & Web Scraping

### NCBI Entrez Best Practices
```python
import os, time
from Bio import Entrez, SeqIO
from dotenv import load_dotenv

load_dotenv()
Entrez.email = os.getenv("NCBI_EMAIL", "your_email@university.edu")
Entrez.api_key = os.getenv("NCBI_API_KEY", None)

# 1. Search (esearch)
handle = Entrez.esearch(db="nucleotide", term="TP53[Gene] AND Homo sapiens[Organism]", retmax=5)
record = Entrez.read(handle)
handle.close()
id_list = record["IdList"]

time.sleep(0.35)  # Rate limiting (max 3 req/sec without key, 10 with key)

# 2. Fetch (efetch)
fetch_handle = Entrez.efetch(db="nucleotide", id=id_list[0], rettype="gb", retmode="text")
seq_record = SeqIO.read(fetch_handle, "genbank")
fetch_handle.close()
```

### UniProt REST API (Modern endpoint)
```python
import requests
import pandas as pd
import io

url = "https://rest.uniprot.org/uniprotkb/search"
params = {
    "query": "gene:TP53 AND organism_id:9606",
    "format": "tsv",
    "fields": "accession,id,gene_names,protein_name,length"
}
response = requests.get(url, params=params, timeout=10)
df = pd.read_csv(io.StringIO(response.text), sep="\t")
```

### PDB Structural Parsing
```python
from Bio.PDB import PDBParser, PPBuilder

parser = PDBParser(QUIET=True)
structure = parser.get_structure("1TUP", "data/structures/1tup.pdb")

# Hierarchy: Structure -> Model -> Chain -> Residue -> Atom (SMCRA)
for model in structure:
    for chain in model:
        print("Chain:", chain.id)
        ppb = PPBuilder()
        for pp in ppb.build_peptides(chain):
            print(pp.get_sequence())
```

### Polite Web Scraping with BeautifulSoup
```python
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "BioinformaticsClassProject/1.0 (student@iiitd.ac.in)"}
response = requests.get("https://example.com/target", headers=headers, timeout=10)

soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", id="data-table")
rows = table.find_all("tr")
data = [[td.get_text(strip=True) for td in tr.find_all(["td", "th"])] for tr in rows]
```
