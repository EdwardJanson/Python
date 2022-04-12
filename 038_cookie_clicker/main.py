from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ---------- Driver setup ---------- #

chrome_service = Service("Your Chrome driver path")
driver = webdriver.Chrome(service=chrome_service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

# ---------- Find elements ---------- #

big_cookie = driver.find_element(By.ID, "bigCookie")

# ---------- Run game ---------- #

GAME_TIME = 300
purchase_time = 5
game_continues = True


def cookie_number():
    return int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))


def purchase_timer():
    if time.time() - start_purchase_time > purchase_time:
        return True
    else:
        return False


start_game_timer = time.time()
start_purchase_time = time.time()

while time.time() - start_game_timer < GAME_TIME:
    big_cookie.click()
    product_elements = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    while purchase_timer():
        product_list = []
        for product_element in product_elements:
            product_cost = int(product_element.find_element(By.CLASS_NAME, "price").text.replace(",", ""))
            product_dict = {product_element: product_cost}
            product_list.insert(0, product_dict)
        for product in product_list:
            product_cost = int(list(product.values())[0])
            while cookie_number() > product_cost:
                list(product.keys())[0].click()
        start_purchase_time = time.time()
        purchase_time += 1
        purchase_timer()

cookies_per_second = driver.find_element(By.CSS_SELECTOR, "#cookies div").text.split(" : ")[1]

print(cookies_per_second)

driver.quit()
