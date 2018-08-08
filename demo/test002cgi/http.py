import urllib.request
import urllib.parse

url = 'http://118.24.152.88/JPA/'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
