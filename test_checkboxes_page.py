import pytest
from playwright.sync_api import expect

def test_start_status(checkboxes_page):
    expect(checkboxes_page.box.nth(0)).not_to_be_checked()
    expect(checkboxes_page.box.nth(1)).to_be_checked()

@pytest.mark.parametrize("b", [0, 1])
def test_check_uncheck(checkboxes_page, b):
    expect(checkboxes_page.box.nth(0)).not_to_be_checked()
    expect(checkboxes_page.box.nth(1)).to_be_checked()
    checkboxes_page.toggle(b)
    if b == 0:
        expect(checkboxes_page.box.nth(b)).to_be_checked()
    else:
        expect(checkboxes_page.box.nth(b)).not_to_be_checked()

def test_double_check(checkboxes_page):
    expect(checkboxes_page.box.nth(0)).not_to_be_checked()
    expect(checkboxes_page.box.nth(1)).to_be_checked()
    checkboxes_page.toggle(0)
    checkboxes_page.toggle(1)
    expect(checkboxes_page.box.nth(0)).to_be_checked()
    expect(checkboxes_page.box.nth(1)).not_to_be_checked()
    checkboxes_page.toggle(0)
    checkboxes_page.toggle(1)
    expect(checkboxes_page.box.nth(0)).not_to_be_checked()
    expect(checkboxes_page.box.nth(1)).to_be_checked()