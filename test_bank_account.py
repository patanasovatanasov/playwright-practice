import pytest
from bank_account import BankAccount

def test_new_acc():
    user1 = BankAccount()
    assert user1.balance == 0

def test_add_money():
    user1 = BankAccount()
    user1.add_money(100)
    assert user1.balance == 100

def test_withdraw_all_money():
    user1 = BankAccount()
    user1.add_money(100)
    assert user1.balance == 100
    user1.withdraw_money(100)
    assert user1.balance == 0

def test_withdraw_more_than_balance():
    user1 = BankAccount()
    user1.add_money(100)
    assert user1.balance == 100
    with pytest.raises(ValueError):
        user1.withdraw_money(1000)
    assert user1.balance == 100

@pytest.mark.parametrize("n", [0, -50])
def test_wrong_add_amounts(n):
    user1 = BankAccount()
    with pytest.raises(ValueError):
        user1.add_money(n)

def test_two_different_accounts():
    user1 = BankAccount()
    user2 = BankAccount()
    user1.add_money(100)
    assert user1.balance != user2.balance