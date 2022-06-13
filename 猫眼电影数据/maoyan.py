# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:maoyan.py
@Time:2022/6/2 14:20

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

import requests
from fake_useragent import *
from lxml import etree
import time
import os

# 随机请求头
ua = fake_useragent.UserAgent()
# 构建请求 需要自己去网页上面换一下  请求不到了就 去网页刷新 把验证码弄了
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': '__mta=247380283.1654160448649.1654161209049.1654161250977.12; _lxsdk_cuid=18123a501cfc8-0bff415e2de21a-26021b51-1fa400-18123a501d0c8; uuid_n_v=v1; uuid=7D1AD970E25211ECB1087FE79CA2CCBE53A95C3A43A941FB9971A9B231090A07; _csrf=42092650e2b4225e939925dce03a24b7acd430b4496865fc1aa4bdda78d8484e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1654160448; _lxsdk=7D1AD970E25211ECB1087FE79CA2CCBE53A95C3A43A941FB9971A9B231090A07; _lx_utm=utm_source=Baidu&utm_medium=organic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1654161328; __mta=247380283.1654160448649.1654161250977.1654161328273.13; _lxsdk_s=18123a501d2-256-62d-f01||55',
    'User-Agent': ua,
    'Referer': 'https://www.maoyan.com/board?timeStamp=1654161327487&channelId=40011&index=2&signKey=fab2d36ee94c53f60d8d19db2362e7fc&sVersion=1&webdriver=false'
}


def RequestsTools(url):
    '''
    爬虫请求工具函数
    :param url: 请求地址
    :return: HTML对象 用于xpath提取
    '''
    response = requests.get(url, headers=headers).content.decode('utf-8')
    html = etree.HTML(response)
    return html


def Index(page):
    '''
    首页函数
    :param page: 页数
    :return:
    '''
    if page == 0:
        url = 'https://www.maoyan.com/board/4?timeStamp=1654160888721&channelId=40011&index=1&signKey=ba7330f7f83dbe59605987f09f882323&sVersion=1&webdriver=false'
    else:
        url = 'https://www.maoyan.com/board/4?timeStamp=1654160888721&channelId=40011&index=1&signKey=ba7330f7f83dbe59605987f09f882323&sVersion=1&webdriver=false&offset={}'.format(
            page)
    print('url', url)
    html = RequestsTools(url)
    # 详情页地址后缀
    urls_text = html.xpath('//a[@class="image-link"]/@href')
    # 评分
    pingfen1 = html.xpath('//i[@class="integer"]/text()')
    pingfen2 = html.xpath('//i[@class="fraction"]/text()')


    for i, p1, p2 in zip(urls_text, pingfen1, pingfen2):
        pingfen = p1 + p2
        urs = 'https://maoyan.com' + i
        # 反正请求太过于频繁
        time.sleep(2)
        Details(urs, pingfen)


def Details(url, pingfen):
    print(url)
    html = RequestsTools(url)
    print(html)
    dianyan = html.xpath('//h1[@class="name"]/text()')  # 电影名称
    leixing = html.xpath('//li[@class="ellipsis"]/a/text()')  # 类型
    diqu = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')  # 读取总和
    timedata = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')  # 时间
    for d, l, b, t in zip(dianyan, leixing, diqu, timedata):
        countyr = b.replace('\n', '').split('/')[0]  # 地区
        shichang = b.replace('\n', '').split('/')[1]  # 时长
        f = open('猫眼.csv', 'a')
        f.write('{}, {}, {}, {}, {}, {}, {}\n'.format(d, pingfen, url, l, countyr, shichang, t))
        print(d, pingfen, url, l, countyr, shichang, t)


for page in range(0, 11):
    page *= 10
    Index(page)
