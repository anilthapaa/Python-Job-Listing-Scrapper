# Fake Python Jobs Scraper

A beginner Python web scraper that collects job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and saves them to a CSV file.

Project Done From: https://roadmap.sh/projects/job-listings-scraper 

## What It Does

- Fetches the Fake Python Jobs webpage
- Extracts the **job title**, **company name**, **location**, and **detail page URL** for every listing
- Handles missing fields gracefully (falls back to `"N/A"`)
- Saves all results to `jobs.csv`
- Prints a preview of the first 3 results in the terminal

## Project Structure

```
fake-jobs-scraper/
├── scraper.py        # Main script
├── jobs.csv          # Output file (generated on run)
└── README.md         # This file
```

## Technologies Used

| Library | Purpose |
|---|---|
| `requests` | Fetches the webpage over HTTP |
| `beautifulsoup4` | Parses HTML and extracts data |
| `csv` | Writes results to a CSV file (built-in) |

## Setup & Usage

### 1. Install dependencies

**Mac / Linux:**
```bash
pip install requests beautifulsoup4
```

**Windows:**
```powershell
py -m pip install requests beautifulsoup4
```

### 2. Run the scraper

**Mac / Linux:**
```bash
python scraper.py
```

**Windows:**
```powershell
py scraper.py
```

### 3. Check the output

A `jobs.csv` file will be created in the same folder with all job listings.

```
title,company,location,url
Software Engineer,Dice,Christopherville Mississippi,https://...
...
```

## Sample Output

```
Fetching jobs from https://realpython.github.io/fake-jobs/ ...
Found 100 job listing(s).
Saved 100 job(s) to 'jobs.csv'.

Preview (first 3 jobs):
  [Senior Python Developer] at Payne, Roberts and Davis — Stewartbury, AA
    https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
  [Energy engineer] at Vasquez-Davidson — Christopherville, AA
    https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html
  [Legal executive] at Jackson, Chambers and Levy — Port Ericaburgh, AA
    https://realpython.github.io/fake-jobs/jobs/legal-executive-2.html
```

## How It Works

1. **`fetch_page(url)`** — Sends a GET request with a browser-like `User-Agent` header (required for GitHub Pages) and returns a parsed BeautifulSoup object. Returns `None` on any network error.

2. **`extract_jobs(soup)`** — Finds every `div.card` on the page and pulls four fields from each using CSS selectors. Missing fields fall back to `"N/A"` instead of crashing.

3. **`save_to_csv(jobs, filename)`** — Writes the list of job dictionaries to a UTF-8 encoded CSV file with a header row.

4. **`main()`** — Orchestrates the three steps above and prints a short terminal preview.