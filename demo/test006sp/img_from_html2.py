# -*- coding: utf-8 -*-
# feimengjuan
import re
import urllib.request
import os


# 抓取网页图片
# https://blog.csdn.net/feimengjuan/article/details/51163803

# 根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    path2 = u'html'
    mkdir(path2)
    save(path2 + '\\' + 'index.html', html)
    return html


def save(filename, contents):  # 保存到文件方法
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


# 创建保存图片的文件夹
def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在    True
    # 不存在  Flase
    isExists = os.path.exists(path)
    if not isExists:
        # print(u'新建了名字叫做', path, u'的文件夹')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已经存在
        # print(u'名为', path, u'的文件夹已经创建成功')
        return False


# 输入文件名，保存多张图片
def saveImages(imglist, name):
    number = 1
    for imageURL in imglist:
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = 'jpg'
        fileName = name + "/" + str(number) + "." + fTail
        # 对于每张图片地址，进行保存
        try:
            if 'http' not in imageURL:
                imageURL = 'http:' + imageURL
            print(imageURL)
            u = urllib.request.urlopen(imageURL)
            data = u.read()
            f = open(fileName, 'wb+')
            f.write(data)
            print(u'正在保存的一张图片为', fileName)
            f.close()
        except urllib.request.URLError as e:
            print(e.reason)
        number += 1


# 获取网页中所有图片的地址
def getAllImg(html):
    # 利用正则表达式把源代码中的图片地址过滤出来
    # reg = r'src="(.+?\.jpg)" pic_ext'  # 贴吧规则
    reg = r'data-imgurl="(.+?\.jpg)" src'  # 百度图片规则
    # reg = r'src="(.+?\.jpg)" alt'  # CSDN博客
    # reg = r'src="(.+?\.jpg)">'  # 菜鸟

    imgre = re.compile(reg)
    imglist = imgre.findall(html)  # 表示在整个网页中过滤出所有图片的地址，放在imglist中
    return imglist


# 创建本地保存文件夹，并下载保存图片
if __name__ == '__main__':
    html = getHtml(
        # "https://tieba.baidu.com/p/2460150866?red_tag=1632632331&traceid="
        # "https://blog.csdn.net/feimengjuan/article/details/51163803"
        # "http://www.runoob.com/python3/python3-install.html"
        "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1533959253245_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%8B%8F35"
    )  # 获取该网址网页详细信息，得到的html就是网页的源代码
    path = u'img'
    mkdir(path)  # 创建本地文件夹
    imglist = getAllImg(html)  # 获取图片的地址列表
    saveImages(imglist, path)  # 保存图片
