import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("n", [1, 2, 3])
def test_before_hover(hovers_page, n):
    expect(hovers_page.text_on_hover(n)).to_be_hidden()

@pytest.mark.parametrize("n", [1, 2, 3])
def test_after_hover(hovers_page, n):
    hovers_page.hover(n)
    expect(hovers_page.text_on_hover(n)).to_have_text(f"name: user{n}")
    if n == 2:
        expect(hovers_page.text_on_hover(n - 1)).to_be_hidden()
        expect(hovers_page.text_on_hover(n + 1)).to_be_hidden()