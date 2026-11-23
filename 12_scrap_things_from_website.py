import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_books():
    base_url = "https://books.toscrape.com/"
    try:
        response = requests.get(
            base_url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("article.product_pod h3 a"):
        title = a.get("title")
        link = urljoin(base_url, a.get("href"))
        print(f"{title} | {link}")


scrape_books()
