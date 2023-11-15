'''
抽取页面主体内容
这里需要算法设计

'''
# 算法1 
# 这个算法用到了 Scrapy 框架
# sel = {
#     'value': 0,
#     'node': None
# }
# def find(node, sel):
#     value = 0
#     for n in node.xpath("*"):
#         if n.xpath("local-name()").get() == "p":
#             t = "".join([s.strip() for s in (n.xpath('text()').getall() + n.xpath("*/text()").getall())])
#             value += len(t)
#         else:
#             value += find(n, a)*0.5
#     if value > sel["value"]:
#         sel["node"] = node
#         sel["value"] = value
#     return value
#
# find(response.xpath("body"), sel)
# print(sel.node)
# from selenium import webdriver  
# from selenium.webdriver.common.by import By  
# from msedge.selenium_tools import EdgeOptions
# from msedge.selenium_tools import Edge
import requests
from bs4 import BeautifulSoup
# import re
# import os, sys, time


# def ready_to_grasp():
#     path = r"d:\\webdriver\\MicrosoftWebDriver.exe"
#     if os.path.exists(path):
#         sys.path.append(path)
#     else:
#         print("Please install webdriver first.\n")
#         exit(-1)
    
#     os.popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222')
#     options = EdgeOptions()
#     options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
#     driver = Edge(executable_path=path, options=options) 
#     return driver

url = "http://ct.ah.gov.cn/"
# driver = ready_to_grasp()
r = requests.get(url) 
try:
    print(r.apparent_encoding)	#	返回内容编码
    # print(r.content)	#	返回响应的内容（以字节为单位）
    print(r.cookies)	#	返回一个 CookieJar 对象，其中包含从服务器返回的 cookies
    print(r.elapsed)	#	返回一个 timedelta 对象，该对象包含从发送请求到到达响应所经过的时间
    print(r.encoding)	#	返回用于解码 r.text 的编码
    print(r.headers)	#	返回响应头的字典
    print(r.history)	#	返回包含请求历史记录（url）的响应对象列表
    print(r.is_permanent_redirect)	#	如果响应是永久重定向 url，则返回 True，否则返回 False
    print(r.is_redirect)	#	如果响应被重定向，则返回 True，否则返回 False
    print(r.links)	#	返回标头链接
    print(r.next)	#	为重定向中的下一个请求返回 PreparedRequest 对象
    print(r.ok)	#	如果状态代码小于 400，则返回 True，否则返回 False
    print(r.reason)	#	返回与状态代码对应的文本
    print(r.request)	#	返回请求此响应的请求对象
    print(r.status_code)	#	返回指示状态的数字（200 正常，404 未找到）
    # print(r.text)	#	以 unicode 格式返回响应的内容
    print(r.url)	#	返回响应的 URL
except:
    r.close()

