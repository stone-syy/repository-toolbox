#!/usr/bin/python
# Desc: 这是一个小小的工具箱，包括了Telnet、MD5、sha1摘要算法等小工具
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
from font import font_list
import re
import os


class Basic(object):

    """这个类是集合了Toolbox类中可能复用的功能函数，包括IP地址校验、hash摘要算法等"""

    def __init__(self):
        self.__doc__ = '主类中可能复用的功能函数'

    def hash(self, pwd, method=md5()):

        """这个函数是对用户输入的字符串进行hash，并返回hash值"""
        try:
            if pwd == '':
                msg.showwarning(title='Warn', message='没有输入内容，请输入！')
            else:
                password = pwd
                hash_method = method
                hash_method.update(password.encode('utf-8'))
                return hash_method.hexdigest()
        except:
            msg.showinfo(title='Info', message='遇到了一个不可描述的错误')

    def ip_check(self, ip):

        """这个函数利用re库对用户输入的IP地址进行合法性校验"""

        try:
            rule = re.compile(r'^([1-9][0-9]{1,2})\.([1-9][0-9]{1,2})\.([1-9][0-9]{1,2})\.([1-9][0-9]{1,2})$')
            result = rule.match(ip)
            return result
        except:
            msg.showinfo(title='Info', message='The is a error'.title())
        #finally:
            #pass

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
        self.telnet_tag = Label(self.frame_1, text='请输入IP/ Port:', font=('Aria', 10))
        self.str_tag = Label(self.frame_1, text='请输入Path/Str:', font=('Aria', 10))

        # create enter
        self.ip_enter = Entry(self.frame_1, width=30)
        self.port_enter = Entry(self.frame_1, width=10)
        self.str_enter = Entry(self.frame_1, width=41)

        # create button
        self.telnetb = Button(self.frame_2, text='Telnet', width=7, command=self._telnet)
        self.pingb = Button(self.frame_2, text='NetPing', width=7)
        self.md5b = Button(self.frame_2, text='md5', width=7, command=self._md5)
        self.sha1b = Button(self.frame_2, text='sha1', width=7, command=self._sha1)
        self.sha128b = Button(self.frame_2, text='sha224', width=7, command=self._sha128)
        self.sha256b = Button(self.frame_2, text='sha256', width=7, command=self._sha256)
        self.sha512b = Button(self.frame_2, text='sha512', width=7, command=self._sha512)
        self.filenum = Button(self.frame_2, text='文件数量', width=7, command=self._file_num)
        self.listfile = Button(self.frame_2, text='列出文件', width=7, command=self._list_file)
        self.cleanb = Button(self.frame_2, text='清除记录', width=7, command=self._clean)
        self.exitb = Button(self.frame_2, text='退出程序', width=7, command=sys.exit)

        # 文本框和滚动条
        self.text = Text(self.frame_3)
        self.scroball = Scrollbar(self.frame_3, command=self.text.yview)

        # frame 投放
        self.frame_1.grid(row=0, column=0)
        self.frame_2.grid(row=1, column=0, pady=2)
        self.frame_3.grid(row=2, column=0)

        # module 摆放
        self.telnet_tag.grid(row=0, column=0)
        self.ip_enter.grid(row=0, column=1)
        self.port_enter.grid(row=0, column=2, padx=2)
        self.str_tag.grid(row=1, column=0)
        self.str_enter.grid(row=1, column=1, columnspan=2)
        self.telnetb.grid(row=0, column=0)
        self.pingb.grid(row=0, column=1)
        self.md5b.grid(row=0, column=2)
        self.sha1b.grid(row=0, column=3)
        self.sha128b.grid(row=0, column=4)
        self.sha256b.grid(row=0, column=5)
        self.sha512b.grid(row=0, column=6)
        self.filenum.grid(row=1, column=0)
        self.listfile.grid(row=1, column=1)
        self.cleanb.grid(row=1, column=2)
        self.exitb.grid(row=1, column=3)

        self.text.grid(row=0, column=0)
        self.scroball.grid(row=0, column=1)
        self.text.config(yscrollcommand=self.scroball.set, width=43, height=20, font=font_list[4])

        # 功能函数

    def _telnet(self):
        """telnet 函数"""
        ip_address = self.ip_enter.get()
        port = self.port_enter.get()
        if ip_address and port != '':
            if Basic().ip_check(ip=self.ip_enter.get()) is None:
                msg.showerror(title='Error', message='ip address error,please check')
            else:
                connect = Telnet(host=ip_address, port=port, timeout=3)
                connect_info = connect.sock
                info = ('src:', str(connect_info).split('=')[5].split('(')[1].split(')')[0],
                        'dst:', str(connect_info).split('=')[6].split('(')[1].split(')')[0])
                self.text.insert(0.0, info)
                self.ip_enter.delete(0, END)
                self.port_enter.delete(0, END)
        elif ip_address == '':
            msg.showerror(title='Error', message='missing IP parameters'.title())
        elif port != '':
            msg.showwarning(title='Error', message='missing port parameters'.title())
        # elif port == '' and ip_address != '':
            # msg.showwarning(title='Warning', message='missing port parameters'.title())
    # except:
        # msg.showerror(title='Error', message='遇到了一个不可描述的错误')

    def _ping(self):
        pass

    def _md5(self):
        md5_value = Basic().hash(pwd=self.str_enter.get())
        if self.str_enter.get() == '':
            pass
        else:
            self.text.insert(0.0, '你输入的字符为%s;\nmd5值为: %s' % (self.str_enter.get(), md5_value))
            self.str_enter.delete(0, END)

    def _sha1(self):
        sha1_value = Basic().hash(pwd=self.str_enter.get(), method=sha1())
        if self.str_enter.get() == '':
            pass
        else:
            self.text.insert(0.0, '你输入的字符为%s;\n sha1值为：%s' % (self.str_enter.get(), sha1_value))
            self.str_enter.delete(0, END)

    def _sha128(self):
        sha224_value = Basic().hash(pwd=self.str_enter.get(), method=sha224())
        if self.str_enter.get() == '':
            pass
        else:
            self.text.insert(0.0, '你输入的字符为%s;sha224值为：%s' % (self.str_enter.get(), sha224_value))
            self.str_enter.delete(0, END)

    def _sha256(self):
        sha256_value = Basic().hash(pwd=self.str_enter.get(), method=sha256())
        if self.str_enter.get() == '':
            pass
        else:
            self.text.insert(0.0, '你输入的字符为%s;sha256值为:%s' % (self.str_enter.get(), sha256_value))
            self.str_enter.delete(0, END)

    def _sha512(self):
        sha512_value = Basic().hash(pwd=self.str_enter.get(), method=sha512())
        if self.str_enter.get() == '':
            pass
        else:
            self.text.insert(0.0, '你输入的字符为%s;sha512值为%s' % (self.str_enter.get(), sha512_value))
            self.str_enter.delete(0, END)

    def _file_num(self):
        file_path = self.str_enter.get()
        if file_path == '':
            pass
        else:
            if os.path.exists(file_path):
                file_sum = 0
                for root, dirs, files in walk(file_path):
                    for file in files:
                        file_sum += 1
                msg.showinfo(title='Info', message='文件路径：{}；文件数量{}'.format(file_path, file_sum))
            else:
                msg.showerror(title='error', message='path not exits'.title())

    def _list_file(self):
        file_path = self.str_enter.get()
        if file_path == '':
            msg.showerror(title='Error', message='None')
        else:
            if os.path.exists(file_path):
                file = os.listdir(file_path)
                for files in file:
                    if os.path.isfile(os.path.join(file_path, files)):
                        self.text.insert(0.0, '%s\n' % files)
            else:
                msg.showerror('Error', message='file path not found'.title())

    def _clean(self):
        self.text.delete(0.0, END)


# 事件循环


window = Tk()
window.title('Tool Box')
window.iconbitmap('ico.ico')
App = Toolbox(window)
window.mainloop()





