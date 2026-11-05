import pytest
from playwright.sync_api import expect

def test_before_press(key_presses_page):
    expect(key_presses_page.msg).to_be_hidden()

@pytest.mark.parametrize("keys ,message", [("T", "T"),
                                           ("3", "3"),
                                           ("$", "4"),
                                           ("7", "7"),
                                           ("Alt", "ALT")])
def test_5_keys(key_presses_page, keys, message):
    key_presses_page.press_key(keys)
    expect(key_presses_page.msg).to_have_text(f"You entered: {message}")

def test_2_keys_in_a_row(key_presses_page):
    key_presses_page.press_key("A")
    key_presses_page.press_key("B")
    expect(key_presses_page.msg).to_have_text("You entered: B")