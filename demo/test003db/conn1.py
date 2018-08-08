import pymysql


# pip install paramiko完美结决pymysql问题
def getConn():
    return pymysql.connect("localhost", "root", "123456", "other_db")
