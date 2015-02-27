#!/usr/bin/env python
__author__ = 'Lyan'
import sqlite3

def ConnDB(DBname):
    conn=sqlite3.connect(DBname)
    return conn

if __name__ == '__main__':
    conn=ConnDB('hosts.db')
    cursor=conn.cursor()
    #cursor.execute("INSERT INTO  hosts (ip,groupname) VALUES  ('10.6.100.6','thirdgroup')")
    cursor.execute("select * FROM hosts")
    #cursor.execute("SELECT DISTINCT groupname FROM hosts")
    values=cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print values