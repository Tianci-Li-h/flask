from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index(name=None):
    return 'Hello World'
    # return render_template('hello.html', name=name)


if __name__ == '__main__':
    # app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()
