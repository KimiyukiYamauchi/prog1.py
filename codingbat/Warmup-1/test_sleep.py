# test_sleep.py

import pytest
from sleep import sleep_in

@pytest.mark.parametrize("weekday,vacation,expected", [
    (False, False, True),
    (True, False, False),
    (False, True, True),
])
def test_sleep_in(weekday, vacation, expected):
    assert sleep_in(weekday, vacation) == expected
