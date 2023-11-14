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
import os, sys


def ready_to_grasp():
    path = r"d:\\webdriver\\MicrosoftWebDriver.exe"
    if os.path.exists(path):
        sys.path.append(path)
    else:
        print("Please install webdriver first.\n")
        exit(-1)

    options = EdgeOptions()
    options.use_chromium = True 
    options.add_argument('headless') 
    options.add_argument("disable-blink-features=AutomationControlled")
    # options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
    # options.add_experimental_option('excludeSwitches', ['enable-automation']) 
    # options.add_argument('disable-blink-features=AutomationControlled')
    # options.add_experimental_option('detach', True)
    driver = Edge(executable_path=path, options=options) 
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", \
        {"headers": {
            "sec-ch-ua-platform": "Windows",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}})
    return driver

url = "http://wlj.luan.gov.cn/"
driver = ready_to_grasp()
driver.get(url)   
a_tag = driver.find_element(By.TAG_NAME, "body")  
print(a_tag.text)
driver.quit()