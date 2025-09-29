import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes and authors
quotes = soup.find_all("div", class_="quote")

for idx, quote in enumerate(quotes, start=1):
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"{idx}. {text} — {author}")