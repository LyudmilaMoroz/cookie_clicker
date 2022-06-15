from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
shop = []
time_to_buy = time.time() + 10
game_over = time.time() + 300


def make_shop():
    all_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
    global shop
    for item in all_items:
        try:
            name = item.text.split("-")[0].strip()
            price = int(item.text.split("-")[1].replace(",", ""))
        except IndexError:
            pass
        else:
            shop.append({name: price})


def buy_item():
    global time_to_buy
    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    time_to_buy += 10
    for item in shop[::-1]:
        for name, price in item.items():
            if money > price:
                buy = driver.find_element(By.XPATH, f'// *[ @ id = "buy{name}"]')
                buy.click()
                time.sleep(0.1)

chrome_driver_path = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


make_shop()
while True:
    now = time.time()
    cookie.click()
    if now >= time_to_buy:
        buy_item()
    if now >= game_over:
        result = driver.find_element(By.ID, "cps").text
        print(f"Your result is: {result} cookies per second")
        break



