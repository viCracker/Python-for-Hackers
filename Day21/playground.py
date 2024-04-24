import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def loop(resource):
    for n_link in resource:
        pg = n_link.text
        if "." in pg:
            print(f"{pg} - File")
        else:
            print(f"{pg} - Folder")
            page3 = f"{r_link}/tree/main/{pg}"
            driver.get(page3)
            print(f"     >got:{page3}")
            time.sleep(2)
            res3 = driver.find_elements(By.CLASS_NAME, "react-directory-row-name-cell-large-screen")
            for shit in res3:
                loop(res3)


driver = webdriver.Chrome()
# driver.minimize_window()  #background
target = "deniskamurua"
target.removeprefix("https://github.com/")
home = f"https://github.com/{target}"
page_1 = f"https://github.com/{target}?tab=repositories"
driver.get(page_1)
# time.sleep(1)
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
links = []
repo_links = []
for i in res:
    suffix = " Public" or " Private"
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
    time.sleep(2)
    res2 = driver.find_elements(By.CLASS_NAME, "react-directory-row-name-cell-large-screen")
    loop(res2)


driver.quit()
# overflow-hidden
