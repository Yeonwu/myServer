from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello~! I love python!'

@app.route('/cat')
def cakes():
    return 'This is cat'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
