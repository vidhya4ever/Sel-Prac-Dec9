from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/shop/')
driver.maximize_window()
time.sleep(2)
ac_obj = ActionChains(driver)
women = driver.find_element('xpath','(//a[text()="Women"])[1]')
ac_obj.move_to_element(women).perform()

woment_list = driver.find_elements('xpath','//li[@class="desktop-oddColumnContent"]')
wlist =[]
for ele in woment_list:
    if ele.text !='':
        wlist.append(ele.text)
    #print(ele.text)
print(wlist)
driver.quit()