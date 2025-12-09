#===================================================================================================
#
# # Sample for relative xpath
# from selenium import webdriver
# import time
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/OneDrive/Desktop/xpath.html')
# time.sleep(2)
# driver.find_element('xpath','//div[2]/input[2]').send_keys('username4')
# time.sleep(1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22

# xpath by attribute
# from selenium import webdriver
# import time
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get("file:///C:/Users/User/OneDrive/Desktop/xpath.html")
# driver.maximize_window()
#
# #driver.find_element('xpath','//a[@href="https://www.amazon.in"]').click()
# # OR
# driver.find_element('link text','Amazon').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# from selenium import webdriver
# import time
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# time.sleep(5)
# driver.find_element('xpath','//input[@id="twotabsearchtextbox"]').send_keys('water bottle')
# driver.find_element('xpath','//input[@id="nav-search-submit-button"]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
# url: https://demowebshop.tricentis.com/

from selenium import webdriver
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element('xpath','//a[@class="ico-register"]').click()
time.sleep(2)
driver.find_element('xpath','//input[@id="gender-female"]').click()
driver.find_element('xpath','//input[@id="FirstName"]').send_keys('vidhya')
driver.find_element('xpath','//input[@id="LastName"]').send_keys('venkat')
driver.find_element('xpath','//input[@id="LastName"]').send_keys('venkat')
driver.find_element('xpath','//input[@id="Email"]').send_keys('vidhya46ever@gmail.com')
driver.find_element('xpath','//input[@id="Password"]').send_keys('password@123')
driver.find_element('xpath','//input[@id="ConfirmPassword"]').send_keys('password@123')
driver.find_element('xpath','//input[@id="register-button"]').click()
time.sleep(2)
driver.find_element('xpath','//a[@href="/logout"]').click()
time.sleep(2)
driver.find_element('xpath','//a[@href="/login"]').click()
time.sleep(2)
driver.find_element('xpath','//input[@id="Email"]').send_keys('vidhya46ever@gmail.com')
driver.find_element('xpath','//input[@id="Password"]').send_keys('password@123')
driver.find_element('xpath','//input[@value="Log in"]').click()
time.sleep(5)
