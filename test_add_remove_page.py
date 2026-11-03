import pytest
from playwright.sync_api import Page, expect
from pages.add_remove_page import AddRemovePage

def test_add_remove_page(page: Page):
    ar = AddRemovePage(page)
    ar.open()
    expect(ar.delete_buttons).to_have_count(0)

@pytest.mark.parametrize("n", [1, 3, 5])
def test_parametrize(page, n):
    ar = AddRemovePage(page)
    ar.open()
    ar.add(n)
    expect(ar.delete_buttons).to_have_count(n)

def test_remove_one(page):
    ar = AddRemovePage(page)
    ar.open()
    ar.add(2)
    ar.delete_one()
    expect(ar.delete_buttons).to_have_count(1)