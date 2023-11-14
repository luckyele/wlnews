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
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import requests
from bs4 import BeautifulSoup
import re
import os, sys, time


def ready_to_grasp():
    path = r"d:\\webdriver\\MicrosoftWebDriver.exe"
    if os.path.exists(path):
        sys.path.append(path)
    else:
        print("Please install webdriver first.\n")
        exit(-1)
    
    os.popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222')
    options = EdgeOptions()
    options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
    driver = Edge(executable_path=path, options=options) 
    return driver

url = "http://wlt.bozhou.gov.cn/"
driver = ready_to_grasp()
driver.get(url) 
# script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
# driver.execute_script(script)  
# a_tag = driver.find_element(By.TAG_NAME, "a")  
# print(a_tag.text)
time.sleep(5)
html = driver.page_source
print(html)
driver.quit()