import pytest

from pages.inputs_page import InputPage
from pages.login_page import LoginPage
from pages.add_remove_page import AddRemovePage
from pages.secure_page import SecurePage


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def add_remove_page(page):
    ar = AddRemovePage(page)
    ar.open()
    return ar

@pytest.fixture
def secure_page(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    yield SecurePage(login_page.page)

@pytest.fixture
def inputs_page(page):
    ip = InputPage(page)
    ip.open(page)
    return ip
