from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
import time


#month, date = time.strftime('%m %d').split(' ')
#format_time = str(int(month)) + '.' + str(int(date))
format_time = '7.3'

#ignore warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service = Service('.\\bin\\chromedriver.exe'), options = options)

driver.get('https://gitlab.com/youtube-aweikeji/TG-aweikeji/-/blob/main/7/7.3/7.3-cl')

ele = driver.find_element(By.CSS_SELECTOR, "[class = 'js-file-title file-title-flex-parent']")

WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[class = 'js-file-title file-title-flex-parent']")))

line1 = driver.find_element(By.ID, "LC1")

#WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[class="gl-display-flex"]')))
