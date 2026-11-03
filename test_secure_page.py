import pytest
from playwright.sync_api import expect

def test_logout_button_visibility(secure_page):
    expect(secure_page.logout_button).to_be_visible()

def test_after_logout(secure_page, login_page):
    secure_page.logout()
    expect(login_page.page).to_have_url(login_page.URL+"login")
    expect(login_page.flash_login_msg).to_contain_text("You logged out of the secure area!")