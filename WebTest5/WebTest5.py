#!/usr/bin/env python
from flask import Flask,render_template,request,redirect,url_for
import ConnDB,HostBean
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product.html')
def product():
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute("select * FROM hosts")
    hostlist = cursor.fetchall()
    cursor.execute("select distinct groupname FROM hosts")
    grouplist = cursor.fetchall()
    cursor.close()
    conn.close()
    print hostlist
    print grouplist
    return render_template('product.html',hostlist=hostlist,grouplist=grouplist)

@app.route('/addhost.html')
def addhost():
    return render_template('addhost.html')

@app.route('/hostpost',methods=['POST'])
def hostpost():
    ip = request.form.get('ipaddress')
    group = request.form.get('group')
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute("insert INTO hosts (ip,groupname) VALUES (?,?)",[ip,group])
    cursor.close()
    conn.commit()
    conn.close()
    print ip, group
    return redirect('/addhost.html')
if __name__ == '__main__':
    app.run('0.0.0.0')
    print url_for('addhost')
