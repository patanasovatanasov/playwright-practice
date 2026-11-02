from playwright.sync_api import expect, Page


def test_check_box(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.locator("input[type='checkbox']")
    box1 = boxes.nth(0)
    box2 = boxes.nth(1)
    box1.check()
    box2.check()
    expect(box1).to_be_checked()
    expect(box2).to_be_checked()

def test_uncheck_box(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.locator("input[type='checkbox']")
    box1 = boxes.nth(0)
    box2 = boxes.nth(1)
    box1.uncheck()
    box2.uncheck()
    expect(box1).not_to_be_checked()
    expect(box2).not_to_be_checked()