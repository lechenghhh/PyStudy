import tkinter as Tkinter  # 导入TKinter模块

result = ""


def getUrl():
    ing = True
    ytm = Tkinter.Tk()  # 创建Tk对象
    ytm.title("login")  # 设置窗口标题
    ytm.geometry("300x300")  # 设置窗口尺寸
    l1 = Tkinter.Label(ytm, text="用户名")  # 标签
    l1.pack()  # 指定包管理器放置组件
    user_text = Tkinter.Entry()  # 创建文本框
    user_text.pack()

    def getText():
        result = user_text.get()  # 获取文本框内容
        print("getText=" + result)
        return result

    Tkinter.Button(ytm, text="登录", command=getText).pack()  # command绑定获取文本框内容方法
    ytm.mainloop()  # 进入主循环
    return getText()


getUrl()


# from tkinter import *
# import tkinter.filedialog
#
#
# def getuser():
#     ytm = Tk()  # 创建Tk对象
#
#     ytm.title("login")  # 设置窗口标题
#     ytm.geometry("300x300")  # 设置窗口尺寸
#     l1 = Tk.Label(ytm, text="用户名")  # 标签
#     l1.pack()  # 指定包管理器放置组件
#     user_text = Tk.Entry()  # 创建文本框
#     user_text.pack()
#     user = user_text.get()  # 获取文本框内容
#     return user
#
#
