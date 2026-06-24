"""
Fake Python Jobs Scraper
Scrapes job listings from https://realpython.github.io/fake-jobs/
and saves results to a CSV file.
"""

import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetch a webpage and return a BeautifulSoup object, or None on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_jobs(soup: BeautifulSoup) -> list[dict]:
    """Extract job listings from a parsed page."""
    jobs = []

    job_cards = soup.select("div.card")
    if not job_cards:
        print("No job cards found on page.")
        return jobs

    for card in job_cards:
        title = card.select_one("h2.title")
        company = card.select_one("h3.company")
        location = card.select_one("p.location")
        link_tag = card.select_one("a[href]")

        # Build a clean record, substituting "N/A" for any missing field
        job = {
            "title": title.get_text(strip=True) if title else "N/A",
            "company": company.get_text(strip=True) if company else "N/A",
            "location": location.get_text(strip=True) if location else "N/A",
            "url": link_tag["href"] if link_tag else "N/A",
        }
        jobs.append(job)

    return jobs


def save_to_csv(jobs: list[dict], filename: str = "jobs.csv") -> None:
    """Write a list of job dicts to a CSV file."""
    if not jobs:
        print("No jobs to save.")
        return

    fieldnames = ["title", "company", "location", "url"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Saved {len(jobs)} job(s) to '{filename}'.")


def main() -> None:
    print(f"Fetching jobs from {BASE_URL} ...")
    soup = fetch_page(BASE_URL)
    if soup is None:
        print("Aborting: could not load the page.")
        return

    jobs = extract_jobs(soup)
    print(f"Found {len(jobs)} job listing(s).")

    if jobs:
        save_to_csv(jobs, "jobs.csv")
        # Preview first 3 results
        print("\nPreview (first 3 jobs):")
        for job in jobs[:3]:
            print(f"  [{job['title']}] at {job['company']} — {job['location']}")
            print(f"    {job['url']}")


if __name__ == "__main__":
    main()