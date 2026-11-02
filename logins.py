from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    attempts = [("tomsmith", "SuperSecretPassword!"), ("tomsmith", "wrong")]
    for user, password in attempts:
        page.goto("https://the-internet.herokuapp.com/login")
        print(f"{user}:{password}")
        page.locator("#username").fill(user)
        page.locator("#password").fill(password)
        page.locator("button[type=submit]").click()
        print(f"{page.locator("#flash").inner_text().strip().split("\n")[0]}")
        if page.url == "https://the-internet.herokuapp.com/secure":
            print("Success!")
        else:
            print("Failure!")
    browser.close()