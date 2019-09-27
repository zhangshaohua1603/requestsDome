#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangshaohua
# @remarks : 传统表单类POST请求（x-www-form-urlencoded）

import requests

r = "http://httpbin.org/post"
datas = {'name':'zhangsan','age':'18'}

res = requests.post(url=r,data=datas)

print(res.text)
