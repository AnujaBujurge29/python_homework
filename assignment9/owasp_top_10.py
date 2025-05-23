from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import json

# Setup Selenium WebDriver with headless Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = "https://owasp.org/www-project-top-ten/"

driver.get(url)
time.sleep(3)  # wait for page to load fully

# Find the top 10 vulnerabilities
top_10_elements = driver.find_elements(By.XPATH, "//section//li/a")

results = []

for item in top_10_elements:
    title = item.text
    link = item.get_attribute("href")
    results.append({"Title": title, "Link": link})

df = pd.DataFrame(results)
print(df)
# Save to CSV
df.to_csv("owasp_top_10.csv", index=False)

# Task Write JSON - Optional
with open("owasp_top_10.json", "w") as f:
    json.dump(results, f, indent=2)

driver.quit()


print("\nSaved top 10 OWASP risks to python_homework/assignment9/owasp_top_10.csv")
