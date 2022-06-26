import pytest

import threefive


def test_three_five_with_one():
    test_number = 1
    result = threefive.three_five(test_number)
    assert result == test_number


def test_three_five_with_zero():
    test_number = 0
    result = threefive.three_five(test_number)
    assert result == "ThreeFive"


def test_three_five_with_three():
    test_number = 3
    result = threefive.three_five(test_number)
    assert result == "Three"


def test_three_five_with_five():
    test_number = 5
    result = threefive.three_five(test_number)
    assert result == "Five"


def test_three_five_with_negative():
    test_number = -3
    result = threefive.three_five(test_number)
    assert result == "Three"


def test_three_five_with_multiple_of_both():
    test_number = 15
    result = threefive.three_five(test_number)
    assert result == "ThreeFive"


def test_three_five_with_none():
    test_number = None
    with pytest.raises(TypeError):
        result = threefive.three_five(test_number)