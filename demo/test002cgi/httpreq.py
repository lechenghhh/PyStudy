import urllib.request
import urllib.parse


# 模块命名时不要与现有模块名冲突

def getHtml(url):
    if url is "":
        url = 'http://www.baidu.com'
    f = urllib.request.urlopen(url)
    html = f.read().decode('utf-8')
    # print(html)
    return html


print(getHtml('http://www.baidu.com'))
