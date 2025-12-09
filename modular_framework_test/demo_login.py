import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)