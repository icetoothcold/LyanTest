#!/usr/bin/env python
from flask import Flask,render_template,request,redirect,url_for,session,flash
import ConnDB

SECRET_KEY = 'development key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    cururl = url_for('index')
    return render_template('index.html',indexurl=cururl)

@app.route('/product.html')
def product():
    cururl = url_for('product')
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute("select * FROM hosts")
    hostlist = cursor.fetchall()
    cursor.execute("select distinct groupname FROM hosts")
    grouplist = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('product.html',hostlist=hostlist,grouplist=grouplist,produrl=cururl)

@app.route('/addhost.html')
def addhost():
    cururl = url_for('addhost')
    return render_template('addhost.html',addhurl=cururl)


@app.route('/delhost.html')
def delhost():
    cururl = url_for('delhost')
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute("select * FROM hosts")
    hostlist = cursor.fetchall()
    cursor.execute("select distinct groupname FROM hosts")
    grouplist = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('delhost.html',hostlist=hostlist,grouplist=grouplist,delhurl=cururl)


@app.route('/delhost/<name>')
def delete(name):
    print name
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute('delete from hosts where ip=?',(name,))
    print cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return redirect('/delhost.html')

@app.route('/hostpost',methods=['POST'])
def hostpost():
    ip = request.form.get('ip')
    group = request.form.get('group')
    conn = ConnDB.ConnDB('hosts.db')
    cursor = conn.cursor()
    cursor.execute("insert INTO hosts (ip,groupname) VALUES (?,?)",[ip,group])
    cursor.close()
    conn.commit()
    conn.close()
    print ip, group
    return redirect('/addhost.html')


@app.route('/login.html')
def loginpage():
    return render_template('login.html')


@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username')
    passwd=request.form.get('passwd')
    if username == 'lyan':
        if passwd == '123456':
            session['logged_in'] = True
            print username,passwd
            print session
            print username,passwd
            return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')




if __name__ == '__main__':
    app.run('0.0.0.0')
