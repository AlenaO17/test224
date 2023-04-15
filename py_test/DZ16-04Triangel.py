import pytest
def is_valid_side(*sides):  # * -плавающее кол-во параметров
    for side in sides:
        if side <= 0:
            return False
    return True

def isTriangle(a, b, c):
    if is_valid_side(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
    return False
def is_valid_side(*sides):
    for side in sides:
        if side <= 0:
            return False
    return True
def isTriangle(a, b, c):
    if is_valid_side(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
    return False
def test_is_valid_side():
    result = is_valid_side(5, 5, 5)
    assert result == True
def test_is_valid_side():
    result = is_valid_side(5, 0, 5)
    assert result == False
def test_is_valid_side():
    result = is_valid_side(5, -8, 5)
    assert result == False
def test_isTriangle():
    result = isTriangle(1, 4, 5)
    assert result == False
def test_isTriangle():
    result = isTriangle(f, 4, 5)
    assert result == True
# Конечный вариант1
