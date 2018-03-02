#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : html_downloader.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:37
import requests

class HtmlDownloader(object):
    """
    HTML下载器
    """
    def __init__(self):
        # requests的url重定向必须加入http包头文件,不然会报302
        self.headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def download(self, url):
        if url is None:
            return None

        response = requests.get(url,headers=self.headers)

        if response.status_code != 200:

            print('页面失败原因: %d \t %s' % (response.status_code, url))
            return None

        return response.content.decode('utf-8')

