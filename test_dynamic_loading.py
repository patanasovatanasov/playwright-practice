from playwright.sync_api import Page, expect

def test_loading(page):
    result = page.locator("#finish h4")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    expect(page.locator("#finish h4")).to_be_hidden()
    page.locator("#start button").click()

    expect(result).to_be_visible(timeout=10000)
    expect(result).to_have_text("Hello World!")