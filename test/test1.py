from flask import Flask    # 导入Flask类
from flask import render_template  # 导入render_template模块
app = Flask(__name__)         # 实例化并命名为app实例


# 使用了装饰器来制定路由url
@app.route('/')  # 调用route路由方法，括号里给定参数，/符号默认为首页
# @app.route('/home/user')    # 调用route路由方法，/home/user定位到访问user方法页面
def index(name=None):
    # return 'Hello World'
    # return '<h3>welcome to my webpage!</h3><hr><p style="color:red">输出语句测试</p>'
    # return render_template("index.html")  # 调用render_template函数，传入html文件参数
    msg = "China up!"
    return render_template("index.html", data=msg)  # 加入变量传递


if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)
