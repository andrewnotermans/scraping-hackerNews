# Hacker News Scraper

This project is a Python script that scrapes Hacker News for the latest stories and sorts them by the number of votes. It utilizes the `requests` library to fetch the HTML content of Hacker News pages and the `BeautifulSoup` library from `bs4` for parsing the HTML.

## Features

- Scrapes multiple pages of Hacker News.
- Extracts story titles, links, IDs, and vote counts.
- Sorts stories by the number of votes in descending order.
- Handles potential errors gracefully, ensuring robust operation.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/andrewnotermans/scrape-1.git
   
