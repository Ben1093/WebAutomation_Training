import logging

from selenium import webdriver

import pytest

# class browser_launch():

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome() #(API request will be created) will Create session with POST request #Fresh browser will open, Session ID is created
#     yield driver # instead of storing we can return them
#     return driver # value will be stored permanently, extra variable

def test_open_the_browser_and_launch_application(driver):
    chrome_options = webdriver.ChromeOptions()
    extension_path = "\Users\Samundeeswari\Downloads"
    chrome_options.add_extension(extension_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://restful-booker.herokuapp.com/")
    driver.maximize_window()
    LOGGER = logging.getLogger(driver.title)