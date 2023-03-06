from selenium import webdriver
import time
#from time import *

# moje_pierwsze_okno_chrome = webdriver.Chrome()
# moje_pierwsze_2_chrome = webdriver.Chrome()
# moje_pierwsze_1_firefox = webdriver.Firefox()

driver = webdriver.Chrome()
driver.get('https://google.com')

button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()


time.sleep(2)
#sleep(2)
driver.quit()

