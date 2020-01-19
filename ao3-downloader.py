import requests

res = requests.get("https://archiveofourown.org/downloads/22247407/All My Angel Wants.html")
playfile = open('test.html', 'wb')
for chunk  in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()