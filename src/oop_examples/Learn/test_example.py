"""Basic Unit testing for example.py"""
from random import randint
import pytest
from example import increment, COLORS


def test_increment():
    """Testing increment function"""
    test_value = randint(100, 1000)

    assert increment(3) == 4