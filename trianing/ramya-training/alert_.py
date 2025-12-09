#url: https://testautomationpractice.blogspot.com/
# Handling confirmation alert -> having both buttons ok and cancel
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/ ')
# driver.maximize_window()

# driver.find_element('xpath','//button[@id="confirmBtn"]').click()
# time.sleep(1)
# alert_object = driver.switch_to.alert
# alert_object.accept()
# time.sleep(1)
#
# driver.find_element('xpath','//button[@id="confirmBtn"]').click()
# alert_object.dismiss()
#
# confirmation_msg = driver.find_element('xpath','//p[@id="demo"]')
# print(confirmation_msg.text)

# driver.find_element('xpath','//button[@id="promptBtn"]').click()
# alert_object = driver.switch_to.alert
# alert_object.send_keys('vidhya')
# alert_object.accept()
#
# confirmation_msg = driver.find_element('xpath','//p[@id="demo"]')
# print(confirmation_msg.text)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Authorization pop up:

#url: https://the-internet.herokuapp.com/basic_auth

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
# driver.maximize_window()
# time.sleep(2)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# push pop up:

#url: https://www.irctc.co.in/nget/train-search

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

opts.add_argument('--disable-notifications') # to disable push notification

driver = webdriver.Chrome(opts)
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
time.sleep(2)