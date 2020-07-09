import pandas as pd
import openpyxl
import smtplib

sender = 'xuweijun@peilian.com'
receivers = ['kidmagic@126.com']

file1 = '/Users/xuweijun/Downloads/python3/user_study.json' #练手用的实验室的用户数据 json格式
file2 = '/Users/xuweijun/Downloads/stu01.xlsx' #10条BuzzKID用户信息excel格式

import json
params_json = json.load(open(r'/Users/xuweijun/Downloads/python3/user_study.json'))
print(len(params_json))
print(type(params_json))
# print(dict.keys(newdata))
print(params_json[0])
items = params_json[0].items()
# for key,values in params_json[0].items():
#     print(str(key))
print(items)


items = params_json[0].items()
for key,values in params_json[0].items():
    print(str(key))
