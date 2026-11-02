from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.locator("input[type='checkbox']")
    box1 = boxes.nth(0)
    box2 = boxes.nth(1)
    box1.check()
    box2.uncheck()
    print("Box 1: ", box1.is_checked())
    print("Box 2: ", box2.is_checked())
    browser.close()