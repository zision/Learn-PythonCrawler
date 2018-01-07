import http.cookiejar
from urllib import request

url = 'http://www.baidu.com'

print('第一种方法')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('\n第二种方法')
req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print('\n第三种方法')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
