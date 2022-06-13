# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:setup.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import musicdl
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=musicdl.__title__,
    version=musicdl.__version__,
    description=musicdl.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=musicdl.__author__,
    url=musicdl.__url__,
    author_email=musicdl.__email__,
    license=musicdl.__license__,
    include_package_data=True,
    entry_points={'console_scripts': ['musicdl = musicdl.musicdl:musicdlcmd']},
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages()
)