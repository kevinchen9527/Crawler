# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import re
import time
from .base import Base
from ..utils import filterBadCharacter


'''微博视频下载器类'''
class Weibo(Base):
    def __init__(self, config, logger_handle, **kwargs):
        super(Weibo, self).__init__(config, logger_handle, **kwargs)
        self.source = 'weibo'
        self.__initialize()
    '''视频解析'''
    def parse(self, url):
        response = self.session.get(url, headers=self.headers)
        title = re.findall(r'"title": "(.*?)",', response.text)
        download_url = re.findall(r'"mp4_720p_mp4": "(.*?)",', response.text) or re.findall(r'"mp4_hd_mp4": "(.*?)",', response.text) or re.findall(r'"mp4_ld_mp4": "(.*?)"', response.text)
        videoinfo = {
            'source': self.source,
            'download_url': download_url[0],
            'savedir': self.config['savedir'],
            'savename': filterBadCharacter(title[0] if title else f'视频走丢啦_{time.time()}'),
            'ext': 'mp4',
        }
        return [videoinfo]
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        }
    '''判断视频链接是否属于该类'''
    @staticmethod
    def isurlvalid(url):
        valid_hosts = ['weibo.cn', 'weibo.com']
        for host in valid_hosts:
            if host in url: return True
        return False