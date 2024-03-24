import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):  # value means formatting bold etc.,
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(os.getcwd() + "/Test_case_1.xlsx"))
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    vwo_login(username, password)

    # file_path = "Test_case_1.xlsx"
    # credentials = read_credentials_from_excel(file_path)
    #
    # for user_cred in credentials:
    #     username = user_cred["username"]
    #     password = user_cred["password"]
    #     print(username,password)
    #     vwo_login(username,password)


def vwo_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_id = driver.find_element(By.XPATH, "//input[@id = 'login-username']")
    email_id.send_keys(username)

    pswrd = driver.find_element(By.XPATH, "//input[@id= 'login-password']")
    pswrd.send_keys(password)

    sign_in_button = driver.find_element(By.XPATH, "//button[@id = 'js-login-btn']").click()

    Element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id = 'js-login-btn']")))

    result = driver.current_url
    if result != "https://app.vwo.com/#/dashboard":
        pytest.xfail("invalid login")
        driver.quit()



