#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : spider_main.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:36
import html_downloader
import html_outputer
import html_parser
import url_manager
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawl %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                if count == 1000:
                    break
            except Exception as e:
                    print 'craw failed: %s' % e

        self.outputer.output_html()



if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/python' # 入口url
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
