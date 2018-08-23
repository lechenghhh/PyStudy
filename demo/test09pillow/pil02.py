from PIL import Image, ImageDraw, ImageFont
from demo.test09pillow.selectImg import selectFile

# http://font.chinaz.com/zhongwenziti.html 字体下载网站

img = Image.open(selectFile())

draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('consola.ttf', size=80)  # HYLiuZiHeiJ.ttf 字体以及大小
fillcolor = '#4CAF50'
(width, height) = img.size
# 第一个参数是加入字体的坐标
# 第二个参数是文字内容
# 第三个参数是字体格式
# 第四个参数是字体颜色
draw.text((40, 100), u'hahaha哈', font=myfont, fill=fillcolor)
img.save('img.jpg', 'jpeg')
