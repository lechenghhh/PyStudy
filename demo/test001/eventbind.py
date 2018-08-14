"""
@Author: 舍名利
@Blog  : www.cnblogs.com/shemingli
@GitHub: github.com/GratefulHeartCoder
@Date  : 2018/4/2
"""
from tkinter import *


def call_back_left(event):
    print("相对于应用程序左上角的位置,左键点击的位置是", event.x, event.y)
    print("相对于屏幕左上角的位置,左键点击的位置是", event.x_root, event.y_root)


def call_back_right(event):
    print("右键点击的位置是", event.x, event.y)
    print("右键点击的位置是", event.x_root, event.y_root)


def main():
    root = Tk()

    # 创建一个框架，在这个框架中响应事件
    frame = Frame(root, width=200, height=200)

    # bind进行绑定  Button指的是鼠标的点击事件
    # 事件本身 - 事件的详细描述
    # 1 左键
    # 3 右键
    frame.bind("<Button-1>", call_back_left)
    frame.bind("<Button-3>", call_back_right)
    frame.pack()

    mainloop()


if __name__ == '__main__':
    main()