# This helps to learn mouse and keyboard operation like below
# scroll, left click, right click, double click,

# action_chains - module name or python file name
# ActionChains - class name
# url: https://www.kushals.com/
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.kushals.com/')
# driver.maximize_window()
# time.sleep(5)
#
# earrings = driver.find_element('xpath','((//div[@class="navigation__tier-1-container"])[2]//a[contains(text(),"Earrings")])[1]')
# ac_obj.move_to_element(earrings).perform()

#*****************************************************************************************************************


# url https://www.myntra.com/

# //div[@class="desktop-navLinks"]//div[@class="desktop-navContent"]

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(5)

# headerlist = driver.find_elements('xpath','//div[@class="desktop-navLinks"]//div[@class="desktop-navContent"]')
# # ac_obj.move_to_element(earrings).perform()
# # print(len(headerlist))
#
# for i in range(0,(len(headerlist))-1):
#     ac_obj.move_to_element(headerlist[i]).perform()
#     time.sleep(1)


# for i in headerlist:
#     ac_obj.move_to_element(i).perform()
#     time.sleep(1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2


# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in navigation_elements[:-1]:
#     ac_obj.move_to_element(ele).perform()
#     time.sleep(2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2


#
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# time.sleep(2)
#
# # copy_ele = driver.find_element('xpath', '//button[text()="Copy Text"]')
# # ac_obj.double_click(copy_ele).perform()
# # time.sleep(2)
# #
# name = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(name).perform()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# time.sleep(2)
#
# # ele = driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
# # ac_obj.context_click(ele).perform()
#
# ac_obj.context_click().perform()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# ac_obj.scroll_to_element(ref_ele).perform()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

## Scrolling till the end of the application
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(3)
#
# ## To go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
'''         Using execute_script        '''

# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# ## To go back to the start of the application
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.maximize_window()
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
'''     Scroll Down and scroll up by Pixels      

        SYNTAX  :   driver.execute_script("window.scrollBy(horizontal, vertical);")  
'''
# #
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.execute_script("window.scrollBy(0, 500);")       ## will scroll down by 500 pixels
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, -500);")      ## will scroll up by 500 pixels

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
# ###################################################################################################
# ###################################################################################################

'''
ANALYZE THE BELOW CODE
'''

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
#
# ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
# time.sleep(1)
# ac_obj.send_keys('Potter').perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2




# Assignment
driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
driver.maximize_window()
time.sleep(2)

draggable = driver.find_element('xpath','//div[@id="draggable"]')
droppable = driver.find_element('xpath','//div[@id="droppable"]')

ac_obj.drag_and_drop(draggable,droppable).perform()
time.sleep(2)