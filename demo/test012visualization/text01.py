# 安装：pip install jieba wordcloud matplotlib

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

from demo.test011pillow.selectImg import selectFile  # 我的选择文件

file_path = selectFile()

# 1.读出歌词
text = open(file_path, 'r', encoding='utf-8').read()
# 2.把歌词剪开
cut_text = jieba.cut(text)
# print(type(cut_text))
# print(next(cut_text))
# print(next(cut_text))
# 3.以空格拼接起来
result = " ".join(cut_text)
print(result)
# 4.生成词云
wc = WordCloud(
    font_path='simhei.ttf',  # 字体路劲
    background_color='white',  # 背景颜色
    width=1280,
    height=720,
    max_font_size=120,  # 字体大小
    min_font_size=20,
    mask=plt.imread('bg2.jpg'),  #背景图片
    max_words=1000
)
wc.generate(result)
wc.to_file('result.png')  # 图片保存

# 5.显示图片
plt.figure('result')  # 图片显示的名字
plt.imshow(wc)
plt.axis('off')  # 关闭坐标
plt.show()
