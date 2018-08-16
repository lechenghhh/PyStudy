# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:32:02 2016

@author: http://blog.csdn.net/lql0716
# 教程地址：https://blog.csdn.net/lql0716/article/details/54174293
"""
import cv2
import numpy as np
import tkinter.filedialog
from tkinter import *


# current_pos = None
# tl = None
# br = None


# 鼠标事件
def get_rect(im, title='请选择指定区域大小'):  # (a,b) = get_rect(im, title='get_rect')
    mouse_params = {'tl': None, 'br': None, 'current_pos': None,
                    'released_once': False}

    cv2.namedWindow(title)
    cv2.moveWindow(title, 100, 100)

    def onMouse(event, x, y, flags, param):

        param['current_pos'] = (x, y)

        if param['tl'] is not None and not (flags & cv2.EVENT_FLAG_LBUTTON):
            param['released_once'] = True

        if flags & cv2.EVENT_FLAG_LBUTTON:
            if param['tl'] is None:
                param['tl'] = param['current_pos']
            elif param['released_once']:
                param['br'] = param['current_pos']

    cv2.setMouseCallback(title, onMouse, mouse_params)
    cv2.imshow(title, im)

    while mouse_params['br'] is None:
        im_draw = np.copy(im)

        if mouse_params['tl'] is not None:
            cv2.rectangle(im_draw, mouse_params['tl'], mouse_params['current_pos'], (255, 0, 0))

        cv2.imshow(title, im_draw)
        _ = cv2.waitKey(10)

    cv2.destroyWindow(title)

    tl = (min(mouse_params['tl'][0], mouse_params['br'][0]),
          min(mouse_params['tl'][1], mouse_params['br'][1]))
    br = (max(mouse_params['tl'][0], mouse_params['br'][0]),
          max(mouse_params['tl'][1], mouse_params['br'][1]))

    return (tl, br)  # tl=(y1,x1), br=(y2,x2)


# 读取摄像头/视频,然后用鼠标事件画框
def readVideo(skipFrame):  # pathName为视频文件路径,skipFrame为视频的第skipFrame帧
    selectXY = [(0, 0), (0, 0)]

    camera = cv2.VideoCapture(0)  # 读取摄像头
    if not camera.isOpened():  # 如果为发现摄像头,则按照路径pathName读取视频文件
        camera = cv2.VideoCapture(selectDir())  # 读取视频文件,如pathName='D:/test/test.mp4'
    c = 1

    while (camera.isOpened()):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(frame, selectXY[0], selectXY[1], (0, 255, 0), 2)
        if (c >= 20):
            mask = np.zeros(gray.shape, dtype=np.uint8)  # 掩码操作,该矩阵与图片大小类型一致,为初始化全0像素值,之后对其操作区域赋值为1即可
            if (c == skipFrame):
                selectXY = get_rect(frame, title='get_rect')  # 鼠标画矩形框
                print(selectXY)
                img01, img02 = frame, frame
                gray01, gray02 = gray, gray
            else:
                img1, img2 = prev_frame, frame
                gray1, gray2 = prev_frame, frame
            cv2.imshow('frame', frame)
            print(selectXY[0], "---", selectXY[1])
        c = c + 1
        prev_gray = gray
        prev_frame = frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 点击视频窗口,按q键退出
            break
    camera.release()
    cv2.destroyAllwindows()


def selectDir():
    root = Tk()
    root.withdraw()
    # file_path = 'D:\\'
    file_path = tkinter.filedialog.askdirectory()
    return file_path


if __name__ == '__main__':
    readVideo(20)
