import pytest
from playwright.sync_api import expect

def test_row_count(tables_page):
    expect(tables_page.rows).to_have_count(4)

@pytest.mark.parametrize("last_name, email", [
    ("Smith", "jsmith@gmail.com"),
    ("Doe", "jdoe@hotmail.com"),
    ("Conway", "tconway@earthlink.net")])
def test_email_by_last_name(tables_page, last_name, email):
    expect(tables_page.email_of(last_name)).to_have_text(email)

def test_sort_by_last_name(tables_page):
    expect(tables_page.rows.first).to_contain_text("Smith")
    tables_page.sort_by("Last name")
    expect(tables_page.rows.first).to_contain_text("Bach")