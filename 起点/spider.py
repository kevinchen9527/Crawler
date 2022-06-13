# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:spider.py
@Time:2022/5/11 13:31

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

import requests  # 发送请求
import re
from bs4 import BeautifulSoup

# 伪装
headers = {
    'cookie': '_yep_uuid=b1421b7f-11da-b15f-a3ad-95316478f93c; e1=%7B%22pid%22%3A%22qd_P_read%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_P_read%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; newstatisticUUID=1648708045_1995757040; _csrfToken=mAWbsvESMNwir4NfKBy5fy8RedwvNBabTq3PLx6r; fu=721555856; _gid=GA1.2.1193345906.1648708045; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; e2=; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; rcr=1031788647%2C1031920667; bc=1031920667%2C1031788647; pageOps=1; lrbc=1031788647%7C686160165%7C0%2C1031920667%7C695153167%7C1; _ga_FZMMH98S83=GS1.1.1648708044.1.1.1648708759.0; _ga_PFYW0QLV3P=GS1.1.1648708044.1.1.1648708759.0; _ga=GA1.2.777546916.1648708045',
    'referer': 'https://book.qidian.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}
url = 'https://book.qidian.com/info/1019664125/#Catalog'
html_data = requests.get(url=url, headers=headers).text
# info_list = re.findall(
#     '<h2 class="book_name"><a href="(.*?)" target="_blank" data-eid=".*?" data-cid=".*?" alt=".*?" title=".*?">(.*?)</a></h2>',
#     html_data)
soup = BeautifulSoup(html_data, 'html.parser')
info_list = soup.findAll('h2')
print(info_list)
# print(len(info_list))
for results in info_list:
    link = 'https:' + results['href']
    # 1. 发送请求
    response = requests.get(url=link, headers=headers)
    # 2. 获取数据
    link_data = response.text
    # print(html_data)
    # 3. 解析数据
    # 网页标签 <p></p> <a></a> <div></div> <img />
    # <div class="read-content j_readContent" id=".*?">(.*?)</div>
    text = re.findall('<div class="read-content j_readContent" id=".*?">(.*?)</div>', link_data, re.S)[0]
    text = text.replace('<p>', '\n')
    text = results['alt'] + '\n\n' + text
    # 4. 保存数据
    with open('大奉打更人.txt', mode='a', encoding='utf-8') as f:
        f.write(text)
