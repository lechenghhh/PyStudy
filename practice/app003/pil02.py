from PIL import Image, ImageDraw, ImageFont
from practice.app003.selectImg import selectFile, selectDir


# http://font.chinaz.com/zhongwenziti.html 字体下载网站
def setTextWithImg(background_path, title, content, name, text2, output_path):
    img = Image.open(background_path)
    print(img.size)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('consola.ttf', size=30)  # HYLiuZiHeiJ.ttf 字体以及大小
    draw.text((40, 40), title, font=myfont, fill='#4CAF50')  # 坐标左上角为0,内容,格式大小,字体颜色
    myfont2 = ImageFont.truetype('consola.ttf', size=20)  # HYLiuZiHeiJ.ttf 字体以及大小
    draw.text((60, 80), content, font=myfont2, fill='#388E3C')
    myfont3 = ImageFont.truetype('consola.ttf', size=40)  # HYLiuZiHeiJ.ttf 字体以及大小
    draw.text((40, 100), name, font=myfont3, fill='#448AFF')
    myfont4 = ImageFont.truetype('consola.ttf', size=20)  # HYLiuZiHeiJ.ttf 字体以及大小
    draw.text((10, 150), text2, font=myfont4, fill='#212121')
    img.save(output_path + '\\' + name + '.jpg', 'jpeg')


# 测试：
# if __name__ == '__main__':
#     setTextWithImg(selectFile(), "title", "content", "name", "text2", selectDir())
