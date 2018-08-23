# 启动程序，请设置路径参数
# 安装python excel库 指令：pip install xlrd
# 安装 Pillow图像处理库 指令：pip install Pillow
from practice.app003.selectImg import selectDir
from practice.app003.xlrd001 import read_excel

# excel_path = ""  # excel绝对路径
# bg_path = ""  # 卡片背景绝对路径
# output_path = ""  # 卡片输出绝对路径
# read_excel(excel_path, bg_path, output_path)


excel_path = "excel.xlsx"  # excel绝对路径
bg_path = "bg.jpg"  # 卡片背景绝对路径
output_path = selectDir() # 卡片输出绝对路径
read_excel(excel_path, bg_path, output_path)
