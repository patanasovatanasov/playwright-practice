import pytest
from playwright.sync_api import expect

def test_add_remove_page(add_remove_page):
    expect(add_remove_page.delete_buttons).to_have_count(0)

@pytest.mark.parametrize("n", [1, 3, 5])
def test_parametrize(n, add_remove_page):
    add_remove_page.add(n)
    expect(add_remove_page.delete_buttons).to_have_count(n)

def test_remove_one(add_remove_page):
    add_remove_page.add(2)
    add_remove_page.delete_one()
    expect(add_remove_page.delete_buttons).to_have_count(1)