import json

json_data = open('../../data/chp3/data-text.json').read()

data = json.loads(json_data) #接收字符串作为参数

for item in data:
    print (item)
