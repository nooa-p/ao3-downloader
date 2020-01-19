import requests
from bs4 import BeautifulSoup

url = "https://archiveofourown.org/works/16571744/chapters/38830805"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.find(class_="title heading")
title = str(title)
stripped = title.strip('<h2 class="title heading">/').strip()
workid = url.strip('https://archiveofourown.org/works/').strip('/chapters/38830805')
finalurl = "https://archiveofourown.org/downloads/" + workid + "/" + stripped + ".html"

res = requests.get(finalurl)
playfile = open((stripped + '.html'), 'wb')
for chunk  in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()