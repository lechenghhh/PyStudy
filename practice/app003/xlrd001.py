# pip install xlrd
import xlrd

from datetime import date, datetime

from demo.test011pillow.selectImg import selectFile, selectDir
from practice.app003.pil02 import setTextWithImg

bg_path = ""
output_path = ""
excel_path = ""


def read_excel(excel_path, bg_path, output_path):
    # 文件位置
    ExcelFile = xlrd.open_workbook(excel_path)
    sheet = ExcelFile.sheet_by_index(0)
    # 打印sheet的名称，行数，列数
    print(sheet.name, sheet.nrows, sheet.ncols)

    # 获取整行或者整列的值
    for i in range(0, sheet.nrows):
        # print(bg_path, sheet.row_values(i)[0], sheet.row_values(i)[0],
        #       sheet.row_values(i)[0], sheet.row_values(i)[0], output_path)
        setTextWithImg(bg_path, sheet.row_values(i)[0], sheet.row_values(i)[1],
                       sheet.row_values(i)[2], sheet.row_values(i)[3], output_path)

# 测试
# if __name__ == '__main__':
#     bg_path = selectFile()
#     excel_path = selectFile()
#     output_path = selectDir()
#     read_excel(excel_path, bg_path, output_path)
