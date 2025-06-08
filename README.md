# 📚 E-commerce Book Scraper with Selenium & Pytest

This project automates testing on [Books to Scrape](http://books.toscrape.com) using **Selenium**, **Pytest**, and **openpyxl**.

It scrapes book data by category, filters books priced under **£20**, and exports the results to Excel! 📊

---

## 🚀 Features

- 🔍 Test book categories: `Fiction`, `Science`, `Travel`
- 🏷️ Filter books priced under £20
- 📄 Save results to `.xlsx` using `openpyxl`
- ⏱️ Log test execution time

---

## 🧰 Tech Stack

- Python 🐍
- Selenium 🔧
- Pytest ✅
- openpyxl 📘

---

## ▶️ How to Run

1. 📦 Install requirements:
   ```bash
   pip install selenium pytest openpyxl
   ```

2. ▶️ Run test:
   ```bash
   pytest test_books.py
   ```

3. 📁 Check the `exports/` folder for Excel files.

---

## 📂 Folder Structure
```bash
.
├── test_books.py
├── exports/
│   ├── Fiction_under_20.xlsx
│   ├── Science_under_20.xlsx
│   └── Travel_under_20.xlsx
```

---

## 📝 Author
Adithya Salian
