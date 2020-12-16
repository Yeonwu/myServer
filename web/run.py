from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello~! I love python!'

@app.route('/cat')
def cakes():
    return 'This is cat'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.219.115', port=80)
