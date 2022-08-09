import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://shopmrbeast.com/slap-to-win');
time.sleep(5)
slapIdiot = driver.find_element_by_id('slapper-face')
while True:
    slapIdiot.send_keys(Keys.ENTER)

driver.quit()