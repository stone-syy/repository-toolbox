# 导入包
from tkinter import *
from time import *
import sys, os, hashlib
from tkinter import messagebox as messagebox
# 开始
def app():
    # encryption function
    def encrypt():
        pwd = enter_2.get()
        try:
            if pwd == '':
                messagebox.showerror(title='Error', message='没有输入内容！')
            elif pwd != '':
                sha1 = hashlib.sha1()
                sha1.update(pwd.encode('utf-8'))
                messagebox.showinfo(title='123', message='SHA1密文为:%s' % sha1.hexdigest())
            else:
                pass
        except:
            messagebox.showerror(title='Error', message='遇到一个不可描述的错误！')

    # find file and dir
    def find_dir_file():
        path = enter_2.get()

    # 清除函数
    def clean():
        msg.delete(0.0, END)

    # 定义窗口
    window = Tk()
    window.title('MyTool')
    window.iconbitmap('qie.ico')

    # 创建容器
    container_1 = Frame(width=170, height=50)
    container_2 = Frame(width=170, height=50)
    container_3 = Frame(width=40, height=50)
    container_4 = Frame(width=190, height=60)
    container_5 = Frame(width=170, height=100)

    # 创建标签
    label_1 = Label(container_1, text='请输入你想查找的路径:', font=('Arial', 12), fg='black')
    label_2 = Label(container_1, text='请输入你加密的字符串:', font=('Arial', 12), fg='black')

    # 创建输入框
    enter_1 = Entry(container_2, width=100)#pack(side=TOP)
    enter_2 = Entry(container_2, width=100)#pack(side=TOP)

    # 创建按钮
    font = ['Verdana', 'Arial']
    button_1 = Button(container_4, text='sha1加密', font=font[0], command=encrypt)
    button_2 = Button(container_4, text='sha 256', font=font[0])
    button_3 = Button(container_4, text='sha 512', font=font[0])
    button_4 = Button(container_4, text='md5 加密', font=font[0])
    button_5 = Button(container_4, text='列出目录', font=font[0])
    button_6 = Button(container_4, text='列出文件', font=font[0])
    button_7 = Button(container_4, text='清除记录', font=font[0])
    button_8 = Button(container_4, text='文件数量', font=font[0])
    button_9 = Button(container_4, text='退出程序', font=font[0])

    # 创建文本框
    msg = Text(container_4)
    msg.config(fg='#008c00')
    msg.bind_all('<keyPress-Return>', clean())

    # 固定大小
    container_1.grid_propagate(0)
    container_2.grid_propagate(0)
    container_3.grid_propagate(0)
    container_4.grid_propagate(0)
    container_5.grid_propagate(0)


    # 窗口布局
    container_1.grid(row=0, column=0)
    container_2.grid(row=0, column=1)
    container_3.grid(row=0, column=2)
    container_4.grid(row=1, column=0)
    container_5.grid(row=2, column=0)

    # 控件布局
    label_1.grid(row=0, column=0)
    label_2.grid(row=1, column=0)
    enter_1.grid(row=0, column=0, pady=2)
    enter_2.grid(row=1, column=0)
    button_1.grid(row=1, column=0)


    # 消息循环
    window.mainloop()

# 调用主函数


app()







