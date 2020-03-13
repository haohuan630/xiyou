#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:09
# @Author  : sunny
# @File    : setting.py
# @Software: PyCharm

url = 'http://www.sh.xinhuanet.com/'
url_page = 'http://sh.xinhuanet.com/main/index{}.htm'

url_list = ['http://sh.xinhuanet.com/main/index.htm',
            'http://sh.xinhuanet.com/shzw/index.htm',
            'http://sh.xinhuanet.com/yq/index.htm',
            'http://sh.xinhuanet.com/fortune/sclist.htm',
            'http://sh.xinhuanet.com/fortune.html',
            'http://sh.xinhuanet.com/fortune/jr.htm',
            'http://sh.xinhuanet.com/fashion.html',
            'http://sh.xinhuanet.com/tour.html',
            'http://sh.xinhuanet.com/edu/wlist.htm',
            'http://sh.xinhuanet.com/minsheng/index.htm',
            'http://sh.xinhuanet.com/culture/index.htm',
            'http://sh.xinhuanet.com/house/index.htm',
            'http://sh.xinhuanet.com/sport/index.htm',
            'http://sh.xinhuanet.com/health.html']

person_new_news_url = ['http://sh.xinhuanet.com/leaders/sj/zxhd.htm', 'http://sh.xinhuanet.com/leaders/yy/zxhd.htm',
                   'http://sh.xinhuanet.com/leaders/dyh/zxhd.htm', 'http://sh.xinhuanet.com/leaders/yyc/zxhd.htm']

# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,ja;q=0.6",
    "Content-Type": "text/html",
    "Host": "sh.xinhuanet.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}
headers_page = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,ja;q=0.6",
    "Content-Type": "text/html",
    "Host": "sh.xinhuanet.com",
    "Connection": "keep-alive",
    "cookie": "uid=b92e8afcc00a411895e02958772a5944; wdcid=33ceec660091123f; bdshare_firstime=1559187304352; pc=f15f3c4aaafd4b8caa234b17ffc20f0a.1559187251.1559551036.2; wdlast=1559624914",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}

# mysql数据库相关配置
MYSQL_HOST = '192.168.11.97'
MYSQL_PORT = 3306
MYSQL_DB = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
CHARSET = 'utf8'
