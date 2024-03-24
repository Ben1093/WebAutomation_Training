import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_cura_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appoinment = driver.find_element(By.ID,"btn-make-appointment")
    make_appoinment.click()

    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")

    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    print(driver.current_url)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"

    time.sleep(5)
    driver.quit()
