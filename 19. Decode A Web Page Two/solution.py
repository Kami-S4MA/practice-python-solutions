import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

for page_num in range(1, 5):
  
  if page_num == 1:
    url = base_url
  else:
    url = base_url+"/"+str(page_num)
  
  r = requests.get(url, headers=headers)
  
  soup = BeautifulSoup(r.text, 'html.parser')
  
  print("\nPAGE",page_num,"\n")
  
  all_paragraphs = soup.find_all('p')
  
  for i in all_paragraphs:
    text = i.text.strip()
    if len(text) > 40:
      print(text)
      print()