# 1. 相关笔记

- 豆瓣镜像安装解决安装速度慢的问题

  ```python
  pip3 install djangorestframework -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
  ```

 - 批量导出/安装开发环境
     ```\python
     pip freeze> request.txt;
     pip install -r request.txt;

     ```
 - 数据库迁移
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```