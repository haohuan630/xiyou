#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 13:52
# @Author  : sunny
# @File    : spider_task.py
# @Software: PyCharm
import gevent.monkey

gevent.monkey.patch_all()
from gevent.pool import Pool

from queue import Queue
import requests
from lxml import etree


# from multiprocessing.dummy import Pool


class TaskSpider(object):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.url_queue = Queue()
        self.pool = Pool()

    def get_url_list(self):
        for index in range(1, 14):
            self.url_queue.put(self.url.format(index))

    def exec_task(self):
        url = self.url_queue.get()

        print(url)
        self.url_queue.task_done()

    def exec_task_finish(self, result):
        # 注意必须携带参数result
        print("result", result)
        print("任务执行完成")
        # 处理完成一个任务后继续处理下一个任务
        self.pool.apply_async(self.exec_task, callback=self.exec_task_finish)

    def run(self):
        self.get_url_list()

        # 执行任务
        # callback 执行完成任务后回调，同时执行 5 个任务
        # async 异步执行
        for idxe in range(5):
            self.pool.apply_async(self.exec_task, callback=self.exec_task_finish)

        # 退出条件
        self.url_queue.join()


if __name__ == '__main__':
    spider = TaskSpider()
    spider.run()
