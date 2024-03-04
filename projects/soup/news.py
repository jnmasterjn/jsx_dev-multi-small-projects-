#import nessassary tools for web scraping

import requests
from bs4 import BeautifulSoup 

url = "https://techcrunch.com/category/artificial-intelligence/"

response = requests.get(url)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser') #html parser is a python built-in that help parse 解析 html 
# print(soup.prettify())
# print(soup.text.strip())

#identifying and extracting headlines
''' 
articles = soup.find_all('h2')
for article in articles:
        print(article.text.strip())

with open('headlines.txt', 'w') as file:
    for link in links:
        file.write(f"{link.text.strip()}")
''' 

filename = "ai_headlines,march3rd"

with open (filename,'w', encoding= 'utf-8') as file:
    articles = soup.find_all('h2')
    for article in articles:
        file.write(article.text.strip()+ '\n') 

print(f"Headlines saved to {filename}")