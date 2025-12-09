# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url: https://www.flipkart.com/

# driver.get('https://www.flipkart.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="TVs & Appliances"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Become a Seller"]').click()
# time.sleep(2)
# driver.find_element('xpath','//button[text()="Start Selling"]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@name="mobileNumber"]').send_keys('9987656789')
# time.sleep(2)
# driver.find_element('xpath','//input[@name="email"]').send_keys('vidhya344@gmail.com')
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Register & Continue"]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
# url: https://www.amazon.in/

# text() function using xpath

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','//a[text()="Bestsellers"]').click()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Most Gifted"]').click()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Amazon Launchpad"]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

#url :https://www.nseindia.com/

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.nseindia.com/")
# driver.maximize_window()
# time.sleep(3)
# # driver.find_element('xpath','//button[text()="2"]').click() #checkbox
# # time.sleep(1)
# # driver.find_element('xpath','''(//button[text()='X'])[2]''').click()  # "X" close button

# driver.find_element('xpath','//li[@class="desktoplogo pt-md-2"]').click()
# #driver.find_element('xpath','//a[text()="NIFTY 11NOV25 25400 PE"]').click()
# #driver.find_element('xpath','//a[text()="Invest"]').click()
# #driver.find_element('xpath','//div[text()="ASIANPAINT"]').click()
# #driver.find_element('xpath','//img[@aria-label="WhatsApp"]').click()
# #driver.find_element('xpath','//button[@class="accessibility-button"]').click()
# #time.sleep(3)
# #driver.find_element('xpath','//button[text()="High Contrast"]').click()
# #time.sleep(2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

#url :https://www.facebook.com/r.php?entry_point=login

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','(//input[@type="text"])[1]').send_keys('vidhya')
# time.sleep(1)
# driver.find_element('xpath','(//input[@type="text"])[2]').send_keys('v')
# time.sleep(1)
# driver.find_element('xpath','(//input[@type="text"])[5]').send_keys('vidhya3435@gmail.com')
# time.sleep(1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url :https://blinkit.com/

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://blinkit.com/")
# driver.maximize_window()
# time.sleep(3)
# #driver.find_element('xpath','//button[text()="Detect my location"]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@name="select-locality"]').send_keys('560049')
# time.sleep(1)
# driver.find_element('xpath','//div[text()="Bengaluru"]').click()
# time.sleep(1)
# driver.find_element('xpath','//div[text()="Login"]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@class="login-phone__input input"]').send_keys('9876543567')
# time.sleep(1)
# driver.find_element('xpath','//button[text()="Continue"]').click()




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url :https://www.giva.co/

# contains(text(),'text')

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.giva.co/")
# driver.maximize_window()
# time.sleep(3)
# #driver.find_element('xpath','//span[contains(text(),"Gold with Lab Diamonds")]').click()
# time.sleep(1)
# driver.find_element('xpath','//span[contains(text(),"GIVA Gift Card")]').click()

##################################################

#url :https://www.python.org/downloads/

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','//a[text()="Python 3.14.0"]/../..//a[text()="Release Notes"]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url :https://www.tradingview.com/

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://www.tradingview.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Search"]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@inputmode="search"]').send_keys('HAL')
# time.sleep(1)
# driver.find_element('xpath','(//button[@aria-label="Search"])[3]').click()
# time.sleep(4)
# # xpath = //span[text()="HAL"]/../../..//span[@class="priceWrapper-qWcO4bp9"]
# HAL_Price = driver.find_element('xpath','//span[text()="HAL"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print("HAL Price",HAL_Price.text)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get('file:///D:/Learnings/PYTHONCLASSES/SELENIUM/Ramya-Notes/demo.html')
# driver.maximize_window()
# time.sleep(2)
# # click checkbox next to python
# # driver.find_element('xpath','//td[text()="Python"]/..//input[@name="download"]').click()
# # time.sleep(2)
# # # click Download link of Linux OS
# # driver.find_element('xpath','//td[text()="Linux"]/..//a[text()="Download"]').click()
# # time.sleep(2)
# # get the version details of 'Linux' OS
# # Linux_Version = driver.find_element('xpath','//td[text()="Linux"]/..//td[2]')
# # print("Linux Version Details are:   ",Linux_Version.text)
# # click on facebook limk
# driver.find_element('xpath','//a[contains(text()," Facebook ")]').click()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url : https://www.iforex.in/tools/live-rates

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','(//div[@id="ai-chat-bubble-close"])[2]').click()
# time.sleep(5)
# # Scroll down manually
# sel_price = driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]')
# print("sell Price:   ", sel_price.text)
# buy_price = driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[3es ]')
# print("Buy Price:   ", buy_price.text)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#url : https://www.iforex.in/tools/live-rates

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)

driver.get('https://www.makemytrip.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath','//span[@class="commonModal__close"]').click()
time.sleep(1)
driver.find_element('xpath','//span[text()="Departure"]').click()
time.sleep(2)

def select_date(month,date):
    while True:
        try:
            driver.find_element('xpath',f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
            time.sleep(1)
            break
        except:
            driver.find_element('xpath','//span[@aria-label="Next Month"]').click()

select_date('August 2026','15')
print("Specified Month gets selected")