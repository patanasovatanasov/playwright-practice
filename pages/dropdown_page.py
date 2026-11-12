from playwright.sync_api import Page

class Dropdown:
    def __init__(self, page):
        self.page = page
        self.dropdown = page.locator("#dropdown")
        self.selected_option = self.dropdown.locator("option[selected]")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def select_options(self, c):
        self.dropdown.select_option(label=f"Option {c}")