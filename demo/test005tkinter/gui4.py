from tkinter import *
import tkinter.filedialog

root = Tk()


def selectDir():
    # filenames = tkinter.filedialog.askopenfilenames()  # 文件名字
    filenames = tkinter.filedialog.askdirectory()  # 文件夹名字
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            string_filename += str(filenames[i]) + "\n"
        lb.config(text="您选择的文件是：" + string_filename)
        print("您选择的文件是：" + string_filename)
    else:
        lb.config(text="您没有选择任何文件")


lb = Label(root, text='')
lb.pack()
btn = Button(root, text="弹出选择文件夹对话框", command=selectDir)
btn.pack()
root.mainloop()
