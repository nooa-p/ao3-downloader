import requests
import sys
import os.path
from bs4 import BeautifulSoup

# checks that the url is in correct form
def check_url(url):
    if not url.isnumeric():
        if not "archiveofourown.org/works/" in url:
            sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address has 'archiveofourown.org/works/' included in it""")
        if "https://www." in url:
            if len(url) == 38:
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'https://www.archiveofourown.org/works/[work_id]'""")
            if not url[38].isnumeric():
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'https://www.archiveofourown.org/works/[work_id]'""")
            else:
                return url
        if "https://" in url:
            if len(url) == 34:
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'https://archiveofourown.org/works/[work_id]'""")
            if not url[34].isnumeric():
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'https://archiveofourown.org/works/[work_id]'""")
            else:
                return url
        else:
            if len(url) == 26:
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'archiveofourown.org/works/[work_id]'""")
            if not url[26].isnumeric():
                sys.exit("""ERROR: INCORRECT ADDRESS
please make sure the address is in the form 'archiveofourown.org/works/[work_id]'""")
            else:
                return "https://" + url
    else:
        return "https://archiveofourown.org/works/" + url

# gets the download url from html code using beautifulsoup
def get_dl(url):
    r = requests.get(url)
    if r.status_code == 200:
        s = BeautifulSoup(r.text, 'html.parser')
        return str(s.find(class_="download").find("a", string="HTML")).strip('<a href=">HTML/')
    if r.status_code == 404:
        sys.exit("""ERROR: 404
there is a problem accessing the address you have given, please check that it's correct 
or that it hasn't been deleted. if you are using a .txt file to download multiple works,
please check that every address or id are on their own line""")
    if r.status_code == 445:
        sys.exit("""ERROR: 445
ao3 is currently experiencing heavy traffic, please wait a few minutes before trying again.
if this error keeps happening, check @AO3_Status on twitter for updates""")
    if r.status_code == 502:
        sys.exit("""ERROR: 502
ao3 is currently experiencing heavy traffic, please wait a few minutes before trying again.
if this error keeps happening, check @AO3_Status on twitter for updates""")
    if r.status_code == 503:
        sys.exit("""ERROR: 502
ao3 is currently experiencing heavy traffic, please wait a few minutes before trying again.
if this error keeps happening, check @AO3_Status on twitter for updates""")
    else:
        sys.exit("there was an unknown error, code: " + r.status_code)

# gets file name from download url
def get_name(url):
    url = url.lstrip('downloads/')
    i = 0
    while not url[i] == "/":
        i += 1
    url = url[i+1:]
    i = 0
    while not url[i] == "?":
        i += 1
    url = url[:i]
    if "%20" in url:
        url = url.replace('%20', ' ')
    return url

# saves the html file on disk
def download(url):
    url = get_dl(check_url(url))
    name = get_name(url)
    r = requests.get("https://archiveofourown.org/" + url)
    pf = open(name, 'wb')
    for chunk in r.iter_content(100000):
        pf.write(chunk)
    pf.close()

# download all works given in file
def download_multiple(file):
    r = open(file, 'r')
    for line in r:
        download(line)

if len(sys.argv) < 2:
    sys.exit('please provide work address or id')
    
download(sys.argv[-1])