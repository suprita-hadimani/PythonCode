#login to web page install pip selenium and install chrome driver for selenium to open in chrome  and firefox driver to open in firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome()
driver.get("https://www.fieldglass.net/")#give the link of web page you want to login
elem=driver.find_element_by_id("usernameId_new")# getthe id name in page information.
elem.clear()
elem.send_keys("suprita")#give your username
elem=driver.find_element_by_id("passwordId_new")
elem.clear()
elem.send_keys("Sup@97")#give ur password here
elem.send_keys(Keys.RETURN)
