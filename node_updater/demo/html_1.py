from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
import time


#month, date = time.strftime('%m %d').split(' ')
#format_time = str(int(month)) + '.' + str(int(date))
format_time = '6.22'

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

contents = driver.find_elements(By.CSS_SELECTOR, 'td > a')

for item in contents:
    print(item.text)