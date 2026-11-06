import pytest

def test_acc_balance_0(acc):
    assert acc.balance == 0

def test_acc_balance_after_add(acc_100):
    assert acc_100.balance == 100

def test_both_fixtures(acc, acc_100):
    assert acc.balance == 100
    assert acc_100.balance == 100