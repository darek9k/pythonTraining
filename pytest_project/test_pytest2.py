import pytest


def test_method_2():
    x = 3
    y = 2
    assert x+y == 5, "Assertion success, Expected 5"
    assert x+y != 2, "Assertion failed, Expected 2"
