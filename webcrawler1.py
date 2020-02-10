from bs4 import BeautifulSoup
import requests

page_url = "https://www.prothomalo.com/"

r = requests.get(page_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.string)