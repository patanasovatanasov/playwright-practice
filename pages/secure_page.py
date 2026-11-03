from playwright.sync_api import Page

class SecurePage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.get_by_role("link", name="Logout")
    def logout(self):
        self.logout_button.click()
