from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.instagram.com/')

driver.maximize_window()

driver.implicitly_wait(10)

username = driver.find_element_by_name('username')
username.send_keys('ayo_theblackguy')
username.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

password = driver.find_element_by_name('password')
password.send_keys('ayoain4609')
password.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

save = driver.find_element_by_class_name('cmbtv')
save.click()

not_now = driver.find_element_by_class_name('mt3GC')
not_now.click()

profile = driver.find_element_by_class_name('gmFkV')
profile.click()

saved = driver.find_element_by_class_name('W9_iZ')
saved.click()

allpost = driver.find_element_by_class_name('Ec1_p')
allpost.click()

n_scrolls = 4000
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

driver.implicitly_wait(10)

time.sleep(300)

driver.quit()
