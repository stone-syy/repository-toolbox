#!/usr/bin/python
# data time: 2019-12-17
# Author: Mr.shi
# E-mail: example@qq.com
# version:1.0.0

"""
change log:
    pass
"""
from hashlib import *
from tkinter import *
from os import path, listdir, walk
from tkinter import messagebox as msg
from telnetlib import Telnet
import re


class Basic(object):

    """这个类是集合了Toolbox类中可能复用的功能函数，包括IP地址校验、hash摘要算法等"""

    def __init__(self):
        self.__doc__ = '主类中可能复用的功能函数'

    def hash(self, pwd, method):

        """这个函数是对用户输入的字符串进行hash，并返回hash值"""

        password = pwd
        hash_method = method
        hash_method.update(password.encode('utf-8'))
        return hash_method.hexdigest()

    def ip_check(self, ip):

        """这个函数利用re库对用户输入的IP地址进行合法性校验"""

        pass

    def clean(self):

        """这个函数是清除text文本框中的所有内容"""

        pass


# create My_app class
class Toolbox(object):

    """这个类是主类，包括定义GUI界面的框架、各种组件以及组件的位置顺序和摆放
       还有各个功能函数也将在这个类中"""

    def __init__(self, master):
        self.__doc__ = '主类，包括了界面框架和组件定义及功能函数定义'
        self.master = master
        self.widgets()

    def widgets(self):

        """定义组件及组件位置"""

        # create frame
        self.frame_1 = Frame()
        self.frame_2 = Frame()
        self.frame_3 = Frame()

        # create gui module
        self.telnet_tag = Label(self.frame_1, text='请输入IP/ Port:', font=('Aria', 12))
        self.str_tag = Label(self.frame_1, text='请输入Path/Str:', font=('Aria', 12))

        # create enter
        self.ip_enter = Entry(self.frame_1, )
        self.port_enter = Entry(self.frame_1, )
        self.str_enter = Entry(self.frame_1, )

        # create button
        self.telnetb = Button(text='Telnet', width=7, font=('Aria', 10))
        self.pingb = Button(text='ping', width=7, font=('Aria', 10))
        self.md5b = Button()
        self.sha1b = Button()
        self.sha128b = Button()
        self.sha256b = Button()
        self.sha512b = Button()
        self.filenum = Button()
        self.listfile = Button()
        self.exitb = Button()
        self.aboveb = Button()

        # frame 投放
        self.frame_1.grid(row=0, column=0)
        self.frame_2.grid(row=1, column=0)
        self.frame_3.grid(row=2, column=0)

        # module 摆放
        self.telnet_tag.grid(row=0, column=0)
        self.ip_enter.grid(row=0, column=1)
        self.port_enter.grid(row=0, column=2)
        self.str_tag.grid(row=1, column=0)
        self.str_enter.grid(row=1, column=1)

        # 功能函数

    def _telnet(self):
        pass

    def _ping(self):
        pass

    def _md5(self):
        pass

    def _sha1(self):
        pass

    def _sha128(self):
        pass

    def _sha256(self):
        pass

    def _sha512(self):
        pass

    def _file_num(self):
        pass

    def _list_file(self):
        pass


# 事件循环


window = Tk()
window.title('Tool Box')
App = Toolbox(window)
window.mainloop()





