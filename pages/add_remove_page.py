from playwright.sync_api import Page

class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_buttons = page.get_by_role("button", name="Delete")

    def open(self):
        self.page.goto(self.URL)

    def add(self, n):
        for _ in range(n):
            self.add_button.click()

    def delete_one(self):
        self.delete_buttons.nth(-1).click()