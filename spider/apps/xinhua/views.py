#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:09
# @Author  : sunny
# @File    : views.py
# @Software: PyCharm
import datetime
import os
from pprint import pprint

import requests
from lxml import etree

from apps.xinhua import config
from libs.log import loggerInFile
from libs.utils import str_replace_n, str_sub
# from model.save_data_to_db import save_data
from setting import DATA_CLASS

# from xinhua import config

path_add = os.path.dirname(os.path.realpath(__file__))
run_file = "新华网"


def get_news_detail(news_class_id, news_url_list):
    """获取新闻详情页内容"""
    for news_url in news_url_list:
        if news_url.startswith('h'):
            headers = config.headers_page

            response = requests.get(news_url, headers=headers)
            # print(response.encoding)  # ISO-8859-1
            # print(response.status_code)
            if response.status_code == 200:
                try:
                    news_info_HTML = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
                    news_info_etr = etree.HTML(news_info_HTML)
                except BaseException as e:
                    print(e)
                    break

                news_id = news_url.split('_')[-1].split('.')[0]

                news_title_xpa = news_info_etr.xpath('//*[@id="title"]/text()')
                news_title = str_replace_n(news_title_xpa[0]) if news_title_xpa else ''

                news_content_xpa = news_info_etr.xpath('//*[@id="article"]/div[2]/p/text()')
                news_content = ''
                for item in news_content_xpa:
                    news_content = news_content + str_sub(item) + '\r\n'

                news_publish_time_xpa = news_info_etr.xpath('//*[@id="article"]/div[1]/div/span[1]/text()')
                news_publish_time = str_sub(news_publish_time_xpa[0]) if news_publish_time_xpa else ''

                news_source_xpa = news_info_etr.xpath('//*[@id="source"]/text()')
                news_source = str_sub(news_source_xpa[0]) if news_source_xpa else ''

                news_img_xpa = news_info_etr.xpath('//*[@id="article"]//p[@align="center"]/img/@src')
                news_img = ''
                for news_img_item in news_img_xpa:
                    news_img = news_img + config.url + news_img_item.split('/')[-1] + '\r\n'

                news_dict = {}
                news_dict['news_id'] = news_id + "_3"
                news_dict['news_url'] = news_url
                news_dict['news_title'] = news_title
                news_dict['news_abstract'] = ''
                news_dict['news_content'] = news_content
                news_dict['news_publish_time'] = news_publish_time
                news_dict['news_source'] = news_source
                news_dict['news_author'] = ''
                news_dict['news_img'] = news_img
                news_dict['news_class'] = news_class_id
                news_dict['spider_time'] = datetime.date.today()

                # print(news_dict)
                # save_data(news_dict)
            else:
                print(news_url, news_url)


def get_news_list(url_index, url_item, is_person_url='false'):
    """除政务以外的news_url_list"""
    headers = config.headers

    for page in range(1, 2):
        if page == 1:
            url_page = url_item.format('')
        else:
            url_page = url_item.format(('_' + str(page)))

        response = requests.get(url_page, headers=headers)

        if response.status_code == 404:
            break
        else:
            news_info_HTML = response.text
            news_info_etr = etree.HTML(news_info_HTML)

            # //div[@class="hdbd-list news-list "]/ul/li/a/@href
            if is_person_url == 'true':
                print(is_person_url)
                news_url_list = news_info_etr.xpath('//div[@class="hdbd-list news-list "]/ul/li/a/@href')[:11]
            else:
                print(is_person_url)
                news_url_list = news_info_etr.xpath('//div[@class="news-list"]/ul/li/a/@href')[:11]

            # print(news_url_list)
            get_news_detail(url_index, news_url_list)


def get_news_list_2(url_index, url_item):
    """获取政务里面的news_url"""
    response = requests.get(url_item, headers=config.headers)
    news_info_HTML = response.text
    news_info_etr = etree.HTML(news_info_HTML)

    news_url_list_2 = news_info_etr.xpath('//div[@class="pc lmtt"]/a/@href')[1:]

    # print(news_url_list_2, url_item)

    for url_index_2, url_item_2 in enumerate(news_url_list_2):
        url_item = url_item_2.split('.htm')[0] + '{}' + '.htm' + url_item.split('.htm')[1]
        url_index_ = str(url_index) + str((url_index_2 + 1))

        get_news_list(int(url_index_), url_item)


def person_new_news():
    """人物最新新闻"""
    person_new_news_url = config.person_new_news_url

    for url_index, url_item in enumerate(person_new_news_url):
        url_item_ = url_item.split('.htm')[0] + '{}' + '.htm' + url_item.split('.htm')[1]

        index_flag = url_item.split('/')[-2]
        if index_flag == 'sj':
            url_index = 111111
        elif index_flag == 'yy':
            url_index = 222222
        elif index_flag == 'dyh':
            url_index = 333333
        elif index_flag == 'yyc':
            url_index = 444444

        # print(url_item_)
        get_news_list(int(url_index), url_item_, 'true')


def news_main():
    """获取新闻列表"""
    url_list = config.url_list

    for url_index, url_item in enumerate(url_list):

        news_class = DATA_CLASS[url_item]

        if url_index == 1:
            get_news_list_2(news_class, url_item)
        else:
            url_item = url_item.split('.htm')[0] + '{}' + '.htm' + url_item.split('.htm')[1]
            get_news_list(news_class, url_item)


def news_nav():
    """获取导航列表"""
    headers = config.headers
    url = config.url
    response = requests.get(url, headers=headers)
    news_info_HTML = response.text.encode('ISO-8859-1').decode(
        requests.utils.get_encodings_from_content(response.text)[0])
    news_info_etr = etree.HTML(news_info_HTML)

    news_url_list = news_info_etr.xpath('//div[@class="nav"]/a/@href')[:14]

    # http://sh.xinhuanet.com/edu/wlist.htm  教育
    # http://sh.xinhuanet.com/fortune/sclist.htm  科创
    news_url_list[3] = "http://sh.xinhuanet.com/fortune/sclist.htm"
    news_url_list[8] = "http://sh.xinhuanet.com/edu/wlist.htm"
    # print(len(news_url_list))
    pprint(news_url_list)

    for url_index, url_item in enumerate(news_url_list):
        print(url_index + 1, url_item)
    #     news_main(url_item)


# @loggerInFile("crm_log.txt", run_file)
def run():
    news_main()
    # person_new_news()


if __name__ == '__main__':
    # 新华网
    run()
