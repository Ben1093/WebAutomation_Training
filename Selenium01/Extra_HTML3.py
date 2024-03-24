# HTML elements
# HTML is the standard markup language for the web pages
  # It is a tag based elements
  # Head
  # Body
  # Footer

# HTML Tag/Element = attribute = value

# Automation steps
# 1. Open the browser
# 2. Navigate to the URL
# 3. Find the email webelement and put email id
# 4. Find the password webelement and put password = 123
# 5. click on the button - sign in - Till this selenium will do the work
# 6. Verify that the dashboard is loaded - pytest framework(will do this)
# 7. Create a report to send to QA lead - HTML - Allure report

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time
import os
from dotenv import load_dotenv

def test_vwologin():
    load_dotenv()
    LOGGER = logging.getLogger(__name__)
    # Create a session
    driver= webdriver.Chrome()
    driver.maximize_window()

    # Open the browser
    # Navigate to URL
    # Command - driver.get(Navigate command to Existing session)
    driver.get("https://app.vwo.com/#/login")

    # Find the Email WebElement and put email id
    # Find the Password WebElement and put password
    # Click on the button - sign in

    # Selenium - How to find the elements
    # find_element by_id: Finds an element by its unique id attribute.
    # find_element by_name: Finds an element by its name attribute.
    # find_element by_link_text: Finds an anchor element (a) by its visible text.
    # find_element by_partial_link_text: Finds an anchor element (a) by a partial match of its visible text.
    # find_element by_tag_name: Finds an element by its HTML tag name (e.g., "div", "input", "a", etc.).
    # find_element by_class_name: Finds an element by its CSS class name.

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button = driver.find_element(By.ID, "js-login-btn")

    # Sending the data email and password and clicking on the button
    # sendKeys and click()

    email_address_ele.send_keys(os.getenv("EMAIL"))
    password_ele.send_keys(os.getenv("PASSWORD"))

    sign_in_button.click()

    time.sleep(5)

    logging.info("title is ->" + driver.title)

    assert 'Dashboard' in driver.title



