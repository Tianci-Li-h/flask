# coding=UTF-8
from datetime import datetime
import requests

starttime = datetime.now()

text_path = "../test_files/000.txt"  # 文本路径

content = [] # 临时存储文本
with open(text_path, 'r', encoding='utf-8') as f:
    content = f.readlines()

line = ''.join(content)
data = {"line": line}
headers = {
    'Connection': 'close',
    }
r = requests.post('http://0.0.0.0:8000/sentiwords', data=data, headers=headers)

if str(r.status_code) != '200':
    print("status_code: ", str(r.status_code))
    print(r.text)

elif r.json()['legal'] == '不通过':
    for temp in r.json()['body']:
        if temp['type'] == '包含敏感词':
            sensitive_word_result = temp['content']
    print(sensitive_word_result)

endtime = datetime.now()
time_consume = endtime - starttime
print('敏感词检测完成，共用时{}'.format(time_consume))