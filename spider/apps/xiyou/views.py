#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : sunny
# @Time    : 2020/3/13 21:50
# @File    : views.py
# @Software: PyCharm
import os
import re
import sys
from pprint import pprint

from lxml import etree

import requests

from apps.xiyou import config
from model.save_data_to_db import save_person_to_db, find_code_for_name, save_college_to_db, save_major_to_db, \
    save_fields_to_db, save_fields_and_person_code_to_db

path_add = os.path.dirname(os.path.realpath(__file__))

# 全局数据盒子
college_dict = {}
major_dict = {}
fields_dict = {}
person_dict = {}
field_and_person_code = {}


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
        college_dict["code"] = data[:3] + "000"

        save_college_to_db(college_dict)
        # pprint(college_dict)

    elif is_number(data[:6]):
        """专业数据"""
        if data[:6] == "085400" and college_dict["code"] == "001000":
            m_code = "185400"
        else:
            m_code = data[:6]

        major_dict["name"] = data
        major_dict["code"] = m_code
        major_dict["college_code"] = college_dict["code"]

        save_major_to_db(major_dict)
        # pprint(major_dict)
    else:
        # 方向 和 人名
        if data != "01电子与通信工程":
            # data = clean_spaces(data)

            field_and_person = data.split("、")  # 处理不规则数据

            if field_and_person[0] == "03 （全日制）光电传感":
                s = field_and_person[0] + "、" + field_and_person[1]
                field_and_person.insert(0, s)
                field_and_person.pop(2)

            fap = field_and_person[0].split()  # 把方向和人名分开
            p_name = fap.pop(-1)  # 删除最后一个人名
            # 人名列表
            p_name_list = field_and_person[1:]
            p_name_list.append(p_name)

            field = ""
            for f in fap:
                field += f

            if "(非全日制)" in field:
                # 全日制和非全日制
                is_f_quan = field.split("(非全日制)")

                # 有非全日制
                f_quan = is_f_quan[0]
                f_quan = f_quan[:-2]

                pattern = re.compile(r'\D+')  # 查找非数字
                f_quan_list = pattern.findall(f_quan)

                for i, q in enumerate(f_quan_list):
                    p_list = q.split("(全")
                    field_name = "0" + str((i + 1)) + "(全/非" + p_list[-1]

                    # 数据格式化
                    fields_dict["name"] = field_name
                    fields_dict["code"] = major_dict["code"][:4] + field_name[:2]
                    fields_dict["major_code"] = major_dict["code"]

                    save_fields_to_db(fields_dict)

                    # print(fields_dict)
                    # 人员信息处理
                    for item in p_name_list:
                        p_code = find_code_for_name(item)

                        # 数据格式化
                        if p_code:
                            field_and_person_code["fields_code"] = fields_dict["code"]
                            field_and_person_code["person_code"] = p_code

                            save_fields_and_person_code_to_db(field_and_person_code)

            else:
                """方向数据格式化"""
                fields_dict["name"] = field
                # 为了编码不重复
                is_00 = "01" if field[:2] == "00" else field[:2]

                fields_dict["code"] = major_dict["code"][:4] + is_00
                fields_dict["major_code"] = major_dict["code"]

                save_fields_to_db(fields_dict)

                # print(fields_dict)

                """人员信息数据"""
                for item in p_name_list:
                    p_code = find_code_for_name(item)

                    # 数据格式化
                    if p_code:
                        field_and_person_code["fields_code"] = fields_dict["code"]
                        field_and_person_code["person_code"] = p_code

                        save_fields_and_person_code_to_db(field_and_person_code)


def clean_spaces(data):
    """去除空格"""

    c_data = data.replace(" ", "")
    return c_data


def clean_person_url_list(url_list):
    """清洗url"""
    p_url_list = []

    for item in url_list:
        if "http://" not in item:
            p_url = "http://gr.xupt.edu.cn" + item.split('../..')[-1]
            p_url_list.append(p_url)

        elif "http://" in item:
            p_url_list.append(item)

    return p_url_list


def clean_con(data):
    person_con = ''
    for item in data:
        item = item.replace('\r\n', "").replace('\xa0', "").replace(" ", "")
        person_con += item

    return person_con


def get_findall_emails(text):
    """
    # 自定义获取文本电子邮件的函数
    :param text: 文本
    :return: 返回电子邮件列表
    """
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return emails


def get_person_info(data_list):
    """人员信息"""
    headers = config.headers

    # 清洗url
    p_url_list = clean_person_url_list(data_list)

    # print(p_url_list)
    for item in p_url_list:
        trytimes = 3  # 某请求失效时重试的次数

        for i in range(trytimes):
            try:
                response = requests.get(item, headers=headers)
                response.encoding = response.apparent_encoding  # 解决中文乱码问题
                p_info_HTML = response.text
                p_info_etr = etree.HTML(p_info_HTML)

                if response.status_code == 200:
                    # print(item, response)
                    # p_info_con = p_info_etr.xpath('string(//*[@id="vsb_content"]/div//span)')
                    p_code = item.split("/")[-1].split(".")[0] + "00"
                    p_con = p_info_etr.xpath('//*[@id="vsb_content"]/div//text()')
                    p_name = p_info_etr.xpath('/html/body//div/h1/text()')[0]

                    p_views = p_info_etr.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/form/div/div[1]/script/text()')
                    p_views = p_views[-1].split(",")[-1].split(")")[0] if p_views else ""

                    # 组装数据和清洗
                    person_con = clean_con(p_con)
                    p_brief_intro = person_con.split("。")[0].split("个人简介：")[-1]

                    try:
                        p_email_list = get_findall_emails(person_con.split("电子邮件")[-1])
                        if len(p_email_list) == 2:
                            p_email = p_email_list[0] + "，" + "p_email_list[0]"
                        else:
                            p_email = p_email_list[0]

                    except:
                        p_email = ""

                    # 数据格式化
                    person_dict["code"] = p_code
                    person_dict["views"] = p_views
                    person_dict["name"] = p_name
                    person_dict["content"] = person_con
                    person_dict["brief_intro"] = p_brief_intro
                    person_dict["email"] = p_email

                    # print(p_name, p_code, p_views, p_email)
                    # print(person_dict)

                    save_person_to_db(person_dict)

                    break
            except:
                print(f'requests failed {i} time')


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

    # 院、专业、方向
    for i in range(2, 100):
        xpath_ = 'string(//*[@id="vsb_content"]/div/table/tbody/tr[' + str(i) + '])'
        con_item = info_etr.xpath(xpath_)
        con_item_str = str(con_item).replace('\r\n', '').strip()

        print("-------------------------", con_item_str)
        if con_item_str:
            data_class(con_item_str)

    # 人员信息详情
    # person_url_list = info_etr.xpath(' //*[@id="vsb_content"]/div/table/tbody//a/@href')
    # get_person_info(person_url_list)


def run():
    """程序入口"""
    get_HTML()


if __name__ == '__main__':
    run()
