import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nytimes.com")

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h2')

seen_titles = set()

for headline in headlines:
  title = headline.get_text(strip=True)

  if title and title not in seen_titles:
    seen_titles.add(title)
    print(title)


