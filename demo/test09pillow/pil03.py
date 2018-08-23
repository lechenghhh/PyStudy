#coding:utf-8
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
"""
创建四位数的验证码
"""
#产生随机验证码内容
def rndTxt():
    txt = []
    txt.append(random.randint(97,123))      #大写字母
    txt.append(random.randint(65,90))       #小写字母
    txt.append(random.randint(48,57))       #数字
    return chr(txt[random.randint(0,2)])

#随机颜色(背景)
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#随机颜色（字体）
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240x60:
width = 60*4
height = 60
img = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype(u'consola.ttf',36)
draw = ImageDraw.Draw(img)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor1())

#输出文字
for txt in range(4):
    draw.text((60*txt+10,10),rndTxt(),font=font,fill=rndColor2())
#模糊化处理
#img = img.filter(ImageFilter.BLUR)
img.save("code.jpg")