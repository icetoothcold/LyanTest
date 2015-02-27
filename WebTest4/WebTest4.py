from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/settings.html')
def settings():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run()
