#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:51
# @Author  : sunny
# @File    : test.py
# @Software: PyCharm
from libs.views.spider_task import TaskSpider


class TestSpider(TaskSpider):
    """测试"""
    def run(self):
        url = "http://----{}"
        header = "header://----{}"

        TaskSpider(url, header)
        print("111111111")


if __name__ == '__main__':
    url = "http://----{}"
    header = "header://----{}"
    test = TestSpider(url, header)
    test.run()

