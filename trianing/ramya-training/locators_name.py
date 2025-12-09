## url : https://www.instagram.com/accounts/login/?hl=en

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(opts)
# driver.get('https://www.instagram.com/accounts/login/?hl=en')
# time.sleep(2)
# driver.maximize_window()
# driver.find_element('name','username').send_keys('vidhyalakshmi')
# time.sleep(2)
# driver.find_element('name','password').send_keys('testing')
# time.sleep(2)
# driver.find_element('name','password').send_keys('')
# time.sleep(2)

####################################################################################

##   url: https://www.facebook.com/r.php?entry_point=login

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(opts)
driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
driver.maximize_window()
driver.find_element('name','firstname').send_keys('Reena')
time.sleep(1)
driver.find_element('name','lastname').send_keys('Josh')
time.sleep(1)
driver.find_element('name','reg_email__').send_keys('reena.josh@gmail.com')
time.sleep(1)
driver.find_element('name','reg_passwd__').send_keys('testingpassword')