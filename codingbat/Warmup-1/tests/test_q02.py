import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from q02 import monkey_trouble

@pytest.mark.parametrize("a_smile,b_smile,expected", [
    (True, True, True),
    (False, False, True),
    (True, False, False),
    (False, True, False),
])
def test_monkey_trouble(a_smile, b_smile, expected):
    assert monkey_trouble(a_smile, b_smile) == expected
