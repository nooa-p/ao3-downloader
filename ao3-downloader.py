import requests
import sys
from bs4 import BeautifulSoup

# checks that the url is in correct form
def check_url(url):
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

# gets the download url from html code using beautifulsoup
def get_dl(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    return str(s.find(class_="download").find("a", string="HTML")).strip('<a href=">HTML/')

# saves the html file on disk
def download(url):
    url = get_dl(check_url(url))
    r = requests.get("https://archiveofourown.org/" + url)
    pf = open(('testi.html'), 'wb')
    for chunk in r.iter_content(100000):
        pf.write(chunk)
    pf.close()