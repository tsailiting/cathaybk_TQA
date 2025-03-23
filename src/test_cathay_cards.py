from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=True")  # Headless 模式
    chrome_options.add_argument("--disable-gpu")  # 無 GPU 環境避免錯誤
    chrome_options.add_argument("--no-sandbox")   # 容器中需開啟
    chrome_options.add_argument("--disable-dev-shm-usage")  # 避免內存限制問題
    # 固定視窗尺寸 iPhone 14 Pro 393 x 852
    chrome_options.add_argument("--window-size=393,852")

    # driver = webdriver.Chrome(service=Service(
    #     ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome(service=Service(
        "/usr/bin/chromedriver"), options=chrome_options)
    return driver


def wait_for(seconds=2):
    time.sleep(seconds)


def capture_and_count_cards():
    driver = init_driver()
    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    wait_for(3)
    driver.save_screenshot("1_home_page.png")

    # 展開選單：個人金融 > 產品介紹 > 信用卡
    menu_button = driver.find_element(By.CSS_SELECTOR, 'a[data-burger]')
    menu_button.click()
    wait_for(1)

    # driver.find_element(By.LINK_TEXT, "個人金融").click()
    # wait_for(1)
    driver.find_element(By.XPATH, '//div[text()="產品介紹"]').click()
    wait_for(1)
    driver.find_element(By.XPATH, '//div[text()="信用卡"]').click()
    wait_for(3)

    # 進入信用卡列表頁
    driver.save_screenshot("2_credit_card_menu.png")

    card_items = driver.find_elements(
        By.XPATH,
        '//div[text()="信用卡"]/ancestor::div[contains(@class,"cubre-o-menuLinkList__item")]//a[contains(@class,"cubre-a-menuLink")]'
    )

    print(f"信用卡選單項目數量: {len(card_items)}")

    driver.find_element(By.XPATH, '//a[text()="卡片介紹"]').click()
    wait_for(3)

    # 點選其中一個選項：例如「停發卡」
    stop_card_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[p[text()="停發卡"]]'))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({ inline: 'end' });", stop_card_tab)
    driver.find_element(
        By.XPATH, '//a[contains(@class,"cubre-m-anchor__btn")]//p[text()="停發卡"]/..').click()
    wait_for(3)
    driver.save_screenshot("3_stop_cards.png")

    retired_section = driver.find_element(
        By.XPATH, "//div[contains(., '停發卡') and contains(@class, 'cubre-o-block__wrap')]")
    pagination_bullets = retired_section.find_elements(
        By.CSS_SELECTOR, ".swiper-pagination-bullet")

    print(f"停發卡卡片數量: {len(pagination_bullets)}")

    driver.quit()


if __name__ == "__main__":
    capture_and_count_cards()
