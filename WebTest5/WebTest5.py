#!/usr/bin/env python
from flask import Flask,render_template
import ConnDB,HostBean
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product.html')
def product():
    conn=ConnDB.ConnDB('hosts.db')
    cursor=conn.cursor()
    cursor.execute("select * FROM hosts")
    hostlist=cursor.fetchall()
    cursor.execute("select distinct groupname FROM hosts")
    grouplist=cursor.fetchall()
    print hostlist
    print grouplist
    return render_template('product.html',hostlist=hostlist,grouplist=grouplist)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
