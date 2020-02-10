from bs4 import BeautifulSoup
import requests

# Get most read article titles from bdnews24.com cricket page
page_url = "https://bdnews24.com/cricket/"

r = requests.get(page_url)
soup = BeautifulSoup(r.text, 'html.parser')
mostread_div = soup.select_one(".mostRead")
article_links = mostread_div.find_all('a')
print("Most read articles")
print("------------------")
for link in article_links:
    print(link.string.strip())
