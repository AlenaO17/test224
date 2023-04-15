import pytest

from Wallet import* # подключаем все классы и методы


def test_default_inital_ammount():
    empty_wallet = Wallet()
    # print(empty_wallet.get_balance())
    assert empty_wallet.get_balance() == 0

def test_add_cash():
    empty_wallet = Wallet()
    empty_wallet.add_cash(100)
    assert empty_wallet.get_balance() == 100

