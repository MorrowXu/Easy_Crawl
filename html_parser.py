#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : html_parser.py
# @Email   : 464580843@qq.com
# Create on 2018/3/1 11:37
import re
import urlparse
# from urllib.parse import urlparse # python3
from bs4 import BeautifulSoup as bs


class HtmlParser(object):
    """

    """

    def _get_new_urls(self, page_url, soup):
        """
        解析url
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\w+$"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        解析数据
        :param page_url:
        :param soup:
        :return:
        """
        res_data = {}
        # url
        res_data['url'] = page_url

        # < dd class ="lemmaWgt-lemmaTitle-title" > < h1 > Request对象 < / h1 >
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary"
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = bs(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
