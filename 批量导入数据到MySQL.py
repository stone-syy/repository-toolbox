import mysql.connector
import time
print('开始连接数据库'.center(30, '*'))
start = time.time()
connect = mysql.connector.connect(host='192.168.137.22', user='admin', password='123456', database='sgk')
cursor = connect.cursor()
print('数据库连接成功'.center(30, '*'))
row = 0
print('现在开始处理')
with open(r'D:\sfz.txt', 'r', encoding='GB2312', errors='ignore') as file:
    for info in file:
        if info == '\n' or info == '':
            continue
        else:
            row = row + 1
            print("\r处理第{}行数据中".format(row), end="")
            #print(info.split('----')[0].strip(), info.split('----')[1].strip())
            cursor.execute('insert into sgk.sfzinfo(username,codes,bank_card,kind,dates) '
                           'value (%s, %s, %s,%s,%s)',
                        (info.split('----')[0].strip(), info.split('----')[1].strip(),
                         '', 'sfz', '2019-2-20'))
cursor.close()
connect.commit()
connect.close()
end = time.time()
print('耗时：{:.2f}'.format(end-start))

