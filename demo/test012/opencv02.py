# -*- coding: utf-8 -*-
# Python3.7中安装openCV库:https://blog.csdn.net/Toby_Cho/article/details/81001382
# https://www.jb51.net/article/132480.htm
import cv2
import numpy as np
import winsound
import time

from demo.test012.playsound import ring
from demo.test012.sendemail import send

spaceTime = 10  # 间隔时间设置为30秒
scale = 1.5  # 高度与宽度的比例，用以控制摔倒的判定界限


def showCameraWindow2():
    visTiem = time.time()
    isRing = False

    camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
    if (camera.isOpened()):  # 判断视频是否打开
        print('摄像头已打开')
    else:
        print('摄像头未打开')

    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('size:' + repr(size))

    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))
    kernel = np.ones((5, 5), np.uint8)
    background = None

    while True:
        grabbed, frame_lwpCV = camera.read()  # 读取视频流
        # 对帧进行预处理,先转灰度图,再进行高斯滤波.
        # 用高斯滤波进行模糊处理,进行处理的原因：每个输入的视频都会因自然震动、
        # 光照变化或者摄像头本身等原因而产生噪声.对噪声进行平滑是为了避免在运动和跟踪时将其检测出来.
        gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

        if background is None:  # 将第一帧设置为整个输入的背景
            background = gray_lwpCV
            continue
        # 对于每个从背景之后读取的帧都会计算其与背景之间的差异,并得到一个差分图(different map).
        # 还需要应用阈值来得到一幅黑白图像,并通过下面代码来膨胀(dilate)图像,从而对孔(hole)和缺陷(imperfection)进行归一化处理
        diff = cv2.absdiff(background, gray_lwpCV)
        diff = cv2.threshold(diff, 148, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
        diff = cv2.dilate(diff, es, iterations=2)  # 形态学膨胀
        # 显示矩形框
        # 该函数计算一幅图像中目标的轮廓
        image, contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            # 对于矩形区域,只显示大于给定阈值的轮廓,所以一些微小的变化不会显示.
            # 对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
            if cv2.contourArea(c) < 1500:
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if h * scale < w:  # 进行比例判断，如果宽比高大，说明目标躺下了
                print("目标疑似躺下了！", "w=", w, "h=", h)
                if isRing:
                    visTiem = time.time()
                    isRing = False
                    print("报警:", visTiem)
                    ring()
                    # send("摔倒报警", "老人摔倒了！")  # 发送邮件

        cv2.imshow('contours', frame_lwpCV)
        cv2.imshow('dis', diff)

        if time.time() - visTiem > spaceTime:  # 大于间隔时间spaceTime
            isRing = True
        # print(time.time(), visTiem)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 按'q'健退出循环
            break

    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    showCameraWindow2()
