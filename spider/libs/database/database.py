#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:07
# @Author  : sunny
# @File    : database.py
# @Software: PyCharm

from pymysql import connect

from setting import DATABASES


class DB(object):
    """连接数据库的上下文管理器"""

    def __init__(self, db_name='default'):
        """初始化数据库连接"""
        self.db_name = db_name
        self.host = DATABASES[self.db_name]['HOST']
        self.port = DATABASES[self.db_name]['PORT']
        self.user = DATABASES[self.db_name]['USER']
        self.password = DATABASES[self.db_name]['PASSWORD']
        self.database = DATABASES[self.db_name]['DATABASE']
        self.charset = DATABASES[self.db_name]['CHARSET']

        self.conn = connect(host=self.host, port=self.port, user=self.user, password=self.password,
                            database=self.database, charset=self.charset)
        self.cs = self.conn.cursor()

    def __enter__(self):
        """返回cursor　游标对象"""
        return self.cs, self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭数据库连接"""
        self.cs.close()
        self.conn.close()


if __name__ == '__main__':
    with DB() as cs_conn:
        # 执行sql 语句
        print(cs_conn)
        cs = cs_conn[0]

        sql = "select * from customer_info;"
        cs.execute(sql)
        data = cs.fetchall()

    print(data)
