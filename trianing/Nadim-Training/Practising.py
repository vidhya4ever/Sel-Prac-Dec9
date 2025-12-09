#url: Facebook
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome()
# driver.get("https://www.facebook.com/")
# sleep(2)
# driver.find_element('id','email').send_keys('vidhya4ever123@gmail.com')
# sleep(2)
# driver.find_element('id','pass').send_keys('password')
# sleep(2)
# driver.find_element('name','login').click()
# sleep(10)
##############################################################################################

#url: flipkart

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


driver = Chrome()
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
sleep(2)
driver.find_element('id','gender-female').click()
sleep(1)
driver.find_element('id','FirstName').send_keys('vidhyalakshmi')
driver.find_element('id','LastName').send_keys('v')
driver.find_element('name','Email').send_keys('vv@gmail.com')
sleep(1)
driver.find_element('id','Password').send_keys('password')
driver.find_element('name','ConfirmPassword').send_keys('password')
driver.find_element('id','register-button').click()
