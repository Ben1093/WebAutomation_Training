#Create Session
#Send the commands - navigate to a url
#If you are using selenium < 4, we use to set the driver path
#if you are using selenium > 4, driver path is not needed they will update automatically
# from lib2to3.pgen2 import driver

from selenium import webdriver

import pytest

# class browser_launch():

@pytest.fixture()
def driver():
    driver = webdriver.Chrome() #(API request will be created) will Create session with POST request #Fresh browser will open, Session ID is created
    yield driver # instead of storing we can return them
    return driver # value will be stored permanently, extra variable

def test_open_the_browser_and_launch_application(driver):
    driver.get("https://restful-booker.herokuapp.com/")
    driver.maximize_window()
    assert "Welcome to Restful-Booker" == driver.title
    print(driver.title)
