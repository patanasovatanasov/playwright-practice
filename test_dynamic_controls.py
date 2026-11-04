from playwright.sync_api import expect
from pages.dynamic_controls import DynamicControlsPage
import pytest

def test_checking_checkbox(dynamic_controls_page):
    expect(dynamic_controls_page.checkbox).to_be_visible()
    expect(dynamic_controls_page.checkbox).not_to_be_checked()
    dynamic_controls_page.check_checkbox()
    expect(dynamic_controls_page.checkbox).to_be_checked()

def test_add_remove_checkbox(dynamic_controls_page):
    expect(dynamic_controls_page.checkbox).to_be_visible()
    dynamic_controls_page.remove_checkbox()
    expect(dynamic_controls_page.checkbox).to_be_hidden()
    expect(dynamic_controls_page.cb_gone_msg).to_be_visible()
    dynamic_controls_page.add_checkbox()
    expect(dynamic_controls_page.checkbox).to_be_visible()
    expect(dynamic_controls_page.cb_back_msg).to_be_visible()

def test_active_disabled_field(dynamic_controls_page):
    expect(dynamic_controls_page.field).to_be_disabled()
    dynamic_controls_page.enable_field()
    expect(dynamic_controls_page.field).to_be_enabled()
    expect(dynamic_controls_page.enabled_msg).to_be_visible()
    dynamic_controls_page.type_text("test-123!")
    expect(dynamic_controls_page.field).to_have_value("test-123!")
    dynamic_controls_page.disable_field()
    expect(dynamic_controls_page.disabled_msg).to_be_visible()
    expect(dynamic_controls_page.field).to_have_value("test-123!")