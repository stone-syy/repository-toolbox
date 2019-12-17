#!/bin/python
# data time:2019-12-17
# Author: Mr.shi
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

# create My_app class
class Myapp(object):

    """这个类是主类，包括定义GUI界面的框架、各种组件以及组件的位置顺序和摆放
       还有各个功能函数也将在这个类中"""

    def __init__(self, master):
        self.__doc__ = '主类，包括了界面框架和组件定义及功能函数定义'
        self.master = master
        self.widgest()

    def widgest(self):
        # create frame
        frame_1 = Frame()
        frame_2 = Frame()
        frame_3 = Frame()

        # create gui module
        telnet_tag = Label(text='请输入IP/Port:', font=('Aria', 12))
        str_tag = Label(text='请输入Path/Str:', font=('Aria', 12))

        # create enter
        ip_enter = Entry()
        port_enter = Entry()
        str_enter = Entry()





