from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

def make_screenshot(okno_przegladarki):
    teraz = datetime.datetime.now()
    nazwa = 'screenshot' + teraz.strftime('%H%M%S') + '.png'
    okno_przegladarki.get_screenshot_as_file(nazwa)

#from time import *
# moje_pierwsze_okno_chrome = webdriver.Chrome()
# moje_pierwsze_2_chrome = webdriver.Chrome()
# moje_pierwsze_1_firefox = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('https://google.com')
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
pole_szukaj = driver.find_element('name','q')
pole_szukaj.send_keys('Dokąd nocą tupta jez?')
pole_szukaj.send_keys(Keys.ENTER)
#przycisk_szukaj = driver.find_element('name', 'btnK')
#przycisk_szukaj.submit()
time.sleep(1)

make_screenshot(driver)
driver.quit()

