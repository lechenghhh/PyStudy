import tkinter as tk
from tkinter import ttk

from demo.test005tkinter.gui6 import showSelectXY
from demo.test009canvas.test03canvas import CanvasDemo

win = tk.Tk()
win.title("Python OpenCV实践")  # 添加标题
win.minsize(240, 360)
aLabel = ttk.Label(win, text="Python OpenCV实践")  # 创建一个标签, text：显示标签的内容
aLabel.grid(column=1, row=0)


def btn1():  # 当acction被点击时,该函数则生效
    print("test04")


def btn2():
    CanvasDemo()
    print("CanvasDemo")


def btn3():
    showSelectXY()
    print("showSelectXY")


action = ttk.Button(win, text="test04", command=btn1)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=1)

action = ttk.Button(win, text="CanvasDemo", command=btn2)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=2)

action = ttk.Button(win, text="showSelectXY", command=btn3)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=3)
aLabel = ttk.Label(win, text="进入任意模式后，按 \'q\' 键返回")  # 创建一个标签, text：显示标签的内容
aLabel.grid(column=1, row=4)
win.mainloop()  # 当调用mainloop()时,窗口才会显示出来
