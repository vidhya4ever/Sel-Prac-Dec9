# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.instagram.com/accounts/login/?hl=en")

#############################################################################################3
# url:  https://www.saucedemo.com/")

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element('id','user-name').send_keys('standard_user')
# driver.find_element('id','password').send_keys('secret_sauce')
# time.sleep(2)
# driver.find_element('id','login-button').click()
# time.sleep(5)
# driver.find_element('id','react-burger-menu-btn').click()
# time.sleep(2)
# driver.find_element('id','logout_sidebar_link').click()

#########################################################################################
# url:    https://testautomationpractice.blogspot.com/

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.maximize_window()
# driver.find_element('id','name').send_keys('VIDHYALAKSHMI')
# time.sleep(1)
# driver.find_element('id','email').send_keys('vidhya@gmail.com')
# time.sleep(1)
# driver.find_element('id','phone').send_keys('123456789')
# time.sleep(1)
# driver.find_element('id','textarea').send_keys('Coimbatore')
# time.sleep(1)
# driver.find_element('id','female').click()
# time.sleep(1)
# driver.find_element('id','wednesday').click()

###################################################################################

from selenium import webdriver
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/')
time.sleep(2)
driver.maximize_window()
driver.find_element('id','email').send_keys('vidhya4ever34@gmail.com')
time.sleep(2)
driver.find_element('id','pass').send_keys('testpass')
time.sleep(2)
driver.find_element('name','login').click()
time.sleep(2)