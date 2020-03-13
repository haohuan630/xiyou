# coding=utf8
import os
import sys
import traceback
import logging
from logging.handlers import TimedRotatingFileHandler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from smtplib import SMTP_SSL

import setting

# 当字符流不属于ascii范围内，就会抛出异常（ordinal not in range(128)）。
# reload(sys)
# sys.setdefaultencoding("utf-8")


def send_log_file(filename, title, content):
    host_server = 'smtp.163.com'
    # sender_qq为发件人的号码
    sender_qq = 'haohuan630'
    # pwd为授权码
    pwd = 'haohuan630'
    # 发件人的邮箱
    sender_qq_mail = 'haohuan630@163.com'
    # 收件人邮箱
    # receiver = setting.RECEIVER
    # 邮件的正文内容
    mail_content = content
    # 邮件标题
    mail_title = title
    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    # 设置发送多个部分
    msg = MIMEMultipart()
    # 文字部分
    puremsg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg.attach(puremsg)
    # 附件部分
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path += "\\logs\\" + filename
    logpart = MIMEApplication(open('{}'.format(path), 'rb').read())
    logpart.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(logpart)
    smtp.sendmail(sender_qq_mail, setting.RECEIVER, msg.as_string())
    smtp.quit()
    print('发送邮件成功')


def loggerInFile(filename, run_file):  # 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
    def decorator(func):
        def inner(*args, **kwargs):  # 1
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            logFilePath = path + "\\logs\\" + filename
            # logFilePath = filename  # 日志按日期滚动，保留5天
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            handler = TimedRotatingFileHandler(logFilePath,
                                               when="d",
                                               interval=1,
                                               backupCount=5)
            formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                # print("Arguments were: %s, %s" % (args, kwargs))
                result = func(*args, **kwargs)  # 2
                logger.info(result)
            except:
                logger.error(traceback.format_exc())
                send_log_file(filename, (run_file+'项目运行异常'), "请查看日志文件")

            logger.removeHandler(handler)  # 日志写入完成后移除handler, 防止重复写入

        return inner

    return decorator


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
