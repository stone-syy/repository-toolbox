import re, sys
import time
a = r'([1-9][0-9]{0, 2})\.([1-9][0-9]{1, 2})\.([1-9][0-9]{0, 2})\.([1-9][0-9]{0, 2})$'
b = re.match(r'([1-9][0-9]{0,2})\.', '192.168.137.239')
print(b)
print(sys.path)
print('{:.5f}'.format(time.time()))
