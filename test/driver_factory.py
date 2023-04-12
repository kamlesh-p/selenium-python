from selenium import webdriver

from test.Browser import Browser


def init_browser(browser):
    if browser == Browser.CHROME:
        driver = webdriver.Chrome()
    elif browser == Browser.EDGE:
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    return driver
