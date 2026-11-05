from playwright.sync_api import Page

class KeyPresses:
    def __init__(self, page: Page):
        self.page = page
        self.example = page.locator("#content")
        self.msg = self.example.locator("#result")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/key_presses")

    def press_key(self, k):
        self.example.locator("#target").press(k)

