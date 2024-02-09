import pytest


@pytest.mark.parametrize("component, result", [(5, 10), (2, 4)])
def test_addition(component, result):
    assert component + component == result
