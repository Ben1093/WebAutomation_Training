import selenium
import pytest
from selenium import webdriver

def test_login():
    chrome_options = webdriver.ChromeOptions()
    extension_path = "/Users/Samundeeswari/Downloads/Ad_Blocker.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)
    # Will run the test without UI - headless
    chrome_options.add_argument('--headless=new')

    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")

# With UI - We can see the test, which is slow and consume lot of resources
# Without UI - Headless - fast, it will consume less resources, you can't see the test
