from playwright.sync_api import Page

class HoversPage:
    URL = "https://the-internet.herokuapp.com/hovers"
    def __init__(self, page: Page):
        self.page = page
        self.img_and_text = page.locator(".figure")

    def open(self):
        self.page.goto(self.URL)

    def hover(self, n):
        self.img_and_text.nth(n - 1).locator("img").hover()

    def text_on_hover(self, n):
        return self.img_and_text.nth(n -1).get_by_role("heading")

