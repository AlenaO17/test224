import pytest

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def test_isEven():
    result = isEven(6)
    assert result == True

def test_isEven_oldNumber():
    result = isEven(5)
    assert result == False