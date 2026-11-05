import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("n", [1, 2, 3])
def test_before_hover(hovers_page, n):
    expect(hovers_page.text_on_hover(n)).to_be_hidden()

@pytest.mark.parametrize("n", [1, 2, 3])
def test_after_hover(hovers_page, n):
    hovers_page.hover(n)
    expect(hovers_page.text_on_hover(n)).to_be_visible()
    expect(hovers_page.text_on_hover(n)).to_have_text(f"name: usr{n}")
    for other in [1, 2, 3]:
        if other != n:
            expect(hovers_page.text_on_hover(other)).to_be_hidden()