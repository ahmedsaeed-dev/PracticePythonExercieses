"""
https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
Use the BeautifulSoup4 and requests Python packages to print out a list of all <h2> titles on a page of your choice.
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.serebii.net"
html = requests.get(url)
r_html = html.text
soup = BeautifulSoup(r_html, 'html.parser')


for x in soup.select('h2'):
    print(x.get_text())