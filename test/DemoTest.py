# from selenium import webdriver
# from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test import DriverFactory
from test.Browser import Browser

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = DriverFactory.init_browser(Browser.CHROME)
driver.get("https://www.facebook.com")
element = driver.find_element(By.ID, "email")
element.send_keys(user_name)
element = driver.find_element(By.ID, "pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
driver.close()
