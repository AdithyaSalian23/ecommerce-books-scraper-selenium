import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

MAX_PRICE = 20.0

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("category", ["Fiction", "Science", "Travel"])
def test_scrape_books(driver, category):
    start_time = time.time()

    url = "http://books.toscrape.com/"
    driver.get(url)
    driver.find_element(By.LINK_TEXT, category).click()

    books = driver.find_elements(By.CLASS_NAME, "product_pod")
    filtered_books = []

    for book in books:
        title = book.find_element(By.TAG_NAME, "h3").text
        price_text = book.find_element(By.CLASS_NAME, "price_color").text.replace('£', '')
        availability = book.find_element(By.CLASS_NAME, "instock").text.strip()

        price = float(price_text)
        if price < MAX_PRICE:
            filtered_books.append([title, price, availability])

    # Save filtered books to Excel
    os.makedirs("exports", exist_ok=True)
    file_path = os.path.join("exports", f"{category}_under_{int(MAX_PRICE)}.xlsx")

    wb = Workbook()
    ws = wb.active
    ws.append(["Title", "Price (£)", "Availability"])
    for row in filtered_books:
        ws.append(row)
    wb.save(file_path)

    duration = round(time.time() - start_time, 2)
    print(f"✅ {category} - {len(filtered_books)} books under £{MAX_PRICE} saved in {duration} seconds.")
