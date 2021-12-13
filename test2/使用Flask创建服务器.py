# 导入Flask类
from flask import Flask
from flask import request
from flask import jsonify
import json

# 创建Flask实例，接收参数__name__表示当前文件名，默认会自动指定静态文件static
app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数get_age；告诉flask通过哪个URL可以触发函数
@app.route('/get_predict', methods=['POST'])
def get_age():
    input_json = request.json   # 调用服务器时输入的json字符串
    dict_json = json.loads(input_json)
    print(type(dict_json))
    x_1 = dict_json['height']
    x_2 = dict_json['weight']
    # 此处可以加自己的特征处理，模型预测
    print(type(x_1))
    data = 0.5 * x_1 + 0.4 * x_2
    return str(data)   # The return type must be a string, tuple  # jsonify(data)


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2021)  # 127.0.0.1 #指的是本地ip
