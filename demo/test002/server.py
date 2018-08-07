# ! /usr/bin/env python
# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
print('server启动')

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

# 协议	功能用处		   端口号 Python模块
# HTTP	网页访问		     80  httplib, urllib, xmlrpclib
# NNTP	阅读和贴新闻文章    119	 nntplib
# FTP	文件传输		     20  ftplib, urllib
# SMTP	发送邮件		     25  smtplib
# POP3	接收邮件		     110 poplib
# IMAP4	获取邮件		     143 imaplib
# Telnet	命令行		 23  telnetlib
# Gopher	信息查找		 70  gopherlib, urllib
