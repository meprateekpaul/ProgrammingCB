# Grading Rubric — Web Scraping Homework (M05E)
**Course:** Programming for Computational Biology (Python)

Each homework deliverable consists of:
1. Executable Jupyter notebook
2. Generated output CSV file in `outputs/`
3. Summary figure (PNG)
4. A 3-line "Ethics & Politeness Statement"

| Component | Weight | Criteria |
|---|---|---|
| **Technical Implementation** | 40% | Robust HTML parsing using `BeautifulSoup` with CSS selectors or API requests. Handles pagination, error status codes (`4xx`/`5xx`), and data cleaning into pandas DataFrames. |
| **Data Integrity & Export** | 25% | Output CSV matches expected schema, contains non-empty clean data, properly encodes biological identifiers, and resides in `outputs/`. |
| **Data Visualisation** | 15% | High-quality Matplotlib/Seaborn plot summarizing the scraped dataset (e.g., publication trends, score distributions, pathway overlaps). Labels, titles, and legends are complete. |
| **Ethics & Politeness Statement** | 20% | Explicit 3-line declaration detailing: (1) whether `robots.txt` and Terms of Service were verified, (2) user-agent identification and delay (`time.sleep`) used, and (3) explanation of why scraping was chosen over bulk download or public API. |
