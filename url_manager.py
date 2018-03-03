#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : url_manager.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:36
class UrlManager(object):
    """
    url管理器,负责url的添加
    """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None: # 如果传入的url为空,则返回一个None
            return
        if url not in self.new_urls and url not in self.old_urls: # 如果传入的url不在新增url和旧url的集合中,就添加进新url集合
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0 # 返回一个nel_urls集合长度

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
