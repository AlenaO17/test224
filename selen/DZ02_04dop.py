from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random

from datetime import datetime

now = datetime.now()
day = random.randint(1, 31)
month = random.randint(1, 12)
year = random.randint(2000, 2020)
date_ron = now.strftime("%m/%d/%Y")
print(date_ron)

driver = webdriver.Chrome()
driver.get("https://makarova1507ana.github.io/registration_page/")
date = driver.find_element(By.XPATH,"/html/body/main/form/input[4]")
date.send_keys(date_ron)
elements = driver.find_elements(By.TAG_NAME, "input")
for i in range(9):
    if i == 6:
        elements[i].send_keys("9529083502")
    if i == 7:
        elements[i].send_keys("Russia")
    if i == 8:
        elements[i].send_keys("owcg4589")
time.sleep(5)
name = 'Images/2.png'
print(name)
driver.save_screenshot(name)
driver.quit()