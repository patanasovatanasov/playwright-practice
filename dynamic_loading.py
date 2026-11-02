from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("#start button").click()
    expect(page.locator("#finish h4")).to_be_visible(timeout=10000)
    print(page.locator("#finish h4").inner_text())
    browser.close()

