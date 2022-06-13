# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Logger.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import logging
from prettytable import PrettyTable


'''定义终端颜色'''
COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'pink': '\033[35m',
    'cyan': '\033[36m',
    'highlight': '\033[93m',
    'number': '\033[96m',
    'singer': '\033[93m',
    'flac': '\033[95m',
    'songname': '\033[91m'
}


'''打印日志类'''
class Logger():
    def __init__(self, logfilepath, **kwargs):
        setattr(self, 'logfilepath', logfilepath)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[logging.FileHandler(logfilepath), logging.StreamHandler()],
        )
    @staticmethod
    def log(level, message):
        logging.log(level, message)
    def debug(self, message, disable_print=False):
        if disable_print:
            fp = open(self.logfilepath, 'a')
            fp.write(message + '\n')
        else:
            Logger.log(logging.DEBUG, message)
    def info(self, message, disable_print=False):
        if disable_print:
            fp = open(self.logfilepath, 'a')
            fp.write(message + '\n')
        else:
            Logger.log(logging.INFO, message)
    def warning(self, message, disable_print=False):
        message = colorize(message, 'red')
        if disable_print:
            fp = open(self.logfilepath, 'a')
            fp.write(message + '\n')
        else:
            Logger.log(logging.WARNING, message)
    def error(self, message, disable_print=False):
        message = colorize(message, 'red')
        if disable_print:
            fp = open(self.logfilepath, 'a')
            fp.write(message + '\n')
        else:
            Logger.log(logging.ERROR, message)


'''打印表格'''
def printTable(title, items):
    assert isinstance(title, list) and isinstance(items, list), 'title and items should be list'
    table = PrettyTable(title)
    for item in items: table.add_row(item)
    print(table)
    return table


'''给终端文字上色'''
def colorize(string, color):
    string = str(string)
    if color not in COLORS: 
        return string
    return COLORS[color] + string + '\033[0m'