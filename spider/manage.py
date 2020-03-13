#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:02
# @Author  : sunny
# @File    : manage.py.py
# @Software: PyCharm

import gevent.monkey
from gevent.pool import Pool

from libs.log import loggerInFile
gevent.monkey.patch_all()

import importlib
import setting
from queue import Queue

run_file = "crm 数据爬取"


class SunnySpider(object):
    """协程 执行任务"""
    def __init__(self):
        self.task_queue = Queue()
        self.pool = Pool()

    def get_task_to_queue(self):
        """获取url 放入队列中"""
        for app in setting.INSTALLED_APPS:
            self.task_queue.put(app)

    def exec_task(self):
        """执行队列中的任务"""
        # 获取 队列中等待的任务
        task_app = self.task_queue.get()

        execute_from_command = importlib.import_module(task_app)
        execute_from_command.run()

        # print(execute_from_command + 1)
        self.task_queue.task_done()

    def exec_task_finish(self, result):
        """队列中的人物完成执行 // 注意必须携带参数result"""

        print("任务执行完成-----result:", result)
        # 处理完成一个任务后继续处理下一个任务
        self.pool.apply_async(self.exec_task, callback=self.exec_task_finish)

    # @loggerInFile("crm_log.txt", run_file)
    def run(self):
        self.get_task_to_queue()

        # callback 执行完成任务后回调，同时执行 task_number 个任务
        # async 异步执行
        app_number = len(setting.INSTALLED_APPS)
        task_number = 10 if app_number > 10 else app_number
        # print(task_number)

        for idxe in range(task_number):
            self.pool.apply_async(self.exec_task, callback=self.exec_task_finish)

        # 退出条件
        self.task_queue.join()


if __name__ == '__main__':
    spider = SunnySpider()
    spider.run()
