import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.status_code)

# Extracting quotes
quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text)