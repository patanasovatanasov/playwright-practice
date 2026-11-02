from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"

def login(page, user, password):
    page.goto(f"{BASE_URL}/login")
    page.get_by_role("textbox", name="Username").fill(user)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name=" Login").click()

def test_login_success(page: Page):
    login(page, "tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url(f"{BASE_URL}/secure")
    expect(page.get_by_text("You logged into a secure area")).to_be_visible()
def test_login_wrong_pwd(page: Page):
    login(page, "tomsmith", "SuperSecretPassword!1")

    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.get_by_text("Your password is invalid!")).to_be_visible()

def test_login_wrong_user(page: Page):
    login(page, "t0msmith", "SuperSecretPassword!")

    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")