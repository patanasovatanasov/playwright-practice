import pytest
from playwright.sync_api import expect, Page

def go_to_page(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

@pytest.mark.parametrize("label, value", [("Option 1", "1"), ("Option 2", "2")])

def test_dropdown(page, label, value):
    go_to_page(page)
    page.locator("#dropdown").select_option(label=label)
    expect(page.locator("#dropdown")).to_have_value(value)