import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# https://github.com/usernam121
# cdp = "/home/vicracker/PycharmProjects/chromedriver-linux64/chromedriver"

driver = webdriver.Chrome()
driver.get("https://github.com/usernam121")
repo = "https://github.com/usernam121"
res = driver.find_elements(By.CLASS_NAME, "repo")

links = []
flink = []


def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "Box-sc-g0xbh4-0")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"found Password at: {second_page}")


def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    for a in res2:
        pass
    if "py" in a.text:
        second_page = f"{next_page}/blob/main/{a.text}"
        going_for_raw(second_page)


for i in res:
    links.append(i.text)


for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)


driver.quit()


