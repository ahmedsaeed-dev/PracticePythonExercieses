"""
https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
"""

import requests
from bs4 import BeautifulSoup


url = "https://www.serebii.net"
html = requests.get(url)
r_html = html.text
soup = BeautifulSoup(r_html, 'html.parser')

open_file = open('file_to_save.txt', 'w')

for x in soup.select('h2'):
    open_file.write(x.get_text() + '\n')

print('Ran successfully!')

