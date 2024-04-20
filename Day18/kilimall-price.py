import time

from selenium import webdriver
from selenium.webdriver.common.by import By
cdp = "/home/vicracker/PycharmProjects/chromedriver-linux64/chromedriver"
on = True
while on:
    def check_price():
        time.sleep(5)
        driver = webdriver.Chrome()

        driver.get("https://www.kilimall.co.ke/listing/2148051?sku_id=16279356&title=Fashion+Multi-pockets+Overalls+Men%26apos;s+Pants+Sportwear+Baggy+Casual+Joggers++Trousers+Sweatpants&image=https://image.kilimall.com/kenya/shop/store/goods/6818/2023/12/17014164260662dd68dd938714ff9acb369b78620ccd8_360.jpg.webp%23&source=&skuId=16279356")
        price = driver.find_element(By.CLASS_NAME, "sale-price")
        print(price.text)
        driver.quit()
    check_price()

# pending update
