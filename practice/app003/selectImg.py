import tkinter
import tkinter.filedialog


def selectFile():  # 选择文件
    root = tkinter.Tk()
    root.withdraw()
    # file_path = 'D:\\'
    file_path = tkinter.filedialog.askopenfilenames()
    print(file_path[0])
    return file_path[0]


def selectDir():  # 选择文件夹
    root = tkinter.Tk()
    root.withdraw()
    # file_path = 'D:\\'
    file_path = tkinter.filedialog.askdirectory()
    print(file_path)
    return file_path
