import pytest
from q07 import make_chocolate

@pytest.mark.parametrize("small, big, goal, expected", [
    (4, 1, 9, 4),
    (4, 1, 10, -1),
    (4, 1, 7, 2),
    (6, 2, 7, 2),
    (4, 1, 5, 0),
    (4, 1, 4, 4),
    (5, 4, 9, 4),
    (9, 3, 18, 3),
    (3, 1, 9, -1),
    (1, 2, 7, -1),
    (1, 2, 6, 1),
    (1, 2, 5, 0),
    (6, 1, 10, 5),
    (6, 1, 11, 6),
    (6, 1, 12, -1),
    (6, 1, 13, -1),
    (6, 2, 10, 0),
    (6, 2, 11, 1),
    (6, 2, 12, 2),
    (60, 100, 550, 50),
    (1000, 1000000, 5000006, 6),
    (7, 1, 12, 7),
    (7, 1, 13, -1),
    (7, 2, 13, 3),
])
def test_make_chocolate(small, big, goal, expected):
    assert make_chocolate(small, big, goal) == expected
