import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage, URL


def test_correct_login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.flash_login_msg).to_contain_text("You logged into a secure area")
    expect(page).to_have_url(URL+"secure")

def test_incorrect_login_name(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tOmsmith", "SuperSecretPassword!")
    expect(login_page.flash_login_msg).to_contain_text("Your username")
    expect(page).to_have_url(URL+"login")

def test_correct_login_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword")
    expect(login_page.flash_login_msg).to_contain_text("Your password")
    expect(page).to_have_url(URL+"login")

def test_empty_login_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")
    expect(login_page.flash_login_msg).to_contain_text("Your username")
    expect(page).to_have_url(URL+"login")
