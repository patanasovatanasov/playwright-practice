import pytest
from playwright.sync_api import expect


def test_starting_value(dropdown_page):
    expect(dropdown_page.selected_option).to_have_text("Please select an option")

@pytest.mark.parametrize("v", [1, 2])
def test_select_1(dropdown_page, v):
    dropdown_page.select_options(v)
    expect(dropdown_page.checked_option).to_have_text(f"Option {v}")