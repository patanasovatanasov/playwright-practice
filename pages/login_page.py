from playwright.sync_api import Page

URL = "https://the-internet.herokuapp.com/"

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_role("textbox", name="username")
        self.password_field = page.get_by_role("textbox", name="password")
        self.flash_login_msg = page.locator("#flash.flash")
        self.button = page.get_by_role("button", name=" Login")

    def login(self, user: str, password: str):
        self.username_field.fill(user)
        self.password_field.fill(password)
        self.button.click()

    def open(self):
        self.page.goto(URL+"login")
