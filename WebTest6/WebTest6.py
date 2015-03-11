
from flask import Flask,render_template,request,redirect,url_for,session,flash

SECRET_KEY = 'development key'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    cururl = url_for('index')
    return render_template('index.html',indexurl=cururl)

@app.route('/show',methods=['POST'])
def show():
    print request.form.get('input1')
    return 'hello world'

if __name__ == '__main__':
    app.run('0.0.0.0')
