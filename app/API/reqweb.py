#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from urllib import quote
from pyquery import PyQuery as pq
from selenium import webdriver

class ReqWebInfo(object):
    @staticmethod
    def get_wx_article_info(wx_url):
        browser = webdriver.PhantomJS()
        browser.get(wx_url)
        html = browser.execute_script("return document.documentElement.outerHTML")
        ' 解析单篇文章 '
        article_dict = {}

        article = html('.weui_media_box[id]')

        title = html('h4[class="weui_media_title"]').text()

        url = 'http://mp.weixin.qq.com' + html('h4[class="weui_media_title"]').attr('hrefs')

        summary = html('.weui_media_desc').text()

        date = html('.weui_media_extra_info').text()

        #pic = self.parse_cover_pic(html)
        #content = self.parse_content_by_url(url).html()

        return html

