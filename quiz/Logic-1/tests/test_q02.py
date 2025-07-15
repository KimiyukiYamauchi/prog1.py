import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import date_fashion

@pytest.mark.parametrize("you, date, expected", [
    (5, 10, 2),
    (5, 2, 0),
    (5, 5, 1),
    (3, 3, 1),
    (10, 2, 0),
    (2, 9, 0),
    (9, 9, 2),
    (10, 5, 2),
    (2, 2, 0),
    (3, 7, 1),
    (3, 2, 0),
    (6, 2, 0),
])
def test_date_fashion(you, date, expected):
    assert date_fashion(you, date) == expected
