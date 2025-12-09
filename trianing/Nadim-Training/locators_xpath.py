# xpath :
#     xpath is used to find the location of a webelement in a html tree structure or in DOM(Document object Model)

# xpath classified into two types:
# 1.Absolute xpath
# 2.Relative xpath

# 1.Absolute xpath
#     -->It will traverse from parent to its own child
#     -->It is Denoted as (/)
# Drawbacks of Absolute xpath
#     -->Absolute xpath is very lengthy comparing to relative xpath
#     --> Always it will traverse from parent to its own child
# 2.Relative xpath
#     -->It will traverse from parent to any of the child
#     -->It is Denoted as (//)

# Sample for Absolute xpath
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")

"""
# """
# driver = http://webdriver.Chrome(opts)
# driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
# time.sleep(3)
# driver.find_element("xpath","html/body/div[2]/input[2]").send_keys("Username4")
# """
# """
# driver = http://webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(3)
# driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()








