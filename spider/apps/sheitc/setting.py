#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:44
# @Author  : sunny
# @File    : setting.py
# @Software: PyCharm


url = 'http://www.sheitc.gov.cn/jgld/index.htm'  # http://www.sheitc.sh.gov.cn/ttxw/index_2.htm

news_url = 'http://www.sheitc.sh.gov.cn/{}/index{}.htm'

# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,ja;q=0.6",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "www.sheitc.sh.gov.cn",
    "Connection": "keep-alive",
    "Referer": "https://ai.qq.com/info/index.shtml",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}
