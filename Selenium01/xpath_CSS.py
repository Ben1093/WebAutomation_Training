from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import  os
from dotenv import load_dotenv


def test_ebay():
    load_dotenv()
    LOGGER = logging.getLogger(__name__)

    driver = webdriver.Chrome()
    driver.maximize_window()

    #ebay URL
    driver.get("https://www.ebay.com/b/Computers-Tablets-Network-Hardware/58058/bn_1865247")

    #select the PC Laptops in the page
    driver.find_element(By.XPATH, "//div[contains(text(),'PC Laptops')]").click()

    driver.find_element(By.XPATH, "//div[@id='mainContent']//div//section[1]//div[2]//div[1]//div[1]//ul[1]//li[1]//a[1]").click()

    list_of_16GB_items = driver.find_elements(By.XPATH, "//ul[@class='b-list__items_nofooter']")
    for i in list_of_16GB_items:
        print(i.text)

    
