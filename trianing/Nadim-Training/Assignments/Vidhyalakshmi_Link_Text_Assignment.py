# #url :  https://www.apple.com/in/
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.apple.com/in/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('link text','Mac').click()
# time.sleep(3)
# driver.close()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#url :  https://www.udemy.com/?srsltid=AfmBOoqcLT1aAfkPqp_U8TpaMwmYRH28y_OdbkR9egTUuWk2m-rUSHi7

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.udemy.com/?srsltid=AfmBOoqcLT1aAfkPqp_U8TpaMwmYRH28y_OdbkR9egTUuWk2m-rUSHi7")
driver.maximize_window()
time.sleep(2)
driver.find_element('link text','Sign up').click()
time.sleep(2)
driver.find_element('name','full-name').send_keys('vidhyalakshmi')
driver.find_element('name','email').send_keys('vidhya123@gmail.com')
time.sleep(1)
driver.find_element('class name','ud-icon.ud-icon-xsmall.ud-fake-toggle-input.ud-fake-toggle-checkbox').click()
time.sleep(1)
driver.find_element('class name','ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ').click()