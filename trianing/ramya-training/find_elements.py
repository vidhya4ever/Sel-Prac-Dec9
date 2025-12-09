#url: https://www.python.org/

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.get('https://www.python.org/')
driver.maximize_window()
time.sleep(2)
all_links = driver.find_elements('tag name','a')
for link in all_links:
    if link.get_attribute('href') is not None:
        print(link.get_attribute('href'))
