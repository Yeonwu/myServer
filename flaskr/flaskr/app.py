# all the imports
from flask import Flask, render_template, request
import pymysql

# configuration

# create our little application :)
app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('home.html', userinfo={
        'name': '오연우',
        'email': '201028@bmrschool.org',
        'grade': '10학년',
        'auth': '관리자'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
