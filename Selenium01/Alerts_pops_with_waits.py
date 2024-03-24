from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_jv_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #click for JS alert and click ok pop for that
    click_js_alert = driver.find_element(By.XPATH,"//button[contains(text(), 'Click for JS Alert')]")
    click_js_alert.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert1 = driver.switch_to.alert

    if "I am a JS Alert" in alert1.text:
        alert1.accept()
        result = driver.find_element(By.XPATH, "//p[@id = 'result']")
        print(result.text)
    else:
        print("Alert text not found")

def test_click_for_js_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #Click for JS confirmation popup ok or cancel
    click_js_confirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    click_js_confirm.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert2 = driver.switch_to.alert

    alert2.dismiss()
    result = driver.find_element(By.XPATH, "//p[@id = 'result']")
    print(result.text)


def test_click_for_js_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #Click for JS prompt popup ok or cancel
    click_js_confirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    click_js_confirm.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert3 = driver.switch_to.alert

    alert3.send_keys("My name is Parthiben")
    alert3.accept()

    result = driver.find_element(By.XPATH, "//p[@id = 'result']")
    print(result.text)




