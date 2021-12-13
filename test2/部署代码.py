from flask import Flask, request
from 敏感词汇 import SensitiveWordDetect

app = Flask(__name__)

# 此处做一些文件读取、类实例化、计算图加载等预处理的工作
sensitive_words_path = '../word_files/senti_words.txt'  # 敏感词列表
stopWords_path = '../word_files/stop_words.txt'  # 特殊符号列表
detector = SensitiveWordDetect(sensitive_words_path, stopWords_path)


@app.route('/sentiwords', methods=["POST"])
def sentiwords():
    line = request.form['line']

    sensitive_words = ''
    if line.strip() != '':
        _, sensitive_lst = detector.replace_sensitive_word(line)
        for word in sensitive_lst:
            sensitive_words += word + ','

    if sensitive_words.strip() == '':
        rst = {
                "legal":"通过",
                "body":[]
        }
    else:
        rst_lst = []
        if sensitive_words.strip() != '':
            rst_lst.append({
                       "type":"包含敏感词",
                       "content":sensitive_words
                    })
        rst = {
            "legal":"不通过",
            "body":rst_lst
        }
    return rst


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=8000)