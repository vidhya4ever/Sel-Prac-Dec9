# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome()
# driver.get('file:///C:/Users/User/OneDrive/Desktop/sample.html')
# sleep(2)
# driver.maximize_window()
# sleep(2)
# testelement = driver.find_element('tag name',"a").click()
# print(testelement)
# sleep(2)
################################################################################
#url    https://demowebshop.tricentis.com/register
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get('https://demowebshop.tricentis.com/register')
sleep(2)
driver.maximize_window()
sleep(2)
#driver.find_element('tag name',"input").send_keys('vidhya')
sleep(2)
# driver.find_elements()