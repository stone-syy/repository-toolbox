from telnetlib import Telnet
connect = Telnet(host='127.0.0.1', port=8080, timeout=3)
sock = connect.sock
if sock is not None:
    print('s')
else:
    print('f')

