import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_1367092.json'
url = urllib.request.urlopen(address, context=ctx)
data = url.read()


info = json.loads(data)
results = 0
for item in info['comments']:
    results = results + int(item['count'])
print(results)