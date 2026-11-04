from playwright.sync_api import Page


class TablesPage:
    URL = "https://the-internet.herokuapp.com/tables"

    def __init__(self, page: Page):
        self.page = page
        self.rows = page.locator("#table1 tbody tr")

    def open(self):
        self.page.goto(self.URL)

    def row_by_last_name(self, last_name: str):
        return self.rows.filter(has_text=last_name)

    def email_of(self, last_name: str):
        row = self.row_by_last_name(last_name)
        return row.locator("td").nth(2)

    def sort_by(self, column):
        self.page.locator("#table1").get_by_text(column).click()

