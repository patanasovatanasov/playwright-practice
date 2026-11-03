import pytest
from playwright.sync_api import Page, expect

URL = "https://the-internet.herokuapp.com/add_remove_elements/"

def del_button(page: Page):
    return page.get_by_role("button", name="Delete")

def add_button(page: Page):
    return page.get_by_role("button", name="Add Element")

def test_beginning(page: Page):
    page.goto(URL)
    expect(del_button(page)).to_have_count(0)

@pytest.mark.parametrize("n", [1, 3, 5])
def test_parametric(page: Page, n):
    page.goto(URL)
    for _ in range(n):
        add_button(page).click()
    expect(del_button(page)).to_have_count(n)

def test_remove_buttons(page: Page):
    page.goto(URL)
    for _ in range(3):
        add_button(page).click()
    del_button(page).nth(-1).click()
    expect(del_button(page)).to_have_count(2)
