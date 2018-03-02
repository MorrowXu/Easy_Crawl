#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : spider_main.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:36
import html_downloader
import outputer
import html_parser
import url_manager
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    pass

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.Outputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('crawl %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.sql_cennector(new_data)
            except Exception as e:
                    print('craw failed: %s' % e)
            count += 1
            if count > 100:
                break

if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/长滩岛' # 入口url
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
