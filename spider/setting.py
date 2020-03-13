#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:02
# @Author  : sunny
# @File    : setting.py
# @Software: PyCharm


# mysql数据库相关配置
import os
import sys

DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'haohuan',
        'DATABASE': 'xiyou',
        'CHARSET': 'utf8',
    },
}

# 注册APP installed // # 注册应用（应用名.apps.apps中的class）
INSTALLED_APPS = [
    # 'apps.xinhua.views',
    'apps.xiyou.views',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "spider"))
sys.path.insert(0, os.path.join(BASE_DIR, "spider/apps"))

for app in INSTALLED_APPS:
    sys.path.insert(0, os.path.join(BASE_DIR, "spider/" + app.replace('.views', "").replace('.', "/")))  # 添加导包路径


# 收件人邮箱设置
RECEIVER = ['menghao.sun@grandhonor.net', 'honggang.wang@grandhonor.net']
# RECEIVER = ['menghao.sun@grandhonor.net']

if __name__ == '__main__':
    print(sys.path)
