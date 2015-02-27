#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Lyan'
import shelve
from datetime import datetime
from flask import Flask,request,render_template,redirect,escape,Markup
application=Flask(__name__)

DATA_FILE='guestbook.dat'

def save_data(name,comment,create_at):
    database=shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list=[]
    else:
        greeting_list=database['greeting_list']
    greeting_list.insert(0,{
        'name': name,
        'comment': comment,
        'create_at': create_at
    })
    database['greeting_list']=greeting_list
    database.close()
    return 0

def load_data():
    database=shelve.open(DATA_FILE)
    greeting_list=database.get('greeting_list',[])
    database.close()
    return greeting_list

@application.route('/')
def login():
    return render_template('login.xhtml')

@application.route('/login', methods=['POST'])
def userCheck():
    username=request.form.get('username')
    password=request.form.get('password')
    if username=='admin' and password=='123456':
        greeting_list=load_data()
        return render_template('index.xhtml',gt=greeting_list)

@application.route('/index')
def index():
    """
    Top page
    use template to show the page
    :return:'index.xhtml'
    """
    greeting_list=load_data()
    return render_template('index.xhtml', gt=greeting_list)

@application.route('/post', methods=['POST'])
def post():
    name=request.form.get('name')
    comments=request.form.get('comments')
    create_at=datetime.now()
    save_data(name,comments,create_at)
    return redirect('/index')

if __name__ == '__main__':
    application.run()