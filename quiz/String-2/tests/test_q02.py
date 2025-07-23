import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import count_hi

@pytest.mark.parametrize("input_str, expected", [
    ('abc hi ho', 1),
    ('ABChi hi', 2),
    ('hihi', 2),
    ('hiHIhi', 2),
    ('', 0),
    ('h', 0),
    ('hi', 1),
    ('Hi is no HI on ahI', 0),
    ('hiho not HOHihi', 2),
])
def test_count_hi(input_str, expected):
    assert count_hi(input_str) == expected
