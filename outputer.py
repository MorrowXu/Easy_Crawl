#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : outputer.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:37
try:
    import MySQLdb as mysql
except ImportError:
    import pymysql as mysql # python3


class Outputer(object):
    """
    将解析好的data存入mysqldb
    """

    def sql_cennector(self, data):
        # 连接mysql数据库
        db = mysql.connect(host = 'localhost', user = 'root', passwd = '930502', db = 'webcrawler', charset = 'utf8')
        cursor = db.cursor()
        sql = r'''INSERT INTO baike_key(key_word, content, url) VALUES("%s","%s", "%s")'''\
                % (data['title'], data['summary'], data['url'])
        # print sql
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('Query OK! The data is already in mysqldb.')
        except Exception as e:
            # 发生错误时回滚
            print('Query failed: %s' % e)
            db.rollback()
        db.close()
        pass

    # def __init__(self):
    #     self.datas = []
    #
    # def collect_data(self, data):
    #     if data is None:
    #         return
    #     self.datas.append(data)
    #
    # def output_html(self):
    #     font = open('output2.html', 'w')
    #     font.write('<html>')
    #     font.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
    #     font.write('<body>')
    #     font.write('<table>')
    #     for data in self.datas:
    #         font.write('<tr>')
    #         font.write('<td>%s&nbsp;</td>' % data['url'])
    #         font.write('<td>%s&nbsp;</td>' % data['title']) # .encoding('utf-8')
    #         font.write('<td>%s</td>' % data['summary']) # .encoding('utf-8')
    #         font.write('</tr>')
    #     font.write('</table>')
    #     font.write('</body>')
    #     font.write('</html>')
    #     font.close()
    #     print 'page done'
