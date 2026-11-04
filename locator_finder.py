from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    br = playwright.chromium.launch(headless=False)
    page = br.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    page.pause()

