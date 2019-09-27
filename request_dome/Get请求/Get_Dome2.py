#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangshaohua
# @remarks : Get请求带参数


import requests

# Get请求方式一
# 定义请求地址
r = "http://httpbin.org/get?name=zhangsan&tel=13012345678"
# 发送请求,获取响应
res = requests.get(r)
# 解析响应
print(res.text)

# Get请求方式二
r = "http://httpbin.org/get"
param = {'name':'zhangsan','tel':'13012345678'}

res = requests.get(url=r,params=param)

print(res.text)