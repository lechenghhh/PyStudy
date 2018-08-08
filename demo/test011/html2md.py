import urllib

from tomd import Tomd  # 安装: pip install tomd

# https://www.v2ex.com/amp/t/364078


url = 'http://118.24.152.88/JPA/'
f = urllib.request.urlopen(url)
html = f.read().decode('utf-8')

md_data = Tomd(html).markdown

print(md_data)


def save(filename, contents):  # 保存到文件方法
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


# md_data[:8]
save('D:\\' + 'webpage2markdown' + '.md', md_data)
