# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# #  file:///C:/Users/User/Downloads/demo%20(2).html
# #  https://www.facebook.com/r.php?entry_point=login
# #  //button[text()="OK"]
# #  https://www.irctc.co.in/nget/train-search
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
#
# driver.maximize_window()
# time.sleep(2)
#
# car_listbox= driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj = Select(car_listbox)
#               select_by_index
from calendar import month

# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_index(4)

#               select_by_value

# select_obj.select_by_value('for')
# time.sleep(2)
# select_obj.select_by_value('merc')

#           select_by_visible_text

# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# #  file:///C:/Users/User/Downloads/demo%20(2).html
# #  https://www.facebook.com/r.php?entry_point=login
# #  //button[text()="OK"]
# #  https://www.irctc.co.in/nget/train-search
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
# driver.maximize_window()
# time.sleep(2)
#
# multiple_listbox= driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj = Select(multiple_listbox)
#
# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#@@@@@@@@@@@@@@@ DESELECT CONCEPT  ##########################
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
# driver.maximize_window()
# time.sleep(2)
#
# multiple_listbox= driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj = Select(multiple_listbox)
#
# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')
# time.sleep(2)

# select_obj.deselect_by_index(1)
# time.sleep(2)
# select_obj.deselect_by_value('bmw')
# time.sleep(2)
# select_obj.deselect_by_visible_text('Ford')
# time.sleep(2)

# select_obj.deselect_all()
# time.sleep(2)

#@@@@@@@@@@@@@@@ SELECT ALL ITEM  ##########################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
# driver.maximize_window()
# time.sleep(2)
#
# multiple_listbox= driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj = Select(multiple_listbox)
#
# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')
# time.sleep(2)
#
# selected_itemslist = select_obj.all_selected_options
#
# for item in selected_itemslist:
#     print(item.text)

#@@@@@@@@@@@@@@@ FIRST SELECTED  ##########################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
# driver.maximize_window()
# time.sleep(2)
#
# multiple_listbox= driver.find_element('xpath','//select[@id="multiple_cars"]')
# select_obj = Select(multiple_listbox)
#
# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')
# time.sleep(2)
#
# first_selected_option = select_obj.first_selected_option
# print(first_selected_option.text)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# driver.maximize_window()
# time.sleep(2)
#
# day_listbox = driver.find_element('xpath','//select[@id="day"]')
# select_obj = Select(day_listbox)
# select_obj.select_by_visible_text('21')
#
# month_listbox = driver.find_element('xpath','//select[@id="month"]')
# select_obj = Select(month_listbox)
# select_obj.select_by_visible_text('Jul')
#
# year_listbox = driver.find_element('xpath','//select[@id="year"]')
# select_obj = Select(year_listbox)
# select_obj.select_by_visible_text('2020')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
#
# driver.maximize_window()
# time.sleep(2)
#
# car_listbox= driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj = Select(car_listbox)
# allcarelements_lists = select_obj.options
# for item in allcarelements_lists:
#     print(item.text)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# driver.get('file:///C:/Users/User/Downloads/demo%20(2).html')
#
# driver.maximize_window()
# time.sleep(2)
#
# car_listbox= driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj = Select(car_listbox)
#
# all_elements = select_obj.options
# #### select_by_index
# for i in range(0,len(all_elements)):
#         select_obj.select_by_index(i)

#### select_by_val
# for item in all_elements:
#         ele = item.get_attribute('value')
#         select_obj.select_by_value(ele)

#######  select_by_visibletext

# for item in all_elements:
#     ele_text = item.text
#     select_obj.select_by_visible_text(ele_text)
