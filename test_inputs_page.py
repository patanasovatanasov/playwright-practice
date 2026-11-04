import pytest
from playwright.sync_api import Error, expect


@pytest.mark.parametrize("value", ["5", "-3", "0"])
def test_inputs_page(inputs_page, value):
    inputs_page.enter(value)
    expect(inputs_page.input_field).to_have_value(value)

def test_inputs_abc(inputs_page):
    inputs_page.input_field.press_sequentially("abc")
    expect(inputs_page.input_field).to_have_value("")

def test_inputs_abc_error(inputs_page):
    with pytest.raises(Error):
        inputs_page.enter("abc")