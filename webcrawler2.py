from bs4 import BeautifulSoup
import requests

# Get featured article title from bdnews24.com sports page
page_url = "https://bdnews24.com/sport/"

r = requests.get(page_url)
soup = BeautifulSoup(r.text, 'html.parser')
featured_div = soup.select_one(".section_topstory")
featured_link = featured_div.find('a')
featured_headline = featured_link.string.strip()
print(featured_headline)
