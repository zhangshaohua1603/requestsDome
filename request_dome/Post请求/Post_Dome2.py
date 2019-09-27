#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangshaohua
# @remarks : JSON类型的POST请求（application/json）

import requests

r = 'http://httpbin.org/post'
datas = '{"name":"zhangsan","age":"18"}'

res = requests.post(url=r,data=datas)

print(res.text)




import requests
import json # 使用到JSON中的方法，需要提前导入

url = "http://httpbin.org/post"
data = {
        "name": "zhangsan",
        "age": 18
        }  # 字典格式，方便添加
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)