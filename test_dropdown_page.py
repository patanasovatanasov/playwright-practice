from playwright.sync_api import expect


def test_starting_value(dropdown_page):
    expect(dropdown_page.selected_option).to_have_text("Please select an option")

def test_select_1(dropdown_page):
    dropdown_page.select_options(1)
    expect(dropdown_page.selected_option).to_have_text("Option 1")

def test_select_2(dropdown_page):
    dropdown_page.select_options(2)
    expect(dropdown_page.selected_option).to_have_text("Option 2")