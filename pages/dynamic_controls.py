from playwright.sync_api import Page

class DynamicControlsPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.checkbox = page.get_by_role("checkbox")
        self.field = page.locator("#input-example").get_by_role("textbox")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.enable_button = page.get_by_role("button", name="Enable")
        self.add_button = page.get_by_role("button", name="Add")
        self.disable_button = page.get_by_role("button", name="Disable")
        self.enabled_msg = page.get_by_text("It's enabled!")
        self.disabled_msg = page.get_by_text("It's disabled!")
        self.cb_gone_msg = page.get_by_text("It's gone!")
        self.cb_back_msg = page.get_by_text("It's back!")

    def remove_checkbox(self):
        self.remove_button.click()

    def add_checkbox(self):
        self.add_button.click()

    def enable_field(self):
        self.enable_button.click()

    def disable_field(self):
        self.disable_button.click()

    def check_checkbox(self):
        self.checkbox.check()

    def type_text(self):
        self.field.type("test-123!")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dynamic_controls")