#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : spider_main.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:36
import downloader
import outputer
import html_parser
import url_manager
import time
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    pass

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() # 初始化url管理器
        self.downloader = downloader.Downloader() # 初始化html下载器
        self.parser = html_parser.HtmlParser() # 初始化html解析器
        self.outputer = outputer.Outputer() # 初始化mysql连接类

    def crawl(self, root_url):
        count = 1 # 计数器
        f_url = ''
        self.urls.add_new_url(root_url) # 将传入的根url传入到url管理器的add_new_url方法中
        while self.urls.has_new_url(): # 启动一个循环,循环数值为new_urls集合的长度
            t = time.strftime('%Y_%m_%d')
            try:
                new_url = self.urls.get_new_url() # 从url管理器中取出一个url, 取出方式为new_urls.pop()
                f_url = new_url
                print('crawl %d : %s' % (count, new_url)) # 打印计数器和url
                html_cont = self.downloader.download(new_url) # 将url传入到html下载器中, 返回一个utf8编码解码的html源码
                new_urls, new_data = self.parser.parse(new_url, html_cont) # html解析器解析源码,返回解析内容中符合规则的url列表和文本字典
                self.urls.add_new_urls(new_urls) # 将解析后的url列表传入url管理器
                self.outputer.sql_cennector(new_data) # 调用sql_cennector将解析后的文本字典传入mysql
            except Exception as e: # 如发生错误,则捕获..
                with open('%s_log.txt' % t, 'a+') as f:  # 'a+' 为追加模式
                    f.write(time.ctime() + ' >>> ' + 'failed' + '\t' + f_url + '\t' +str(e))
                    f.write('\n\n\n')
                print('craw failed: %s' % e) # 将爬取中的异常捕获,并打印原因
            else: # 不发生错误,则...
                with open('%s_log.txt' % t, 'a+') as f:  # 'a+' 为追加模式
                    f.write(time.ctime() + ' >>> ' + 'sucessed'+ '\t' + f_url + '\t')
                    f.write('\n\n\n')
            finally:
                f_url = '' # 置空

            count += 1
            if count > 100:
                self.outputer.sql_closer() # 爬取完毕,关闭mysql连接
                break # 跳出循环


if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/flash' # 入口url
    t1 = time.time()
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    t2 = time.time()
    time_cost = t2 - t1
    print('本次执行一共花费%.2f秒' % time_cost)
