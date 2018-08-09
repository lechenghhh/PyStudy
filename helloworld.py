#! /usr/bin/env python
# -*- coding: utf-8 -*-
import keyword

print("hello world")

print(keyword.kwlist)  # 显示所有python保留字

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

b1 = 0
b1 = False

if not b1:
    print("!b1")
else:
    print("b1")

c1 = "hahah"
c2 = "hah" + "ah"

if c1 is c2:
    print("yes")
else:
    print("no")

# input("\n\n按下 enter 键后退出。")
name = input("请输入你的名称:")
print("Hello " + name)
