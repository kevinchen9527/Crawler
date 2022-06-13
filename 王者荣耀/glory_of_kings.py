# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:glory_of_kings.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import os
import time
import requests

hero_url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {
    'Cookie': 'pgv_pvid=6659127930; ptui_loginuin=100823443; pt_sms_phone=186******16; RK=AJtpm7i0RF; ptcz=1464cc228492e8e1432f0a0ca762896e9a5cbffbadd182d9d5af9f56f0db0648; eas_sid=01d6R5b2o356J1s1z6B9t7c5K4; tvfe_boss_uuid=6664ce0a6a1a0c4c; Qs_lvt_323937=1653468840; Qs_pv_323937=2791758346309558000; LW_sid=e176T5e3p4D6t808576003Q5H7; LW_uid=91k6r5n344R628Z8v7i0j3T5P8; pgv_info=ssid=s8951714952; _qpsvr_localtk=0.9169185253869083; pvpqqcomrouteLine=index_wallpaper_a20190620material_herolist_skinDetail_herodetail_skinDetail',
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'Referer': 'https://pvp.qq.com/',
}
hero_list_info = requests.get(hero_url, headers=headers)
hero_list_json = hero_list_info.json()
hero_name = list(map(lambda x: x['cname'], hero_list_json))
hero_number = list(map(lambda x: x['ename'], hero_list_json))


def down_loader():
    """
    下载
    :return:
    """
    i = 0
    for j in hero_number:
        os.chdir('d:\\Users\\Administrator\\Desktop\\wzry\\')
        # 1 创建文件夹
        os.mkdir('d:\\Users\\Administrator\\Desktop\\wzry\\' + hero_name[i])
        # 2 进入创建好的文件夹
        os.chdir('d:\\Users\\Administrator\\Desktop\\wzry\\' + hero_name[i])
        i += 1
        # 开始拼接图片地址
        for k in range(1, 11):
            time.sleep(3)
            url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + "/" + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(url)
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)
                print("完成了" + hero_name[i] + "的第" + str(k) + "张图")


down_loader()
