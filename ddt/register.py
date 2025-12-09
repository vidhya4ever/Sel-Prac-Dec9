# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys('vidhya')
# driver.find_element('id', 'LastName').send_keys('v')
# driver.find_element('id', 'Email').send_keys('vv@gmail.com')
# driver.find_element('id', 'Password').send_keys('pwdnewone')
# driver.find_element('id', 'ConfirmPassword').send_keys('pwdnewone')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from selenium import webdriver
# import time
# from ddt.reading_excel import read_testdata
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(3)
#
# path = r'C:\Users\User\PycharmProjects\Selenium_Training\trianing\Files\demo_data.xlsx'
# data = read_testdata(path,'registration',2)
# print(data)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys(data['firstname'])
# driver.find_element('id', 'LastName').send_keys(data['lastname'])
# driver.find_element('id', 'Email').send_keys(data['email_id'])
# driver.find_element('id', 'Password').send_keys(data['pwd'])
# driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from selenium import webdriver
import time
from ddt.reading_excel import read_testdata


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(3)

path = r'C:\Users\User\PycharmProjects\Selenium_Training\trianing\Files\demo_data.xlsx'
data = read_testdata(path,'registration',2)
print(data)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('id', 'gender-female').click()
driver.find_element('id', 'FirstName').send_keys(data['firstname'])
driver.find_element('id', 'LastName').send_keys(data['lastname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['pwd'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])