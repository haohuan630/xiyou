#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 9:37
# @Author  : sunny
# @File    : libs.py
# @Software: PyCharm

import re


def str_sub(str_old):
    """只保留括号内的内容"""
    str_new = re.sub(r'[^\u4e00-\u9fa5,A-Za-z0-9\-。.？！，、；:：“”‘’（）《》〈〉/—\\]', "", str_old)

    return str_new


def str_replace(str_old):
    """只保留括号内的内容"""
    str_new = str_old.replace(u'\xa0', u' ').replace(u'\u3000', '').replace(u'\r\n ', '')

    return str_new


def str_replace_n(str_old):
    """只保留括号内的内容"""
    str_new = str_old.replace(u'\xa0', u' ').replace(u'\n', '').replace(u'\r', '')

    return str_new
