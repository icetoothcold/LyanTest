#!/usr/bin/env python
__author__ = 'Lyan'
import sqlite3

def ConnDB(DBname):
    conn=sqlite3.connect(DBname)
    return conn

if __name__ == '__main__':
    conn=ConnDB('hosts.db')
    cursor=conn.cursor()
    cursor.execute("select * FROM hosts WHERE groupname='firstgroup'")
    values=cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print values[0][1]