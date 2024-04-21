import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.minimize_window()  #background
target = input("Enter Target Github Account(e.g.usernam121): ")
target.removeprefix("https://github.com/")
home = f"https://github.com/{target}"
page_1 = f"https://github.com/{target}?tab=repositories"
driver.get(page_1)
time.sleep(1)
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
links = []
repo_links = []
for i in res:
    suffix = "Public" or "Private"
    link_txt = i.text.removesuffix(suffix)
    links.append(link_txt)
num = 1
for link in links:
    link = f"{home}/{link}"
    # print(f"{num}.{link}")
    repo_links.append(link)
    num += 1
# print(real_links)
for r_link in repo_links:
    driver.get(r_link)
    print(f"Got {r_link}")
driver.quit()
# overflow-hidden
