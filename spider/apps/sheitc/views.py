#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:42
# @Author  : sunny
# @File    : views.py
# @Software: PyCharm

import datetime
import os
import re

from lxml import etree
import requests

from sheitc import setting
from spider.libs.log import loggerInFile
from spider.model.save_data_to_db import save_data
from spider.setting import DATA_CLASS

run_file = "上海信息经济委员会"


def get_news_info(news_info_url_list):
    """获取新闻信息"""
    for url_item in news_info_url_list:
        url = url_item
        # print(url)
        headers = setting.headers

        response = requests.get(url, headers=headers)
        news_info = response.text

        news_info = etree.HTML(news_info)
        news_id = url.split('/')[-1].split('.')[0]
        try:
            news_info_img = news_info.xpath('//*[@id="ivs_content"]/p/img/@src')
        except BaseException as e:
            print(e)
            news_info_img = ['']
        try:
            news_info_title = news_info.xpath('//*[@id="ivs_title"]/text()')
        except BaseException as e:
            print(e)
            news_info_title = ['']
        try:
            news_info_source = news_info.xpath('//div/h3[2]/text()')
        except BaseException as e:
            print(e)
            news_info_source = ['']
        try:
            news_info_content = news_info.xpath('//*[@id="ivs_content"]/p/text()')
        except BaseException as e:
            print(e)
            news_info_content = ['']

        news_content = ''
        news_img = ''
        for con_item in news_info_content:
            news_content += con_item.replace(u'\xa0', u' ').replace(u'\u3000', '').replace(u'\r\n ', ''). \
                                replace(u' ', '') + '\r\n'

        for img_item in news_info_img:
            news_img += img_item + '\r\n'

        news_class = DATA_CLASS[setting.url]

        news_dict = {}

        news_dict['news_id'] = news_id + "_1"
        news_dict['news_url'] = str(url)
        news_dict['news_title'] = news_info_title
        news_dict['news_abstract'] = ''
        news_dict['news_content'] = news_content
        news_dict['news_publish_time'] = ''
        news_dict['news_source'] = news_info_source
        news_dict['news_author'] = ''
        news_dict['news_img'] = news_img
        news_dict['news_class'] = news_class
        news_dict['spider_time'] = datetime.date.today()

        # print(news_class)
        save_data(news_dict)


def getDate(date):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=date)
    yesterday = today - oneday
    day = str(yesterday).split('-')[-1]

    return day


def news_info_main(item):
    # for url_item in news_url:

    for i in range(1, 3):
        if i != 1:
            url = setting.news_url.format(item, ('_' + str(i)))
        else:
            url = setting.news_url.format(item, '')

        headers = setting.headers
        # print(url)

        response = requests.get(url, headers=headers)
        news_info_HTML = response.text
        # print(news_info_HTML)

        rex = r'<p><a href="([^"]*)"[^>]*>([\s\S]*?)</a>'

        news_info_url_list = []
        for url_item in re.findall(rex, news_info_HTML):
            news_flag = url_item[0].split('/')[-2]
            if (news_flag == 'zxxx' or news_flag == 'ttxw'):
                news_info_url_list.append(url_item[0])

        get_news_info(news_info_url_list)


@loggerInFile("sheitc_log.txt", run_file)
def run():
    # 新闻动态
    news_list = ['zxxx', 'ttxw']
    for item in news_list:
        news_info_main(item)


if __name__ == '__main__':
    # 上海经济和信息化委会
    run()
