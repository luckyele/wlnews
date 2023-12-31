from selenium import webdriver  
from selenium.webdriver.common.by import By  
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.options import Options 

import sys, os, time

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
    options.add_argument('disable-gpu')
    options.add_argument('no-sandbox')
    options.add_argument('incognito')
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = Edge(executable_path=path, options=options)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', \
        {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                Safari/537.36 Edg/119.0.0.0'
        })

    return driver

def ready_to_grasp2():
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


def get_filename(url):
    filename = url.split("//")[1]
    return filename

def grasp_all_options(url, driver):
    assert(driver)
    driver.get(url)
      
    option_tags = driver.find_elements(By.TAG_NAME, "option")  
    filename = get_filename(url).rstrip('/')
    with open("./txt/" + filename + ".txt", 'w', encoding='utf-8') as f:  
        for tag in option_tags:
            print(tag.text, tag.get_attribute('value'))
            # f.write(tag.text + "\t" + tag.get_attribute('value')+ "\n" )

    driver.quit()

def grasp_all_a(url, driver):
    assert(driver)
    driver.get(url)   
    time.sleep(15)
    a_tags = driver.find_elements(By.TAG_NAME, "a")  
    # print(a_tags)

    filename = get_filename(url).rstrip('/')
    with open("./txt/" + filename+".txt", 'w', encoding='utf-8') as f:  
        for tag in a_tags:
            title = tag.get_attribute('title').replace('\n','').strip(' ')
            href = tag.get_attribute('href')
            if title and href:
                if 'javascript' not in href:
                    f.write(title + "\t" + href + "\n" )
            elif  href:
                    if 'javascript' in href:
                        continue
                    else:
                        f.write("\t" + href + "\n" )
    driver.quit()

if __name__ == "__main__":
    urls = [
        "https://www.ahlib.com/",
        "https://www.ahm.cn/",
        "http://www.ahswhg.cn/",
        "http://www.ahkaogu.com/",
        "http://www.anhuify.net/",
        "https://www.ahctic.cn/",
        "https://www.ahsmsg.com/",
        "https://wlj.hefei.gov.cn/",
        "http://wlt.huaibei.gov.cn/",
        # "https://wlt.bozhou.gov.cn/",
        "http://ct.ahsz.gov.cn/",
        "http://wtlj.bengbu.gov.cn/",
        "http://wlt.fy.gov.cn/",
        "http://wlj.huainan.gov.cn/",
        "http://ct.chuzhou.gov.cn/",
        "http://wlj.luan.gov.cn/",
        "http://wlj.mas.gov.cn/",
        "http://ct.wuhu.gov.cn/",
        "http://wlj.tl.gov.cn/",
        "http://whhlyj.chizhou.gov.cn/",
        "http://wlj.xuancheng.gov.cn/",
        "http://ct.anqing.gov.cn/",
        "http://wlj.huangshan.gov.cn/",
        "https://ct.ah.gov.cn",
    ]
    for url in urls:
        driver = ready_to_grasp()
        grasp_all_a(url, driver)
        time.sleep(10)