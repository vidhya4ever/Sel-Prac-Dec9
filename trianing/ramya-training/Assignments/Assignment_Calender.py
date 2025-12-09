# url: https://www.irctc.co.in/nget/train-search
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# driver.maximize_window()
# time.sleep(1)
# driver.find_element('xpath','//button[text()="OK"]').click()
# time.sleep(1)
# driver.find_element('xpath','//p-calendar[@id="jDate"]').click()
# time.sleep(1)
#
# def select_date(jmonth,jdate):
#     while True:
#         month = driver.find_element('xpath', '//div[@class="ui-datepicker-title ng-tns-c69-9"]')
#         #print(month.text)
#         if month.text == f'{jmonth}':
#             driver.find_element('xpath',f'//a[text()="{jdate}"]').click()
#             print(f'The given journey date "{jdate} {jmonth}" is selected')
#             break
#         else:
#             driver.find_element('xpath','//span[@class="ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9"]').click()
#
# select_date('January2026','10')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
# # url: https://www.booking.com/
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)

driver.get('https://www.booking.com/')
driver.maximize_window()
time.sleep(2)
# driver.find_element('xpath','//button[@aria-label="Dismiss sign-in info."]').click()
# time.sleep(1)
driver.find_element('xpath','//button[@data-testid="searchbox-dates-container"]').click()
time.sleep(1)
# # month = driver.find_element('xpath','(//h3[@class="e7addce19e af236b7586"])[1]')
# # print(month.text)
# date = driver.find_element('xpath','(//span[text()="15"])[1]')
# print(date.text)
driver.find_element('xpath','(//span[text()="15"])[1]').click()





# month = //h3[text()="November 2025"]
# date = (//span[text()="15"])[1]
# def select_date(checkin_month,checkin_date):
#     while True:
#         current_month = driver.find_element('xpath','//h3[@aria-live="polite"][1]')
#         print(current_month.text)
#         if current_month.text == checkin_month:
#             time.sleep(3)
#             driver.find_element('xpath',f'(//span[text()="{checkin_date}"])[1]').click()
#             print(f'The given checkin date "{current_month.text}{checkin_date}" selected')
#             break
#         else:
#             driver.find_element('xpath','//button[@aria-label="Next month"]').click()
#
# select_date('November 2025','20')

##########################33
# //span[text()="Ranchi"]

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//input[@id="toCity"]').send_keys('Ranchi')
# time.sleep(2)
# ele = driver.find_element('xpath','//p[@class="font12 greyText appendBottom3"][1]')
# print(ele.text)