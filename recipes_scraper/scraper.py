import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.simplyrecipes.com/search?q=burger"
r = requests.get(URL)
print(r.ok)
# soup = bs(r.content,
#                      'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())