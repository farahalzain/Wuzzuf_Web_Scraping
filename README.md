#***Wuzzuf Web Scraping – Python Project***

**Wuzzuf Web Scraping** is a Python project designed to extract job postings from [Wuzzuf](https://wuzzuf.net/) for multiple keywords such as Data Science, Machine Learning, AI, and Python Developer. The project scrapes job titles, company names, occupations, specifications, and links to postings, and saves the results into CSV files.

---

# ***Features***

* Scrapes jobs from Wuzzuf for multiple keywords.
* Extracts **Title**, **Link**, **Occupation**, **Company**, and **Specs**.
* Saves **individual CSV files** for each keyword.
* Combines all scraped data into a **single CSV file**.
* Handles pagination automatically and respects polite delays.
* Clean and modular code using helper functions.

---

# ***Project Structure***

Wuzzuf-Web-Scraping/

scrap_helper.py     # Contains scraping and data processing functions
main.py             # Main script to run scraping and save CSV files


---

# ***Code Overview***

## `scrap_helper.py` – Helper Functions

* `find_no_of_jobs(job)` → Returns total jobs and total pages for a given query.
* `scrap_pages(query, delay=1)` → Scrapes all pages for a query, returns both a dictionary and a DataFrame.
* `combine_dfs(dfs)` → Combines multiple DataFrames and removes duplicates.
* `combine_dicts(dicts)` → Combines multiple job dictionaries into one.

## `main.py` – Main Script

* Defines the list of keywords to scrape.
* Uses `scrap_helper` functions to scrape each keyword.
* Saves individual CSV files for each keyword.
* Combines all results into `combined_jobs.csv`.

---

# ***How to Run***

* Libraries: `requests`, `beautifulsoup4`, `pandas`


# ***Run the Project***


Run the file **main.py**


This will:

1. Scrape jobs for the predefined keywords.
2. Save a CSV file for each keyword.
3. Save a combined CSV file `combined_jobs.csv`.

---

## Example Output

Individual CSVs:

* `data_science.csv`
* `machine_learning.csv`
* `artificial_intelligence.csv`
* `python_developer.csv`

Combined CSV:

* `combined_jobs.csv`

Each CSV contains columns:
`Title | Link | Occupation | Company | Specs`

---
