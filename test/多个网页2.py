from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    msg = "China up!"
    return render_template("index.html", data=msg)


@app.route('/news')  # 增加一个news页面
def newspage():
    newsContent = "全国上下一心支持武汉，武汉加油！"
    return render_template("news.html", data=newsContent)


@app.route('/product/<a>', methods=['GET'])  # 增加一个product页面
def productpage(a):
    return render_template("product.html", data=a)


if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)
