from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys("UNASP")
driver.find_element_by_name("btnK").submit()

driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="slider-135-slide-284-layer-24"]/rs-layer-wrap[4]/rs-loop-wrap/rs-mask-wrap').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]/div[2]/h3').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/a[1]').click()

time.sleep(60)
