from playwright.sync_api import Page

class InputPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_field = page.get_by_role("spinbutton")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/inputs")

    def enter(self, value):
        self.input_field.fill(value)