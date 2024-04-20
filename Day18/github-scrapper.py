import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# https://github.com/usernam121
# cdp = "/home/vicracker/PycharmProjects/chromedriver-linux64/chromedriver"

driver = webdriver.Chrome()
driver.get("https://github.com/usernam121?tab=repositories")
time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")

for i in res:
    print(i.text)
driver.quit()

