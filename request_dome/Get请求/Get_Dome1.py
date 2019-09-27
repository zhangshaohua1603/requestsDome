#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangshaohua
# @remarks : Get请求无参数


import requests

# Get请求
# 定义请求地址
r = "http://httpbin.org/get"
# 发送请求,获取响应
res = requests.get(r)
# 解析响应
print(res.text)
