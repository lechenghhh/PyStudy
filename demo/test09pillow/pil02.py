from PIL import Image, ImageDraw, ImageFont

# http://font.chinaz.com/zhongwenziti.html 字体下载网站
from pil.selectImg import selectFile

img = Image.open(selectFile())
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('consola.ttf', size=80)  # HYLiuZiHeiJ.ttf
fillcolor = '#4CAF50'
(width, height) = img.size
# 第一个参数是加入字体的坐标
# 第二个参数是文字内容
# 第三个参数是字体格式
# 第四个参数是字体颜色
draw.text((40, 100), u'hahaha', font=myfont, fill=fillcolor)
img.save('output.jpg', 'jpeg')
