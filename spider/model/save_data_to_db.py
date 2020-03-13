#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:55
# @Author  : sunny
# @File    : save_data_to_db.py
# @Software: PyCharm
from libs.database.database import DB


def save_college(item):
    """保存学院数据"""
    with DB() as cs_and_con:
        cursor = cs_and_con[0]
        connect = cs_and_con[1]

        # # 查询操作
        sql_select = "select * from t_college WHERE code=%s"
        value_select = item['code']
        # 先进行查重处理
        cursor.execute(sql_select, value_select)
        # 是否有重复数据
        repetition = cursor.fetchone()
        connect.commit()
        # 有重复就更新， 没有重复就保存
        if repetition:
            # 更新
            print("重复")
            # sql_update = "update t_college set code=%s, news_url=%s, news_title=%s, news_abstract=%s," \
            #              " news_content=%s ,news_publish_time=%s,news_source=%s,news_author=%s,spider_time=%s," \
            #              "news_img=%s, news_class=%s where code=%s"
            # value_update = (
            #     item['code'], item['news_url'], item['news_title'], item['news_abstract'], item['news_content'],
            #     item['news_publish_time'], item['news_source'], item['news_author'], item['spider_time'],
            #     item['news_img'], item["news_class"], repetition[1])
            #
            # try:
            #     cursor.execute(sql_update, value_update)
            #     update_con = "id为{}的数据已存在, 更新中...".format(repetition[1])
            #     print(update_con)
            #     connect.commit()
            # except Exception as e:
            #     print(e)
            #     print(sql_update, value_update)
            #     connect.rollback()
        else:
            # 执行数据操作
            # 插入操作
            sql_insert = "insert into t_college(code, news_url, news_title, news_abstract, news_content ," \
                         "news_publish_time,news_source,news_author,spider_time, news_img, news_class) " \
                         "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value_insert = (
                item['code'], item['news_url'], item['news_title'], item['news_abstract'], item['news_content'],
                item['news_publish_time'], item['news_source'], item['news_author'], item['spider_time'],
                item['news_img'], item['news_class'])

            try:
                cursor.execute(sql_insert, value_insert)
                add_con = "id为{}的数据存储中...".format(item['news_id'])
                print(add_con)
                connect.commit()
            except Exception as e:
                print(e)
                connect.rollback()
            else:
                connect.commit()


def save_data(item):
    """入库"""
    with DB() as cs_and_con:
        cursor = cs_and_con[0]
        connect = cs_and_con[1]

        # # 查询操作
        sql_select = "select * from t_college WHERE news_id=%s"
        value_select = item['news_id']
        # 先进行查重处理
        cursor.execute(sql_select, value_select)
        # 是否有重复数据
        repetition = cursor.fetchone()
        connect.commit()
        # 有重复就更新， 没有重复就保存
        if repetition:
            # 更新
            sql_update = "update crm_content set news_id=%s, news_url=%s, news_title=%s, news_abstract=%s," \
                         " news_content=%s ,news_publish_time=%s,news_source=%s,news_author=%s,spider_time=%s," \
                         "news_img=%s, news_class=%s where news_id=%s"
            value_update = (
                item['news_id'], item['news_url'], item['news_title'], item['news_abstract'], item['news_content'],
                item['news_publish_time'], item['news_source'], item['news_author'], item['spider_time'],
                item['news_img'], item["news_class"], repetition[1])

            try:
                cursor.execute(sql_update, value_update)
                update_con = "id为{}的数据已存在, 更新中...".format(repetition[1])
                print(update_con)
                connect.commit()
            except Exception as e:
                print(e)
                print(sql_update, value_update)
                connect.rollback()
        else:
            # 执行数据操作
            # 插入操作
            sql_insert = "insert into crm_content(news_id, news_url, news_title, news_abstract, news_content ," \
                         "news_publish_time,news_source,news_author,spider_time, news_img, news_class) " \
                         "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value_insert = (
                item['news_id'], item['news_url'], item['news_title'], item['news_abstract'], item['news_content'],
                item['news_publish_time'], item['news_source'], item['news_author'], item['spider_time'],
                item['news_img'], item['news_class'])

            try:
                cursor.execute(sql_insert, value_insert)
                add_con = "id为{}的数据存储中...".format(item['news_id'])
                print(add_con)
                connect.commit()
            except Exception as e:
                print(e)
                connect.rollback()
            else:
                connect.commit()


if __name__ == '__main__':
    pass
