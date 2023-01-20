import requests
from bs4 import BeautifulSoup

company_name = "Google"
url = f"https://www.example.com/search?q={company_name}"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

articles = soup.find_all("article")
for article in articles:
    headline = article.find("h2").get_text()
    summary = article.find("p").get_text()
    print(f"{headline}\n{summary}\n")
