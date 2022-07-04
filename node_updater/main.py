# Author: zch9241
# Licence: No licence.All rights reserved
# version: 0.1-Alpha
# 基于Python selenium，获取订阅链接并复制到剪贴板
# 
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

keys = ['cl', 'xhj', 'shadowrocket', '.gitkeep']

month, date = time.strftime('%m %d').split(' ')
format_time = str(int(month)) + '.' + str(int(date))
#format_time = '6.22'

#ignore warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service = Service('.\\bin\\chromedriver.exe'), options = options)

driver.get(url = 'https://gitlab.com/youtube-aweikeji/TG-aweikeji/-/find_file/main')

WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'file_find')))

InputBox = driver.find_element(By.ID, 'file_find')
InputBox.click()
InputBox.send_keys(format_time)

time.sleep(2)

def reader():
    """
    若不能从文件名获取，则阅读文件
    """
    def key_find():
        for key in keys:
            if key in link.lower(): 
                return True
            else:
                continue
        return False
    
    contents_ = driver.find_elements(By.CSS_SELECTOR, 'td > a')
    
    for con in contents_:
        link = con.get_attribute('href')
        if key_find() == False:
            driver.get(link)

            WebDriverWait(driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, "[class = 'js-file-title file-title-flex-parent']")
                    ))

            line1 = driver.find_element(By.ID, "LC1").text
            if 'port' not in line1:
                url = driver.find_element(By.CSS_SELECTOR, '[title="Open raw"]').get_attribute('href')
                return url
            else:
                continue
    return None
    
    #leng = len(contents_)
    #for i in range(leng):
    #    item_ = driver.find_elements(By.CSS_SELECTOR, 'td > a')[i]
    #    item_.click()


def searcher():
    contents = driver.find_elements(By.CSS_SELECTOR, 'td > a')
    for _item in contents:
        #e.g. '7/7.3/7.3-cl'
        text = _item.text.lower()
        s = text.split('/')[-1].replace('.', '')
        f = format_time.replace('.', '')

        #判断是否为当日的链接
        if f not in s:
            continue

        if 'v2' in text:
            _item.click()
            url = driver.find_element(By.CSS_SELECTOR, '[title="Open raw"]').get_attribute('href')
            return url
        else:
            continue
    result = reader()
    if result != None:
        return result

    print('[main-searcher] WARN : 没有元素符合要求')
    return None

url = searcher()

print('[main] INFO : 成功获取订阅链接 {}'.format(url))
pyperclip.copy(url)
print('[main] INFO : 订阅链接已复制到剪贴板')
