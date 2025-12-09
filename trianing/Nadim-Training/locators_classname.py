from selenium.webdriver import Chrome
from time import sleep

# driver = Chrome()
# driver.get("file:///C:/Users/User/OneDrive/Desktop/sample.html")
# sleep(3)
# Method 1
# driver.find_element('class name','c1').send_keys('vidhya')
# driver.find_element('class name','c2').send_keys('test-pwd')
#Method 2
# driver.find_element('class name','user.name').send_keys('vidhya')
# sleep(5)
###########################################################################################
#  url: https://demowebshop.tricentis.com/register
# class="text-box single-line"

# NOT USING DOT (.) IN CLASS VALUE
#---------------------------------

# driver = Chrome()
# driver.get('https://demowebshop.tricentis.com/register')
# driver.maximize_window()
# sleep(2)
# driver.find_element('class name','text-box single-line').send_keys('vidhya')
# sleep(2)

# WE ARE USING DOT (.) IN CLASS VALUE TO AVOID NOSUCHELEMENT EXCEPTION
#----------------------------------------------------------------------

driver = Chrome()
driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
sleep(4)
driver.find_element('class name','text-box.single-line').send_keys('vidhya')
sleep(2)