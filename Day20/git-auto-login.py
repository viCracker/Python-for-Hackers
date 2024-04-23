import time

from selenium import webdriver
from selenium.webdriver.common.by import By

uname = input("Username: ")
passwd = input("Password: ")
driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.find_element("id", "login_field").send_keys(uname)
driver.find_element("id", "password").send_keys(passwd)
driver.find_element("name", "commit").click()
time.sleep(10)
driver.quit()
