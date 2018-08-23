# coding:utf-8
# 安装 PIL指令：pip install Pillow
from PIL import Image
import tkinter
import tkinter.filedialog
from demo.test09pillow.selectImg import selectFile

# 要索引的字符列表

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
file_path = selectFile()
print(file_path)
img = Image.open(file_path)  # 读取图像文件
(width, height) = img.size
img = img.resize((int(width * 0.2), int(height * 0.2)))  # 对图像进行一定缩小
print(img.size)


def convert(img):
    img = img.convert("L")  # 转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))  # 获取每个坐标像素点的灰度
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt


def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r, g, b = img.getpixel((j, i))  # 获取每个坐标像素点的rgb值
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)  # 通过灰度转换公式获取灰度
            unit = (256.0 + 1) / length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt


txt = convert(img)
print(txt)
f = open("output.txt", "w")
f.write(txt)  # 存储到文件中
f.close()
