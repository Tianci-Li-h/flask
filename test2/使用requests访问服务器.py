# 调用API接口
import requests
import json

base_url = 'http://127.0.0.1:5000/get_predict'
data_json = json.dumps({'height': 183, 'weight': 130})   # dumps：将python对象解码为json数据
response = requests.post(base_url, json=data_json)
predict_data = response.json()
print('response:', response)
print('response.text:', response.text)
print('response.content:', response.content)
print('predict_result', predict_data)
