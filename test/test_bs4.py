import re
from bs4 import BeautifulSoup

'''
# 这里是6-3 BeautifulSoup的语法 的笔记内容。可以通过删除三引号取消屏蔽状态
import re

# 根据HTML网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(
                    'html_doc',  # HTML文档字符串
                    'html.parser',  # HTML解析器
                    from_encoding='utf8'  # HTML文档的编码
                    )

# 搜索节点 方法：find_all(name, attrs, string)

# 查找所有标签为a的节点
soup.find_all('a')

# 查找所有标签为a，链接符合/view/123.htm形式的节点
soup.find_all('a', href='/view/123.htm')
soup.find_all('a', href=re.compile(r'view/\d+\.htm'))

# 查找所有标签为div，class为abc，文字为Python的节点
soup.find_all('div', class_='abc', string='Python')

# 得到节点：<a href='1.html'>Python</a>

# 获取查找到的节点的标签名称
# node.name

# 获取查找到的a节点的href属性
# node['href']

# 获取查找到的a节点的链接文字
# node.get_text()
'''


# 6-4 BeautifulSoup实例测试

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# python3 缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉, 故去掉，否则会报错

# 第一种方法
print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())


# 第二种方法
print('获取lacie的链接')
link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())


# 第三种方法
print('正则匹配')
link_node = soup.find('a', href=re.compile(r'ill'))
print(link_node.name, link_node['href'], link_node.get_text())


# 第四种方法
print('获取p段落文字')
p_node = soup.find('p', class_='title')
print(p_node.name, p_node.get_text())
