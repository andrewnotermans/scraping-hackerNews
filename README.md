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

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4

## Usage
Run the script to scrape Hacker News and display the top stories sorted by votes:
      ```bash
      python3 scrape-1.py

## Code Explanation


### Function Definitions

*   get\_soup(url): Fetches the HTML content of the given URL and returns a BeautifulSoup object.
    
*   sort\_stories\_by\_votes(hnlist): Sorts the list of stories by the number of votes in descending order.
    
*   create\_custom\_hn(links, ids, subtext): Creates a custom Hacker News list with story IDs, titles, links, and vote counts.
    

### Main Script

*   Initializes lists to store links, subtexts, and IDs from multiple pages.
    
*   Loops through the specified number of pages, scraping the required data.
    
*   Prints the lengths of the lists for debugging purposes.
    
*   Calls create\_custom\_hn to generate the sorted list of stories and prints it.
    

### Error Handling

*   The script includes error handling to manage potential IndexError occurrences during the list operations.
    

Example Output
--------------

The script will output the top stories with their IDs, titles, links, and vote counts, like so:
```bash
[
    {
        'id': 12345,
        'title': 'Example Story',
        'link': 'https://example.com/story',
        'votes': 150
    },
    ...
]

