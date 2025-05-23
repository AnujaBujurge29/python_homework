# Task 2: Understanding HTML and the DOM for the Durham Library Site

# | Element                 | Tag  | Class                   |
# | ----------------------- | ---- | ----------------------- |
# | Search result container | li   | cp-search-result-item   |
# | Title                   | a    | cp-title-link           |
# | Author(s)               | a    | cp-author-link          |
# | Format & Year container | div  | cp-format-info          |


# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(url)
time.sleep(2)
# 9.3.3: Find all <li> elements that are search result items
search_results = driver.find_elements(
    By.CSS_SELECTOR, "li.cp-search-result-item")

# print(f"Found {(search_results)} search result items.")

# 9.3.4 empty list Result
results = []

# 9.3.5 Main loop through the search result items
for item in search_results:
    try:
        # Get the title
        title_element = item.find_element(
            By.CSS_SELECTOR, "h2.cp-title a span.title-content")
        title = title_element.text.strip()
        # print(f"  Title: {title_element}")

        # # Get all authors (may be more than one)
        author_elements = item.find_elements(
            By.CSS_SELECTOR, "span.cp-author-link span a")
        authors = "; ".join([a.text.strip() for a in author_elements])

        # # Get the format and year
        format_and_year_el = item.find_element(
            By.CSS_SELECTOR, "span.display-info-primary"
        )
        format_and_year = format_and_year_el.text.strip()

        # Create dict and append
        book_data = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_and_year
        }
        results.append(book_data)

    except Exception as e:
        print(f"Skipping item due to error: {e}")

# 9.3.6: Create and print the DataFrame
df = pd.DataFrame(results)
print(df)


# Task 4.1: Write out the Data
df.to_csv("get_books.csv", index=False)
print("Data written to CSV")

# Task 4.2:Write JSON
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=2)
