#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhangshaohua
# @remarks : JSON序列化及反序列化


"""
序列化（字典 -> 文本/文件句柄）： json.dumps()/json.dump()
"""

# 输出后中文被转码
import json

data = {'name':'张三','email':'zhangsan@qq.com','tel':'13012345678','home':'北京市朝阳区'}

srt_data = json.dumps(data)

print(srt_data)

# 文本格式化的方法

import json

data = {'name':'张三','email':'zhangsan@qq.com','tel':'13012345678','home':'北京市朝阳区'}
# indent:缩减空格数
# sort_keys=True:将json结果的key按ascii码排序
# ensure_ascii=False:不确保ascii码，如果返回格式为UTF-8包含中文
srt_data = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)

print(srt_data)

"""
反序列化（文本/文件句柄 -> 字典) : json.loads()/json.load()
"""

import json

res_dict = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
f = open("demo1.json","w")
json.dump(res_dict, f)

import json

f = open("demo2.json","r", encoding="utf-8")  # 文件中有中文需要指定编码
f_dict = json.load(f) # 反序列化将文件句柄转化为字典
print(f_dict['name']) # 读取其中参数
f.close()
