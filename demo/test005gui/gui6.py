"""
@Author: 舍名利
@Blog  : www.cnblogs.com/shemingli
@GitHub: github.com/GratefulHeartCoder
@Date  : 2018/4/2
"""
from tkinter import *
from tkinter import ttk
import cv2

from demo.test012.opencv01 import showCameraWindow

start = [0, 0];
end = [0, 0]
index = True


def call_back_left(event):
    print("相对于应用程序左上角的位置,左键点击的位置是", event.x, event.y)
    # print("相对于屏幕左上角的位置,左键点击的位置是", event.x_root, event.y_root)
    global index
    if index:
        start[0] = event.x
        start[1] = event.y
    else:
        end[0] = event.x
        end[1] = event.y
    index = not index


def btn1():
    print(start, end)
    # showCameraWindow(start[0], start[1], end[0], end[1])


def showSelectXY():
    root = Tk()

    root.title("请用鼠标选择监控报警范围")  # 添加标题
    camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头

    # 创建一个框架，在这个框架中响应事件
    frame = Frame(root, width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                  bg='yellow')
    camera.release()

    # bind进行绑定  Button指的是鼠标的点击事件
    # 事件本身 - 事件的详细描述
    # 1 左键
    # 3 右键
    frame.bind("<Button-1>", call_back_left)
    # frame.bind("<Button-3>", call_back_right)
    frame.pack()

    action = ttk.Button(root, text="选好了，进入监控画面", command=btn1)
    action.pack()
    mainloop()


if __name__ == '__main__':
    showSelectXY()
