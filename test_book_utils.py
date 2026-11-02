from books_utils import *

def test_clean_price_normal():
    assert clean_price("£51.77") == 51.77

def test_stock_count_normal():
    assert stock_count("In stock (22 available)") == 22

def test_rating_to_int_normal():
    assert rating_to_int("One") == 1

def test_is_long_enough_normal():
    assert is_long_enough("One") == False

def test_stock_count_out_of_stock():
    assert stock_count("Out of stock") == 0

def test_has_at_sign():
    assert has_at_sign("petar@mail.com") == True

def test_has_at_sign_no_at_sign():
    assert has_at_sign("petar.mail.com") == False

def test_has_at_sign_none():
    assert has_at_sign("") == False