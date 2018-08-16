import tkinter as tk
from tkinter import ttk

from demo.test012.opencv01 import showCameraWindow
from demo.test012.opencv02 import showCameraWindow2
from demo.test012.opencv03 import showCameraWindow3

win = tk.Tk()
win.title("Python OpenCV实践")  # 添加标题
win.minsize(240, 360)
aLabel = ttk.Label(win, text="Python OpenCV实践")  # 创建一个标签, text：显示标签的内容
aLabel.grid(column=1, row=0)


def btn1():  # 当acction被点击时,该函数则生效
    showCameraWindow()
    print("儿童模式启动")


def btn2():
    showCameraWindow2()
    print("老人模式启动")


def btn3():
    showCameraWindow3()
    print("防盗模式启动")


action = ttk.Button(win, text="儿童模式", command=btn1)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=1)

action = ttk.Button(win, text="老人模式", command=btn2)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=2)

action = ttk.Button(win, text="防盗模式", command=btn3)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=3)

win.mainloop()  # 当调用mainloop()时,窗口才会显示出来
