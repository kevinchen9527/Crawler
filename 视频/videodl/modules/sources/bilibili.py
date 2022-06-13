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


'''B站视频下载器类'''
class Bilibili(Base):
    def __init__(self, config, logger_handle, **kwargs):
        super(Bilibili, self).__init__(config, logger_handle, **kwargs)
        self.source = 'bilibili'
        self.__initialize()
    '''视频解析'''
    def parse(self, url):
        response = self.session.get(url, headers=self.headers)
        bv = re.compile('BV..........').search(url).group()
        response = self.session.get(self.pagelist_url.format(bv), headers=self.headers)
        response_json = response.json()
        cid_list = [item['cid'] for item in response_json['data']]
        titles = [item.get('part', f'视频走丢啦_{time.time()}') for item in response_json['data']]
        download_urls = []
        for cid in cid_list:
            response = self.session.get(self.play_url.format(cid, bv), headers=self.headers)
            response_json = response.json()
            for item in response_json['data']['durl']:
                download_urls.append(item['url'])
        assert len(titles) == len(download_urls)
        videoinfos = []
        for idx, download_url in enumerate(download_urls):
            videoinfo = {
                'source': self.source,
                'download_url': download_url,
                'savedir': self.config['savedir'],
                'savename': filterBadCharacter(titles[idx]),
                'ext': 'mp4',
            }
            videoinfos.append(videoinfo)
        return videoinfos
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        }
        self.pagelist_url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'
        self.play_url = 'http://api.bilibili.com/x/player/playurl?&cid={}&bvid={}&qn=80&fnval=0&fnver=0&fourk=1'
    '''判断视频链接是否属于该类'''
    @staticmethod
    def isurlvalid(url):
        valid_hosts = ['bilibili.com/video']
        for host in valid_hosts:
            if host in url: return True
        return False