
# Using find_element to print table rows

#url: https://testautomationpractice.blogspot.com/
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# time.sleep(2)
#
# for row in range(2,8):
#     for i in  range (1,5):
#         print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{row}]/td[{i}]').text,end=" ")
#     print(sep='\n')

#***** python reference created
# for row in range(2,8):
#     for i in  range (1,5):
#         print(row, i,end=" ")
#     print(sep='\n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Using Find_elements method to print table rows
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
table_rows = driver.find_elements('xpath','//table[@name="BookTable"]//tr')
count=1 # This is to ignore header in the table
for row in table_rows:
    if count>1:
        print(row.text)
    count=count+1