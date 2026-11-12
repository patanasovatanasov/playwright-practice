import pytest

from pages.dropdown_page import Dropdown
from pages.checkboxes_page import Checkboxes
from pages.dynamic_controls import DynamicControlsPage
from pages.hovers_page import HoversPage
from pages.inputs_page import InputPage
from pages.key_presses_page import KeyPresses
from pages.login_page import LoginPage
from pages.add_remove_page import AddRemovePage
from pages.secure_page import SecurePage
from pages.tables_page import TablesPage
from bank_account import BankAccount
from playlist import Playlist


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def add_remove_page(page):
    ar = AddRemovePage(page)
    ar.open()
    return ar

@pytest.fixture
def secure_page(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    yield SecurePage(login_page.page)

@pytest.fixture
def inputs_page(page):
    ip = InputPage(page)
    ip.open()
    return ip

@pytest.fixture
def dynamic_controls_page(page):
    dc = DynamicControlsPage(page)
    dc.open()
    return dc

@pytest.fixture
def tables_page(page):
    tp = TablesPage(page)
    tp.open()
    return tp

@pytest.fixture
def hovers_page(page):
    h = HoversPage(page)
    h.open()
    return h

@pytest.fixture
def key_presses_page(page):
    kp = KeyPresses(page)
    kp.open()
    return kp

@pytest.fixture
def rock():
    pl1 = Playlist("Рок")
    return pl1

@pytest.fixture
def full_rock(rock):
    rock.add_song("song1")
    rock.add_song("song2")
    rock.add_song("song3")
    yield rock

@pytest.fixture
def acc():
    acc1 = BankAccount()
    return acc1

@pytest.fixture
def acc_100(acc):
    acc.add_money(100)
    return acc

@pytest.fixture
def checkboxes_page(page):
    boxes = Checkboxes(page)
    boxes.open()
    return boxes

@pytest.fixture
def dropdown_page(page):
    dd = Dropdown(page)
    dd.open()
    return dd