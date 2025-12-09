# QUESTION 1.  wap to fetch all the popular searches from https://www.myntra.com/
# url: https://www.myntra.com/
#
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
time.sleep(2)
popularsearches = driver.find_elements('xpath','//div[@class="desktop-pSearchlinks"]//a')
for ele in popularsearches:
    print (ele.text)
#
# ============================================================================================================
#
# QUESTION 2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
# url: https://www.myntra.com/
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
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(1)
# driver.find_element('xpath','//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(1)
# driver.find_element('xpath','//div[@class="colour-more"]/span').click()
# time.sleep(1)
# colours = driver.find_elements('xpath','(//div[@class="vertical-filters-filters"])[2]//label')
# for ele in colours:
#     print (ele.text.split('(')[0])
#
# ============================================================================================================
# QUESTION 3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
#              wap to print the name and price of each food item in available
#
# url: https://www.zomato.com/Bengaluru/
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.zomato.com/Bengaluru/')
# driver.maximize_window()
# time.sleep(2)
# #click on search box
# driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
# driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('PIZZA')
# time.sleep(1)
# #click on "pizza-delivery"
# driver.find_element('xpath','(//p[text()="Pizza - Delivery"])[1]').click()
# time.sleep(1)
# # click on first pizza delivered restaurant from the list shown
# driver.find_element('xpath','(//div[@class="sc-fYAFcb jTHwOF"]//a[2])[1]').click()
# time.sleep(3)
# itemname = driver.find_elements('xpath','//div[@class="sc-dgEPJF nioNy"]//h4')
# itemprice = driver.find_elements('xpath','//div[@class="sc-dgEPJF nioNy"]//span[@class="sc-17hyc2s-1 cCiQWA"]')
#
# for i,j in zip(itemname,itemprice):
#     print(i.text," = ",j.text)
#
# ============================================================================================================
# QUESTION 4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
#
# url: https://in.bookmyshow.com/
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://in.bookmyshow.com/')
# driver.maximize_window()
# time.sleep(2)
# #input the location details in inputbox
# driver.find_element('xpath','//input[@id="dummy"]').send_keys('coimbatore')
# #select location by clicking
# driver.find_element('xpath','(//div[@class="sc-fv93km-0 cPDWyb"]//span)[1]').click()
# #click on movies tab
# driver.find_element('xpath','//a[text()="Movies"]').click()
# time.sleep(4)
# movieslist = driver.find_elements('xpath','//div[@class="sc-7o7nez-0 elfplV"]')
# for movie in movieslist:
#     print(movie.text)
#
# ===============================================================================================
#
