# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

titles = soup.find_all("span", {"class": "", "aria-label": ""})
# print(titles)
for title in titles:
    print(title.string)
