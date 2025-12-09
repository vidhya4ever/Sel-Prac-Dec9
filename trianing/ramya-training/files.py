#                  FILE UPLOADING

# EXAMPLE 1
#url :https://testautomationpractice.blogspot.com/

# single file upload

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# time.sleep(2)
# singlefilepathname = r'C:\Users\User\OneDrive\Desktop\Desktop\GK.txt'
# multifilepathname = r'C:\Users\User\OneDrive\Desktop\Desktop\mail.txt'
# driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(singlefilepathname)
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(multifilepathname)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# EXAMPLE 2
#url: https://testautomationpractice.blogspot.com/
# multiple file selection

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# time.sleep(2)
# file1 = r'C:\Users\User\OneDrive\Desktop\Desktop\GK.txt'
# file2 = r'C:\Users\User\OneDrive\Desktop\Desktop\mail.txt'
# file3 = r'C:\Users\User\OneDrive\Desktop\Desktop\QSPIDERS.txt'
#
# # first method
# # files = (file1, file2, file3)
# # driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{"\n".join(files)}')
#
# # second method
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')

#***************************************************************************************************************

#           FILE DOWNLOADING CONCEPT

#url: https://testautomationpractice.blogspot.com/

# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# opts.add_argument('--incognito')
# driver = webdriver.Chrome(options=opts)
# driver = webdriver.Chrome(opts)
# driver.get('https://demoqa.com/upload-download')
# driver.maximize_window()
# time.sleep(4)
# driver.find_element('xpath','//a[text()="Download"]').click()
# time.sleep(2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

