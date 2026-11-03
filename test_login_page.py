import pytest
from playwright.sync_api import expect

def test_correct_login_page(page, login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.flash_login_msg).to_contain_text("You logged into a secure area")
    expect(login_page.page).to_have_url(login_page.URL+"secure")
@pytest.mark.parametrize("username, password, msg", [
    ("tOmsmith", "SuperSecretPassword!", "Your username is invalid"),
    ("tomsmith", "SuperSecretPassword", "Your password is invalid"),
    ("", "", "Your username is invalid")])
def test_wrong_logins(username, password, msg, login_page):
    login_page.login(username, password)
    expect(login_page.flash_login_msg).to_contain_text(msg)
    expect(login_page.page).to_have_url(login_page.URL+"login")
