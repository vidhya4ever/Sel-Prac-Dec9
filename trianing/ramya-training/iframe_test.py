from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
ac_obj = ActionChains(driver)

driver.get('https://www.linkedin.com')
driver.maximize_window()

time.sleep(3)
googleframe = driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]')

driver.switch_to.frame(googleframe)
driver.find_element('xpath','//span[text()="Continue with Google"]').click()
driver.switch_to.parent_frame()
time.sleep(3)

ac_obj.scroll_to_element()