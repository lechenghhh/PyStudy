'''
Created on 2017年8月31日
@author: Nick
'''

# _*_coding:utf-8_*_
import tkinter as tk
from tkinter import *
# from openpyxl.worksheet.properties import Outline
from _tkinter import create

'''
Tkinter教程之Canvas篇
'''


def test04():
    def eventPrint(event):
        print('eventPrint!')

    def printRect(event):
        print('rectangle')

    def printLine(event):
        print('line')

    # 提供可以用来进行绘图的Container，支持基本的几何元素，使用Canvas进行绘图时，所有的操作都是通过Canvas，不是通过它的元素
    # 元素的表示可以使用handle或tag。

    root = tk.Tk()

    root.wm_title('Canvas')  # 设置窗体标题
    root.wm_minsize(400, 400)  # 设置窗口最小化大小
    root.wm_maxsize(2800, 2800)  # 设置窗口最大化大小
    root.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

    # 2、创建一个Canvas，设置其背景色为白色,大小
    cv = Canvas(root, bg='white', width=100, height=80)
    cv.pack(side=TOP)

    fram = Frame(root)
    cv = Canvas(fram, bg='white', width=800, height=200)

    # 3、创建一个items,坐标为(10,10,110,110)，并填充颜色为红色
    cv.create_rectangle(10, 10, 110, 110, fill='red')

    # 4、指定矩形的边框颜色为绿色
    cv.create_rectangle(120, 10, 220, 110, outline='green')

    # 5、指定边框的宽度
    cv.create_rectangle(230, 10, 330, 110, outline='black', width=10)

    # 6、画虚线
    # 使用属性dash,这个值只能为奇数
    cv.create_rectangle(350, 10, 440, 110, outline='black', width=10, dash=3)

    # 7、使用画刷填充
    # 使用属性stipple
    cv.create_rectangle(460, 10, 550, 110, fill='red', outline='black', width=10, dash=3, stipple='gray12')

    # 8、修改item的坐标
    # 使用Canvas的方法coords(原item,坐标元组)来重新设置item的坐标
    # 重新设置rt的坐标（相当于移动一个item）
    rt = cv.create_rectangle(570, 10, 660, 110, fill='green', outline='black', width=5, dash=7, stipple='gray12')
    cv.coords(rt, (680, 10, 770, 110))

    # 9、创建item的tags
    # 使用属性tags设置item的tag
    # 使用Canvas的方法gettags获取指定item的tags
    ta = cv.create_rectangle(10, 120, 110, 220, fill='green', outline='black', width=5, dash=7, stipple='gray12',
                             tags='r1')
    print(cv.gettags(ta))

    # 使用tags属性指定多个tags,即重新设置tags的属性，通过itemconfig(原item,属性字段)函数修改item属性值
    cv.itemconfig(ta, tags=('r2', 'r3', 'r4', 'r5'))
    cv.gettags(ta)
    print(cv.gettags(ta))

    cv.pack(side=LEFT)
    fram.pack(side=TOP)

    fram_1 = Frame(root)
    cv = Canvas(fram_1, bg='white', width=800, height=100)

    # 10、多个item使用同一个tag
    cv.create_rectangle(10, 10, 110, 110, fill='red', tags=('r2', 'r3', 'r4', 'r5'))
    cv.create_rectangle(120, 10, 220, 110, fill='black', tags='r1')
    cv.create_rectangle(230, 10, 330, 110, fill='green', tags='r2')

    # fid_withtag返回所有与tag绑定的item。,返回的是item的序号元组，item编号从1开始
    cv.find_withtag('r2')
    print(cv.find_withtag('r2'))

    cv.pack(side=LEFT)
    fram_1.pack(side=TOP)

    # 11、通过tag来访问item
    # 得到了tag值也就得到了这个item，可以对这个item进行相关的设置。
    fram_2 = Frame(root)
    cv = Canvas(fram_2, bg='white', width=800, height=100)
    cv.create_rectangle(10, 10, 80, 80, fill='green', tags=('r2', 'r3', 'r4', 'r5'))
    cv.create_rectangle(90, 10, 160, 80, fill='black', tags='r1')
    cv.create_rectangle(170, 10, 240, 80, fill='red', tags='r3')

    # 将所有与tag('r3')绑定的item边框颜色设置为蓝色
    for item in cv.find_withtag('r3'):
        cv.itemconfig(item, outline='blue', width=3)

    cv.pack(side=LEFT)
    fram_2.pack(side=TOP)

    # 13、向其它item添加tag
    # 使用addtag_above、addtag_below来向上一个或下一个item添加tag
    # 第一个参数是tag值，第二个参数数需要修改的item
    fram_3 = Frame(root)
    cv = Canvas(fram_3, bg='white', width=800, height=100)
    tags_1 = cv.create_rectangle(10, 10, 80, 80, fill='green', tags=('r2', 'r3', 'r4', 'r5'))
    tags_2 = cv.create_rectangle(90, 10, 160, 80, fill='black', tags='r1')
    tags_3 = cv.create_rectangle(170, 10, 240, 80, fill='red', tags='r3')

    # 向tags_2的上一个item(tags_3)添加rt1
    cv.addtag_above('rt1', tags_2)
    # 向tags_2的下一个item(tags_1)添加rt11
    cv.addtag_below('rt11', 2)

    # Canvas使用了stack的技术，新创建的item总是位于前一个创建的item之上，故调用above时，它会查找rt2上面的item为rt3,故rt3中添加了tag('r4')，同样add_below会查找下面的item。

    for item in [tags_1, tags_2, tags_3]:
        print(cv.gettags(item))

    # 14、返回其它item
    # 使用find_above/find_below查找上一个或下一个item，并通过itemconfig()函数设置属性
    cv.itemconfig(cv.find_above(tags_2), dash=7, outline='blue', stipple='gray12')
    cv.itemconfig(cv.find_below(tags_2), dash=2, outline='black', stipple='gray12')
    # Canvas使用了stack的技术，新创建的item总是位于前一个创建的item之上，故调用above时，它会查找rt2上面的item为rt3,故rt3中添加了tag('r4')，同样add_below会查找下面的item。

    cv.pack(side=LEFT)
    fram_3.pack(side=TOP)

    # 16、移动item
    fram_4 = Frame(root)
    cv = Canvas(fram_4, bg='white', width=800, height=100)
    rt_1 = cv.create_rectangle(10, 10, 80, 80, fill='green')
    rt_2 = cv.create_rectangle(10, 10, 80, 80, fill='green')
    rt_3 = cv.create_rectangle(170, 10, 240, 80, fill='red', tags=('s1', 's2', 's3'))
    # move可以指定x,y在相对偏移量，可以为负值
    cv.move(rt_2, 80, 10)
    cv.itemconfig(rt_2, fill='red')

    # 17、删除item
    # delete删除给定的item

    # 使用id删除item
    cv.delete(1)
    # 使用item名称删除item
    cv.delete(rt_2)
    # 使用tag删除item
    cv.delete('s1')

    cv.pack(side=LEFT)
    fram_4.pack(side=TOP)

    # 18、缩放item
    # scale缩放item,计算公式:(coords - offset)*scale + offset
    # scale的参数为(self,xoffset,yoffset,xscale,yscale),self可以是item的名称、id以及tag属性

    fram_5 = Frame(root)
    cv = Canvas(fram_5, bg='white', width=800, height=100)
    sf = cv.create_rectangle(10, 10, 80, 80, fill='green')
    sf_1 = cv.create_rectangle(90, 10, 160, 80, fill='green', tags='r1')

    # 将y坐标放大为原来的2位，x坐标值不变
    cv.scale(sf_1, 0, 0, 1, 2)
    # 等价于
    # cv.scale(2,0,0,1,2)
    # cv.scale('r1',0,0,1,2)

    # 19、绑定item与event
    ev_1 = cv.create_rectangle(170, 10, 240, 80, fill='blue', tags='r1')
    ev_2 = cv.create_rectangle(250, 10, 320, 80, fill='black', tags='r2')
    ev_3 = cv.create_rectangle(330, 10, 400, 80, fill='red', tags='r3')

    # 使用tag_bind来绑定item与事件,tag_bind(tagOrId, sequence, func, add)
    # tagOrId可以是item名称、tag属性值，
    # 只有点击到矩形的边框时才会触发事件,不使用add参数，默认就是向这个item添加一个处理函数，它不会替换原来的事件函数，例子结果：既响应左键又响应右键
    # 只有点击到矩形的边框时才会触发事件
    cv.tag_bind(ev_1, '<Button-1>', eventPrint)
    cv.tag_bind('r2', '<Button-1>', eventPrint)

    # 绑定item与左键事件
    cv.tag_bind('r3', '<Button-1>', printRect)
    # 绑定item与右键事件
    cv.tag_bind('r3', '<Button-3>', printLine)

    # 将事件与tag('r1')绑定后，创建新的item并指定已绑定事件的tag,新创建的item同样也与事件绑定，
    ev_3 = cv.create_rectangle(330, 10, 400, 80, fill='green', tags='r3')

    cv.pack(side=LEFT)
    fram_5.pack(side=TOP)

    # 20、绘制弧形
    fram_6 = Frame(root)
    cv = Canvas(fram_6, bg='white', width=800, height=50)
    # 使用默认参数创建一个ARC，结果为90度，填充色为红色的扇形
    cv.create_arc(10, 10, 80, 80, fill='red')

    # 21、设置弧形的样式
    # 使用三种样式，分别创建了扇形、弓形和弧形
    d = {1: PIESLICE, 2: CHORD, 3: ARC}
    for i in d:
        cv.create_arc((10 + 80 * i, 10, 80 + 80 * i, 80), style=d[i], fill='blue', outline='black', width=5, dash=7)
        print(str(i) + d[i])

    cv.pack(side=LEFT)
    fram_6.pack(side=TOP)

    fram_7 = Frame(root)
    cv = Canvas(fram_7, bg='white', width=800, height=50)
    # 22、设置弧形的角度
    # 使用三种样式，start指定起始角度；extent指定角度偏移
    for i in d:
        cv.create_arc((10 + 80 * i, 10, 80 + 80 * i, 80), style=d[i], start=30, extent=30)
        print(str(i) + d[i])

    cv.pack(side=LEFT)
    fram_7.pack(side=TOP)

    # 23、绘制位图
    # 使用bitmap创建位图create_bitmap
    # 使用bitmap属性来指定位图的名称，这个函数的第一个参数为一个点(x,y)指定位图存放位置的左上位置。
    fram_8 = Frame(root)
    cv = Canvas(fram_8, bg='white', width=800, height=100)
    d = {1: 'error', 2: 'info', 3: 'question', 4: 'hourglass'}
    for i in d:
        cv.create_bitmap((20 * i, 20 * i), bitmap=d[i])

    cv.pack(side=LEFT)
    fram_8.pack(side=TOP)

    root.mainloop()

    # 创建第二个根窗口
    root_1 = tk.Tk()

    root_1.wm_title('Canvas-one')  # 设置窗体标题
    root_1.wm_minsize(400, 400)  # 设置窗口最小化大小
    root_1.wm_maxsize(2800, 2800)  # 设置窗口最大化大小
    root_1.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

    # 24、绘制GIF图像
    # 创建gif图像create_image
    # 先使用PhotoImage创建GIF图像，再将image属性来设置为新创建的img
    fram_9 = Frame(root_1)
    cv = Canvas(fram_9, bg='white', width=800, height=160)
    img = PhotoImage(file='C:\\Users\\Nick\\Desktop\\1.gif')
    cv.create_image((150, 150), image=img)

    cv.pack(side=LEFT)
    fram_9.pack(side=TOP)

    # 25、绘制直线
    # 创建带箭头的直线create_line
    # 使用arrow属性来控制是否显示箭头
    # 将直线的属性joinstyle分别设置为bevel/miter/round，测试其效果。
    fram_10 = Frame(root_1)
    cv = Canvas(fram_10, bg='white', width=800, height=160)
    d = [(0, 'none', 'bevel'), (1, 'first', 'miter'), (2, 'last', 'round'), (3, 'both', 'round')]
    for i in d:
        cv.create_line(
            (10, 10 + i[0] * 20, 110, 110 + i[0] * 20),  # 设置直线的起始、终点
            arrow=i[1],  # 设置直线是否使用箭头
            arrowshape='40 40 10'  # 设置箭头的形状(填充长度，箭头长度，箭头宽度

        )
    for i in d:
        cv.create_line(
            (130, 10 + i[0] * 30, 220, 110 + i[0] * 30),  # 设置直线的起始、终点
            arrow=i[1],  # 设置直线是否使用箭头
            arrowshape='40 40 10',  # 设置箭头的形状(填充长度，箭头长度，箭头宽度
            joinstyle=i[2],
        )
    cv.pack(side=LEFT)
    fram_10.pack(side=TOP)

    # 26、绘制椭圆
    # 绘制椭圆，使用create_oval属性

    fram_11 = Frame(root_1)
    cv = Canvas(fram_11, bg='white', width=800, height=100)
    # 创建一个长200，宽100的椭圆
    cv.create_oval((10, 10, 210, 110), fill='red')

    cv.pack(side=LEFT)
    fram_11.pack(side=TOP)

    # 27、创建多边形
    # 创建多边形（三角形）,使用create_polygon
    fram_12 = Frame(root_1)
    cv = Canvas(fram_12, bg='white', width=800, height=160)
    # 创建一个直角三角形
    # 指定三个点的坐标，三个点坐标必须满足三角形的定义。
    cv.create_polygon((10, 10, 10, 200, 100, 200), fill='blue')
    # 创建四边形
    cv.create_polygon((200, 10, 10, 100, 80, 200, 200, 200), fill='blue')
    cv.move(2, 80, 10)

    cv.pack(side=LEFT)
    fram_12.pack(side=TOP)

    # 28、修饰图形
    # 创建多边形create_ploygon（三角形）
    # smooth/splinesteps用来修改绘制的图形,不明白这两个参数还有其它什么作用。
    fram_13 = Frame(root_1)
    cv = Canvas(fram_13, bg='white', width=800, height=100)
    # 创建一个直角三角形
    cv.create_polygon((10, 10, 10, 100, 50, 100),
                      smooth=True,  # 平滑处理，但未找到控制此参数的项
                      splinesteps=0,  # 不明白是控制什么的？？？
                      )
    cv.pack(side=LEFT)
    fram_13.pack(side=TOP)

    # 29、绘制文字
    fram_14 = Frame(root_1)
    cv = Canvas(fram_14, bg='white', width=800, height=100)
    # 创建一个文字对象，默认设置为居中对齐
    # 使用anchor控制文字的位置，使用justify控制对齐方式
    cv.create_text((10, 10), text='Hello Text,居中', anchor=W, fill='blue')
    cv.create_text((20, 20), text='Hello Text,居左', anchor=W, fill='blue', justify=LEFT)
    cv.create_text((30, 30), text='Hello Text,居右', anchor=W, fill='blue', justify=RIGHT)
    cv.pack(side=LEFT)
    fram_14.pack(side=TOP)

    # 30、选中文字
    # 使用anchor组件在Canvas上的位置，默认情况下为居中对齐,这样使用后其它的item将不能再使用button战胜的那块区域
    fram_15 = Frame(root_1)
    cv = Canvas(fram_15, bg='white', width=800, height=100)
    # 创建一个文字对象，默认设置为居中对齐
    # 使用anchor控制文字的位置，使用justify控制对齐方式
    txt = cv.create_text((10, 10), text='Hello Text', anchor=W)
    # 设置文本的选中起始位置
    cv.select_from(txt, 2)
    # 设置文本的选中结束位置
    cv.select_to(txt, 5)

    cv.pack(side=LEFT)
    fram_15.pack(side=TOP)

    # 31、创建组件
    fram_16 = Frame(root_1)
    cv = Canvas(fram_16, bg='white', width=800, height=100)

    # 创建一个Button对象，默认设置为居中对齐
    def printWindow():
        print('window')

    bt = Button(cv, text='ClickMe', command=printWindow)
    # 修改button在canvas上的对齐方式
    cv.create_window((10, 10), window=bt, anchor=W)
    # 新创建的line对象与button有重叠
    cv.create_line(10, 10, 20, 20)
    # 新创建的line不在button之上，即没有重叠
    cv.create_line(30, 30, 100, 100)

    cv.pack(side=LEFT)
    fram_16.pack(side=TOP)

    root_1.mainloop()


if __name__ == '__main__':
    test04()
