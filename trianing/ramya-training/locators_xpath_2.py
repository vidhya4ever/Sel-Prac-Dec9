# # url: https://blinkit.com/
#
# # get_attribute()
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.instagram.com/')
# driver.maximize_window()
# time.sleep(2)
# ele = driver.find_element('xpath','//button[@type="submit"]')
# print(ele.is_enabled())
# assert ele.is_enabled(),'button is not enabled'
#========================================================================================
# # url: https://www.myntra.com/
#
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
# ele = driver.find_element('xpath','(//a[text()="Women"])[1]')
# #print(ele.value_of_css_property('font-size'))
#========================================================================================

####### Find elements
# url: https://demowebshop.tricentis.com/
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
# ele = driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# for item in ele:
#     print (item.text)

#========================================================================================
#url: https://demowebshop.tricentis.com/

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
# categories = driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# for ele in categories:
#     print (ele.text)

#========================================================================================

#url:https://www.myntra.com/

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath','//li[text()="Adidas Originals Shoes"]').click()
#
# shoename = driver.find_elements('xpath','//h4[@class="product-product"]')
# shoeprice = driver.find_elements('xpath','//div[@class="product-price"]')
#
# for i , j in zip(shoename, shoeprice):
#     print(i.text,"=",j.text)

#========================================================================================
