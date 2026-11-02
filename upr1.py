from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com")
    a = 0
    with open("test.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["#", "quote", "author", "tags"])
        while True:
            quotes = page.locator(".quote")
            for q in quotes.all():
                text = q.locator(".text").inner_text()
                author = q.locator(".author").inner_text()
                tag = q.locator(".tag").all_inner_texts()
                tag_str = ", ".join(tag)
                a += 1
                print(f"{a} - {text} - {author} [{tag_str}]")
                writer.writerow([a, text, author, tag_str])
            nxt = page.locator("li.next a")
            if nxt.count() == 0:
                break
            nxt.click()
            page.wait_for_load_state()
    browser.close()