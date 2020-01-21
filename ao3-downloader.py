import requests
import sys
from bs4 import BeautifulSoup

def check_url():
    return


url = "https://archiveofourown.org/works/16571744/chapters/38830805"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
finalurl = str(soup.find(class_="download").find("a", string="HTML")).strip('<a href=">HTML/')

res = requests.get("https://archiveofourown.org/" + finalurl)
playfile = open(('testi.html'), 'wb')
for chunk  in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()