# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:LizhiFM.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import time
import os
from .base import Base
from ..utils import seconds2hms, filterBadCharacter


'''荔枝FM下载类'''
class Lizhi(Base):
    def __init__(self, config, logger_handle, **kwargs):
        super(Lizhi, self).__init__(config, logger_handle, **kwargs)
        self.source = 'lizhi'
        self.__initialize()
    '''歌曲搜索'''
    def search(self, keyword, disable_print=True):
        if not disable_print: self.logger_handle.info('正在%s中搜索 >>>> %s' % (self.source, keyword))
        cfg = self.config.copy()
        response = self.session.get(self.search_url.format(keyword), headers=self.headers)
        all_items = response.json()['audio']['data']        
        songinfos = []
        for item in all_items:
            response = self.session.get(self.songinfo_url.format(item['audio']['id']), headers=self.headers)
            response_json = response.json()
            if response_json['code'] != 0: continue
            download_url = response_json['data'].get('userVoice', {}).get('voicePlayProperty', {}).get('trackUrl', '')
            if not download_url: continue
            filesize = '-'
            ext = download_url.split('.')[-1]
            duration = int(item.get('audio').get('duration', 0))
            songinfo = {
                'source': self.source,
                'songid': str(item['audio']['id']),
                'singers': filterBadCharacter(item['radio'].get('user_name', '-')),
                'album': filterBadCharacter(item['radio'].get('name', '-')),
                'songname': filterBadCharacter(item['audio'].get('name', '-')),
                'savedir': os.path.abspath(os.path.dirname(__file__)) + '/' + cfg['savedir'],
                'savename': filterBadCharacter(item['audio'].get('name', f'{keyword}_{int(time.time())}')),
                'download_url': download_url,
                'lyric': '',
                'filesize': filesize,
                'ext': ext,
                'duration': seconds2hms(duration)
            }
            if not songinfo['album']: songinfo['album'] = '-'
            songinfos.append(songinfo)
            if len(songinfos) == cfg['search_size_per_source']: break
        return songinfos
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Referer': 'http://m.lizhi.fm'
        }
        self.search_url = 'http://m.lizhi.fm/api/search_audio/{}/1'
        self.songinfo_url = 'https://m.lizhi.fm/vodapi/voice/info/{}'