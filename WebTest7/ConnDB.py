#!/usr/bin/env python
__author__ = 'Lyan'
import sqlite3

def ConnDB(DBname):
    conn=sqlite3.connect(DBname)
    return conn

if __name__ == '__main__':
    conn=ConnDB('hosts.db')
    cursor=conn.cursor()
    ip='10.6.200.1'
    group='test1'
    #cursor.execute('create table hosts (ip varchar(50) primary key, groupname varchar(50))')
    #cursor.execute("insert INTO hosts (ip,groupname) VALUES (?,?)",[ip,group])
    #cursor.execute("INSERT INTO  hosts (ip,groupname) VALUES  ('10.6.100.6','thirdgroup')")
    cursor.execute("SELECT * FROM hosts")
    #cursor.execute("SELECT DISTINCT groupname FROM hosts")
    values=cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print values