from playwright.sync_api import sync_playwright
import csv
from urllib.parse import urljoin

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com")
    total = 0
    a = 0
    ratings = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5}
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["a", "title", "price", "stock", "stock_num", "stars"])
        while True:
            articles = page.locator("article.product_pod")
            for article in articles.all():
                title_text = article.locator("h3 a").get_attribute("title")
                price = article.locator("p.price_color").inner_text()
                stock = article.locator("p.instock").inner_text().strip()
                stars = article.locator(".star-rating").get_attribute("class")
                rating = ratings[stars.split()[1]]
                price_a = price.replace("£", "")
                total += float(price_a)
                link = article.locator("h3 a").get_attribute("href")
                page.goto(urljoin(page.url, link))
                stock_num = page.locator(".product_main .instock").inner_text().split()
                stock_num1 = stock_num[2].replace('(', '')
                a = a + 1
                print(f"{a}. {title_text} - {price_a} - {stock} - {stock_num1} - {rating}")
                writer.writerow([a, title_text, price_a, stock, stock_num1, rating])
                page.go_back()
            nxt = page.locator("li.next a")
            if a >= 20:
                break
            if nxt.count() == 0:
                break
            nxt.click()
            page.wait_for_load_state()
        avg = total / a
        print(f"{avg:.2f}")
        browser.close()