import requests
from bs4 import BeautifulSoup

URL = "https://ridmik.news/latest"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

news_container = soup.find(id="__next")

# Find all news items by looking for the div with class "title"
latest_news_elements = news_container.find_all("div", class_="title")

for title_element in latest_news_elements:
    title_text = title_element.find("a").get_text(strip=True)
    
    # Find the summary element. Assuming it is a sibling of the title div
    summary_element = title_element.find_next_sibling("div", class_="summary")
    summary_text = summary_element.get_text(strip=True) if summary_element else 'No summary available'
    
    print(title_text)
    print(summary_text)
    print()
