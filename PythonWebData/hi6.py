import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = 'http://py4e-data.dr-chuck.net/comments_1367091.xml'
#address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = urllib.request.urlopen(address, context=ctx)
data = url.read()
tree = ET.fromstring(data)
results = tree.findall('.//count')
result = 0
for i in results:
    result = result+int(i.text)
print(result)