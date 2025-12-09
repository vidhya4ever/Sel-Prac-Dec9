import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)
class register:
    def gender(self):
        driver.find_element('id', 'gender-female').click()
    def firstname(self):
        driver.find_element('id', 'FirstName').send_keys(data['firstname'])
    def lastname(self):
        driver.find_element('id', 'lastname').click()
    def email(self):
        driver.find_element('id', 'email').click()
driver.find_element('id', 'LastName').send_keys(data['lastname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['pwd'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])