"""
print_msg_to_log_model.py
监听所有的print到log日志 封装类 PrintLogger
Version: 1.0
Author: LC
DateTime: 2019年3月11日14:49:32
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import sys
import os


class PrintLogger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a+", encoding="utf-8")  # r(只读），r+（读写），w（只写）, w+（读写）， a(追加），a+（追加读）

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
