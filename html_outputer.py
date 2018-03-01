#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : html_outputer.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:37 
class HtmlOutputer(object):
    """
    html输入器
    """
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        font = open('output2.html', 'w')
        font.write('<html>')
        font.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        font.write('<body>')
        font.write('<table>')
        for data in self.datas:
            font.write('<tr>')
            font.write('<td>%s&nbsp;</td>' % data['url'])
            font.write('<td>%s&nbsp;</td>' % data['title']) # .encoding('utf-8')
            font.write('<td>%s</td>' % data['summary']) # .encoding('utf-8')
            font.write('</tr>')
        font.write('</table>')
        font.write('</body>')
        font.write('</html>')
        font.close()
        print 'page done'
