from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("select").select_option(label="Option 2")
    print(page.locator("select option:checked").inner_text())
    browser.close()