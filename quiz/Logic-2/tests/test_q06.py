import pytest
from q06 import close_far

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 10, True),
    (1, 2, 3, False),
    (4, 1, 3, True),
    (4, 5, 3, False),
    (4, 3, 5, False),
    (-1, 10, 0, True),
    (0, -1, 10, True),
    (10, 10, 8, True),
    (10, 8, 9, False),
    (8, 9, 10, False),
    (8, 6, 9, True),
])
def test_close_far(a, b, c, expected):
    assert close_far(a, b, c) == expected
