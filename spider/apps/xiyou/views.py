#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : sunny
# @Time    : 2020/3/13 21:50
# @File    : views.py
# @Software: PyCharm
import os
import sys
from pprint import pprint

from lxml import etree

import requests

from apps.xiyou import config

path_add = os.path.dirname(os.path.realpath(__file__))

# 全局数据盒子
college_dict = {}
major_dict = {}
fields_dict = {}
person_dict = {}


def is_number(s):
    """判断字符串是否为数字"""
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def data_class(data):
    """数据分类"""
    if data[-2:] == "学院":
        """学院数据"""
        college_dict["name"] = data[3:]
        college_dict["code"] = data[:3] + "0000"

        pprint(college_dict)

    elif is_number(data[:6]):
        """专业数据"""
        major_dict["name"] = data
        major_dict["code"] = data[:6] + "0"
        major_dict["collegeCode"] = college_dict["code"]

        pprint(major_dict)
    else:
        field_and_person = data.split("、")  # 处理不规则数据
        fap = field_and_person[0].split()

        """方向数据"""
        fields_dict["name"] = fap[0] + fap[1]
        # 为了编码不重复
        flag = "0" if "非全日制" in fap[1] else "1"
        fields_dict["code"] = major_dict["code"][:4] + fap[0] + flag
        fields_dict["majorode"] = major_dict["code"]

        print(fields_dict)

        """人员信息数据"""
        person_list = field_and_person[1:]
        person_list.append(fap[-1])
        print(person_list)
        for item in person_list:
            pass



def get_HTML():
    """ """
    headers = config.headers
    # print(url)

    response = requests.get(config.url, headers=headers)
    response.encoding = response.apparent_encoding  # 解决中文乱码问题
    info_HTML = response.text
    info_etr = etree.HTML(info_HTML)

    # //*[@id="vsb_content"]/div/table/tbody/tr[4]/td[2]/p/span[1]/span[1]/a[1]/@href
    # //*[@id="vsb_content"]/div/table/tbody/tr[7]/td[1]/p
    # 'string(//*[@id="vsb_content"]/div/table/tbody/tr[1])'
    # con_list = info_etr.xpath('//*[@id="vsb_content"]/div/table/tbody//p/span[1]/span[1]/a[1]/@href')
    for i in range(2, 7):
        xpath_ = 'string(//*[@id="vsb_content"]/div/table/tbody/tr[' + str(i) + '])'
        con_item = info_etr.xpath(xpath_)
        con_item_str = str(con_item).replace('\r\n', '').strip()

        # print(con_item_str)
        data_class(con_item_str)


    # con_list = con_list.replace('\r', '').replace('\t', '').replace('\n\n', '\n').replace('\xa0', ' ').replace('\r\n', ' ')

    # con_list = data_clean(con_list)



def run():
    """程序入口"""
    get_HTML()


if __name__ == '__main__':
    run()
