# -*- coding: utf-8 -*-


from urllib.request import urlopen
res = urlopen('http://just-the-time.appspot.com/')
result = res.read().strip()
print(result)
#b'2017-07-28 04:53:46'
result_str = result.decode('utf-8')
print(result_str[:10])
#'2017-07-28 04:53:46'

def get_current_date():
    return result_str[:10]