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
    cursor.execute("select * FROM hosts WHERE groupname='firstgroup'")
    values=cursor.fetchall()
    hostbean=HostBean.HostBean()
    hostbean.setip(values[0][0])
    hostbean.setgroup(values[0][1])
    return render_template('product.html',ip=hostbean.getip(),group=hostbean.getgroup())


if __name__ == '__main__':
    app.run()
