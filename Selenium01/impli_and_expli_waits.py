from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import  os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_vwo_login_with_waits():
    LOGGER = logging.getLogger(__name__)
    load_dotenv()

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_id = driver.find_element(By.XPATH, "//input[@id = 'login-username']")
    email_id.send_keys(os.getenv("EMAIL"))

    password = driver.find_element(By.XPATH, "//input[@type = 'password']")
    password.send_keys(os.getenv("PASSWORD"))

    sign_in_button = driver.find_element(By.XPATH, "//button[@id = 'js-login-btn']").click()
    element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard"))

    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")

    assert driver.current_url == "https://app.vwo.com/#/dashboard", "page title error"
    assert heading_element.text == "Aman"






