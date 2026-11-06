from playwright.sync_api import Page

class Checkboxes:
    def __init__(self, page):
        self.page = page
        self.boxes_id = page.locator("#checkboxes")
        self.box = self.boxes_id.locator("input[type='checkbox']")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def toggle(self, b):
        self.box.nth(b).click()
