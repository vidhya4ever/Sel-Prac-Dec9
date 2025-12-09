"""
driver = http://webdriver.Chrome(opts)
driver.get("https://www.apple.com/in/")
time.sleep(3)
driver.find_element("link text","Mac").click()
"""
"""
driver = http://webdriver.Chrome(opts)
driver.get("https://www.udemy.com/?srsltid=AfmBOoo4hmoNb6Wh5YORtxfUokZWS5Ey9-BzMF4T4xB4IKtxnPsFrA_F")
time.sleep(3)
driver.find_element("link text","Sign up").click()
time.sleep(3)
driver.find_element("name","full-name").send_keys("Pookie")
time.sleep(3)
driver.find_element("name","email").send_keys("mailto:Pookie@gmail.com")
time.sleep(3)
driver.find_element("class name","ud-icon.ud-icon-xsmall.ud-fake-toggle-input.ud-fake-toggle-checkbox").click()
time.sleep(3)
driver.find_element("class name","ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ").click()
"""
# Partial Link text:
#     It is used to find the location of an element by passing some portion of a text value
#     It will work only for anchor tag (it will work for span tag also but not all the time)
#     In this also the text value is case sensitive

# Note:
#     In link text you have to pass the text value completely but in partial link text you have to pass the text value some portion
#     Both link text and partial link text are case sensitive
# Amazon in Ecommerce website
"""
2025 --> Python 3.14.0
2026 --> Python 4.11.0
"""

# 2026:
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(3)
driver.find_element("link text","Python 3.14.0").click()
"""
# NoSuchElementException

# Python 3.14.0
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(3)
driver.find_element("partial link text","Python").click()
"""

Oct
29 - 11: 01
am

#+=========================================================================================

< html >
< head >
< title > Sample
Webpage < / title >
< / head >
< body >
< h1 > Login
Page < / h1 >
Username: < input
type = "text"
id = "a1" > < br > < br >
Password: < input
type = "password"
id = "a1" > < br > < br >
< a
href = "https://www.amazon.in"
id = "a3" > Forgot
Password ? < / a > < br > < br >
< input
type = "checkbox"
id = "a4" > I
Agree
the
Terms & Conditions < br > < br >
< input
type = "submit"
value = "Login"
id = "a5" >
< input
type = "reset"
value = "Cancel"
id = "a6" > < br > < br >
< a
href = "https://www.python.org/" > Python
3.17
.0 < / a >

< / body >

< / html >