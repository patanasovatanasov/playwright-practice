import pytest
from playwright.sync_api import Page, expect


from test_login import login

BASE_URL = "https://the-internet.herokuapp.com"

@pytest.mark.parametrize("user, password, message", [
    ("tomsmith", "wrong",                "Your password is invalid!"),
    ("nobody",   "SuperSecretPassword!", "Your username is invalid!"),
    ("", "", "Your username is invalid!")
])
def test_login_fails(page: Page, user, password, message):
    login(page, user, password)
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.locator("#flash")).to_contain_text(message)