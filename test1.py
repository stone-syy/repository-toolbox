import telnetlib
a = telnetlib.Telnet(host='192.168.137.239', port=22, timeout=3)
b = a.sock
print(b)
c = str(b).split('=')[6].split('(')[1].split(')')[0]
print('src:', c)

