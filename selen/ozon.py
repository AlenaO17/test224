import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestMainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ozon.ru/")

    def test_ozon(self):
        driver = self.driver
        driver.find_element(By.NAME, "text").click()
        driver.find_element(By.NAME, "text").send_keys("кофемолка")
        time.sleep(8)
        name = 'Images/4.png'
        print(name)
        driver.save_screenshot(name)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div[3]/div/div/form/div[2]/button/span").click()
        self.assertNotEqual(self.driver.current_url, "https://www.ozon.ru/")

