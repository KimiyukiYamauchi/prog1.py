import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import cigar_party

@pytest.mark.parametrize("cigars, is_weekend, expected", [
    (30, False, False),
    (50, False, True),
    (70, True, True),
    (30, True, False),
    (50, True, True),
    (60, False, True),
    (61, False, False),
    (40, False, True),
    (39, False, False),
    (40, True, True),
    (39, True, False),
])
def test_cigar_party(cigars, is_weekend, expected):
    assert cigar_party(cigars, is_weekend) == expected
