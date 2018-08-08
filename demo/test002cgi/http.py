import urllib.request


def getHtml(url):
    if url is "":
        url = 'http://118.24.152.88/JPA/'
    f = urllib.request.urlopen(url)
    html = f.read().decode('utf-8')
    print(html)
    return html


getHtml('http://www.baidu.com')
