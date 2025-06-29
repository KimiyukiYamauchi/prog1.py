# test_sleep.py
import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from q01 import sleep_in

@pytest.mark.parametrize("weekday,vacation,expected", [
    (False, False, True),
    (True, False, False),
    (False, True, True),
    (True, True, True),
])
def test_sleep_in(weekday, vacation, expected):
    assert sleep_in(weekday, vacation) == expected
