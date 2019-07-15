from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>hello.</h1>'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
