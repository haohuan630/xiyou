#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : sunny
# @Time    : 2020/3/23 13:39
# @File    : test.py
# @Software: PyCharm
import requests
from lxml import etree

url = "http://gr.xupt.edu.cn/info/1101/3959.htm"

# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,ja;q=0.6",
    "Content-Type": "text/html",
    "Host": "gr.xupt.edu.cn",
    "Connection": "keep-alive",
    "Referer": "https://ai.qq.com/info/index.shtml",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "If-None-Match": "54fbd-59f8d40b6f990-gzip",
    "Cookie": "JSESSIONID=0FF1B2B126ED764DE82AD122873B75C5"
}


def run():
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding  # 解决中文乱码问题
    info_HTML = response.text
    info_etr = etree.HTML(info_HTML)
    views = info_etr.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/form/div/div[1]/text()')

    print(views)


if __name__ == '__main__':
    run()
