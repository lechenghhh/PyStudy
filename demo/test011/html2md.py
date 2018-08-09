import urllib

# https://www.v2ex.com/amp/t/364078
import tkinter.filedialog
from tkinter import *

from tomd import Tomd  # 安装: pip install tomd

from demo.test002cgi.httpreq import getHtml


def save(filename, contents):  # 保存到文件方法
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


def setUrl():
    url
    root = Tk()
    root.title('请输入网址')
    root.geometry("300x200")
    root.withdraw()


def selectDir():
    root = Tk()
    root.withdraw()
    # file_path = 'D:\\'
    file_path = tkinter.filedialog.askdirectory()
    return file_path


url = 'https://baike.baidu.com/item/Python/407313'
# url = input("请输入要存储的网址: ")  # 输入获取网址
# if "http" not in url:
#     url = "http://" + url
html = getHtml(url)
md_data = Tomd(html).markdown
title = md_data[:20].replace('#', '').replace(' ', '').replace('\n', '')

# 路径选择
save(selectDir() + '\\' + "fff" + '.md', md_data)
