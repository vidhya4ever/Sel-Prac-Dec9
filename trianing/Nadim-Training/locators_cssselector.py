#url : https://demowebshop.tricentis.com/login

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()
# time.sleep(1)
# driver.find_element('css selector','input[id="Email"]').send_keys('123@gmail.com')
# time.sleep(2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#url : https://www.myntra.com/

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(1)
# driver.find_element('css selector','input[class="desktop-searchBar"]').send_keys('iphone')
# time.sleep(2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#url: https://www.facebook.com/
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element('css selector','a[data-testid="open-registration-form-button"]').click()
time.sleep(1)
driver.find_element('name','firstname').send_keys('vidhyalakshmi')
time.sleep(1)
driver.find_element('name','lastname').send_keys('v')
time.sleep(1)
driver.find_element('css selector','input[value="1"]').click()
time.sleep(1)
driver.find_element('css selector','input[name="reg_email__"]').send_keys('vv.vidhya@gmail.com')
time.sleep(2)
driver.find_element('css selector','button[name="websubmit"]').click()
time.sleep(1)
