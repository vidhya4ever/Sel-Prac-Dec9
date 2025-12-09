# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(2)
#
# print(driver.window_handles)
# print(driver.window_handles[-1])
#
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element('xpath','//input[@class="header__search"]').send_keys('pixel9')
# time.sleep(2)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Twitter"]').click()
# time.sleep(2)
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(4)
# driver.find_element('xpath','//span[text()="Follow"]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22

# from selenium import webdriver
# import time
#
# from selenium.webdriver import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(3)
#
#
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('pixel9')
#         time.sleep(2)
#         driver.switch_to.window(driver.window_handles[0])
#         time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
#
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if 'nopCommerce' in driver.current_url:
#         driver.find_element('xpath','//span[text()="Follow"]').click()
#         time.sleep(2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22

# from selenium import webdriver
# import time
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(20)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
#
# def handle_window():
#     return driver.window_handles
#
# def multiple_window_handling(urlele,wbele):
#     for handle in handle_window():
#         driver.switch_to.window(handle)
#         if urlele in driver.current_url:
#             if urlele == 'googleblog':
#                 driver.find_element('xpath', wbele).send_keys('pixel9')
#                 time.sleep(2)
#             elif urlele == 'nopCommerce':
#                 driver.find_element('xpath',wbele).click()
#             driver.switch_to.window(handle_window()[0])
#
# multiple_window_handling(urlele='googleblog',wbele='//input[@class="header__search"]')
#
# multiple_window_handling(urlele='nopCommerce',wbele='//span[text()="Follow"]')

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



