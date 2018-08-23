# -*- coding: utf-8 -*-
# Python3.7中安装openCV库:https://blog.csdn.net/Toby_Cho/article/details/81001382
# https://www.jb51.net/article/132480.htm
import cv2
import numpy as np
import time
from practice.app002.playsound import ring

spaceTime = 10  # 间隔时间设置为30秒


def showCameraWindow():
    selectXY = [(0, 0), (0, 0)]  # 选取框位置
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
    i = 0

    while True:

        grabbed, frame_lwpCV = camera.read()  # 读取视频流
        # 对帧进行预处理,先转灰度图,再进行高斯滤波.
        # 用高斯滤波进行模糊处理,进行处理的原因：每个输入的视频都会因自然震动、
        # 光照变化或者摄像头本身等原因而产生噪声.对噪声进行平滑是为了避免在运动和跟踪时将其检测出来.
        gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)
        i += 1

        if background is None:  # 将第一帧设置为整个输入的背景
            background = gray_lwpCV
            continue
        # 对于每个从背景之后读取的帧都会计算其与背景之间的差异,并得到一个差分图(different map).
        # 还需要应用阈值来得到一幅黑白图像,并通过下面代码来膨胀(dilate)图像,从而对孔(hole)和缺陷(imperfection)进行归一化处理
        diff = cv2.absdiff(background, gray_lwpCV)
        diff = cv2.threshold(diff, 48, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
        diff = cv2.dilate(diff, es, iterations=2)  # 形态学膨胀
        # 显示矩形框
        # 该函数计算一幅图像中目标的轮廓
        image, contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            cv2.rectangle(frame_lwpCV, selectXY[0], selectXY[1], (22, 22, 222), 2)  # 绘制选定区域
            # 对于矩形区域,只显示大于给定阈值的轮廓,所以一些微小的变化不会显示.
            # 对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
            if cv2.contourArea(c) < 1500:
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            xCenter = x + w / 2
            yCenter = y + h / 2
            # print(selectXY[0][0], selectXY[0][1], selectXY[1][0], selectXY[1][1], xCenter, yCenter)
            if selectXY[0][0] < xCenter and xCenter < selectXY[1][0] and \
                    selectXY[0][1] < yCenter and yCenter < selectXY[1][1]:
                cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (255, 0, 255), 2)
                if isRing:
                    visTiem = time.time()
                    isRing = False
                    print("小朋友跑到了指定区域-时间是:", visTiem)
                    ring()
                    # send("儿童报警", "小朋友跑到了指定区域！！")  # 发送邮件
            else:
                cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if time.time() - visTiem > spaceTime:  # 大于间隔时间spaceTime
                isRing = True
        if (i >= 20):
            if (i == 20):
                selectXY = get_rect(frame_lwpCV, title='Please Select Size')  # 鼠标画矩形框
                print(selectXY)
            cv2.imshow('contours', frame_lwpCV)
            cv2.imshow('dis', diff)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 按'q'健退出循环
            break

    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()


# 鼠标事件选择框
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
            cv2.rectangle(im_draw, mouse_params['tl'], mouse_params['current_pos'], (0, 0, 222))

        cv2.imshow(title, im_draw)
        _ = cv2.waitKey(10)

    cv2.destroyWindow(title)

    tl = (min(mouse_params['tl'][0], mouse_params['br'][0]),
          min(mouse_params['tl'][1], mouse_params['br'][1]))
    br = (max(mouse_params['tl'][0], mouse_params['br'][0]),
          max(mouse_params['tl'][1], mouse_params['br'][1]))

    return (tl, br)  # tl=(y1,x1), br=(y2,x2)


if __name__ == '__main__':
    showCameraWindow()
