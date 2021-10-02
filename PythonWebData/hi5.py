from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Zen.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
for i in range (7):
    for count,tag in enumerate(tags):
        if count == 17:
            url = tag.get('href')
            html = urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup('a')
print(url.split('/')[-1].split('.')[0].split('_')[-1])