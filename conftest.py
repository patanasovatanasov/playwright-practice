import pytest
from pages.login_page import LoginPage
from pages.add_remove_page import AddRemovePage


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