import pymysql


# pip install paramiko完美结决pymysql问题
def getConn():
    return pymysql.connect("localhost", "root", "", "test")
