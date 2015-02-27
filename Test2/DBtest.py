__author__ = 'Lyan'
import mysql.connector

import a.Main as Main


conn=mysql.connector.connect(user='root',password='password',database='test3',use_unicode=True)

def creatDB():
    cursor=conn.cursor()
    cursor.execute('create table user2 (id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user2 (id,name) values (%s,%s)',['1','Micheal'])
    print cursor.rowcount
    conn.commit()
    cursor.close()
    return 0
def insertDB():
    cursor=conn.cursor()
    cursor.execute('insert into user2 (id,name) values (%s,%s)',['2','Tom'])
    print cursor.rowcount
    conn.commit()
    cursor.close()
    return 0
def checkDB():
    cursor=conn.cursor()
    cursor.execute('select * from user2')
    values=cursor.fetchall()
    print values
    cursor.close()
    return 0
#creatDB()
#insertDB()
if __name__ == '__main__':
    checkDB()
    conn.close()
    Main.printText()



