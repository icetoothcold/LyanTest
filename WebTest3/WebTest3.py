from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/SecPage.html')
def secondpage():
    return render_template('SecPage.html')

@app.route('/FifthPageOne.html')
def fifthpageone():
    return render_template('FifthPageOne.html')


if __name__ == '__main__':
    app.run()
