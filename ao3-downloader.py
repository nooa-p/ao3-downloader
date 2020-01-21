import requests
import sys
from bs4 import BeautifulSoup

def check_url(url):
    if not "archiveofourown.org/works/" in url:
        sys.exit("error: incorrect url type / not ao3 link")
    if "https://www." in url:
        if len(url) == 38:
            sys.exit("error: incorrect url type / too short no id(httpswww)")
        if not url[38].isnumeric():
            sys.exit("error: incorrect url type / no id")
        else:
            return url
    if "https://" in url:
        if len(url) == 34:
            sys.exit("error: incorrect url type / too short no id(https)")
        if not url[34].isnumeric():
            sys.exit("error: incorrect url type / no id")
        else:
            return url
    else:
        if len(url) == 26:
            sys.exit("error: incorrect url type / too short no id(nothing)")
        if not url[26].isnumeric():
            sys.exit("error: incorrect url type / no id")
        else:
            return "https://" + url


#url = "https://archiveofourown.org/works/23"

#print(check_url(url))

#res = requests.get(url)
#soup = BeautifulSoup(res.text, 'html.parser')
#finalurl = str(soup.find(class_="download").find("a", string="HTML")).strip('<a href=">HTML/')

#res = requests.get("https://archiveofourown.org/" + finalurl)
#playfile = open(('testi.html'), 'wb')
#for chunk  in res.iter_content(100000):
#    playfile.write(chunk)
#playfile.close()