from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from selenium.common.exceptions import StaleElementReferenceException

import sys, os, time

def ready_to_grasp():
    path = r"d:\\webdriver\\MicrosoftWebDriver.exe"
    if os.path.exists(path):
        sys.path.append(path)
    else:
        print("Please install webdriver first.\n")
        exit(-1)
    
    os.popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222')
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    options.add_argument('no-sandbox')
    options.add_argument('incognito')
    options.add_argument("disable-blink-features=AutomationControlled")
    
    options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
    driver = Edge(executable_path=path, options=options)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', \
        {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                Safari/537.36 Edg/119.0.0.0'
        })

    return driver

def get_filename(url):
    filename = url.split("//")[1]
    return filename

def get_tags(driver):
    tmp = []
    a_tags = driver.find_elements(By.TAG_NAME, "a")  
    for tag in a_tags:
        if tag.get_attribute('href') == 'about:blank' and len(tag.get_attribute('title')) != 0: 
                if tag.get_attribute('title') not in tmp:
                    tmp.append(tag)
    return tmp

def grasp_all_a2(url, driver):
    
    driver.get(url)
    time.sleep(10)   #waiting for load webpages

    a_tags = get_tags(driver)
    print(len(a_tags))
        
    tmp = a_tags
    titles = []
    for i in range(len(a_tags)):
        href =  tmp[i].get_attribute('href')
        if href == 'about:blank':
            titles.append(tmp[i].get_attribute('title'))
    
    # for i, t in enumerate(titles):
    #     print("{}{}".format(i, t))
    fresh_drv = driver
    bk_titles = titles
    i = 0
    
    rlts = []
    while len(bk_titles) > 0:
        titles = bk_titles
        for i in range(len(titles)):
            try:
                # print("{}{}".format(i, titles[i]))
                fresh_drv.find_element_by_link_text(titles[i]).click()
                time.sleep(5)
            except:
                continue
            r = "{}\t {}".format(titles[i], driver.current_url)
            print(r)
            rlts.append(r)
            start_time = time.time()
            bk_titles.remove(titles[i])
            print("Left {} items.".format(len(bk_titles)))
            
            fresh_drv.back()
            time.sleep(1)
        end_time = time.time() 
        if (end_time - start_time) > 50.0:
            break
    
    filename = get_filename(url).rstrip('/')
    with open("./txt/" + filename+".txt", 'w', encoding='utf-8') as f:  
        for rlt in rlts:
            f.write(rlt + "\n" )


if __name__ == "__main__":
    # for url in urls:
    driver = ready_to_grasp()
    grasp_all_a2("https://wlt.bozhou.gov.cn/", driver)
    time.sleep(3)
    driver.quit()
