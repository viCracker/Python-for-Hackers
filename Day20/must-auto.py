import time

from selenium import webdriver
from selenium.webdriver.common.by import By

uname = input("Registration Number: ")
passwd = input("Password: ")
driver = webdriver.Chrome()
driver.get("https://student.must.ac.ke")
driver.find_element("id", "Main_RegNo").send_keys(uname)
driver.find_element("id", "Main_password").send_keys(passwd)
driver.find_element("id", "Main_btnLogin").click()
time.sleep(2)
driver.close()
