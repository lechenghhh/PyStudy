# coding=utf-8

# urllib模块提供了读取Web页面数据的接口
import urllib.request
# re模块主要包含了正则表达式
import re


# 定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()  # read()方法用于读取URL上的数据
    html = html.decode('utf-8')
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  # 正则表达式，得到图片地址
    imgre = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = imgre.findall(html)  # re.findall() 方法读取html 中包含 imgre(正则表达式)的数据
    # 把筛选的图片地址通过for循环遍历并保存到本地
    # 核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    print(imglist)

    for imgurl in imglist:
        print(imglist[x])
        urllib.request.urlretrieve(imgurl, 'D:\E\%s.jpg' % x)
        x += 1


html = getHtml(
    # "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1533953434295_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8"
    'https://www.douban.com/'
)
getImg(html)
