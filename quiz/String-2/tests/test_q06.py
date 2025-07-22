import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import xyz_there

@pytest.mark.parametrize("input_str, expected", [
    ('abcxyz', True),
    ('abc.xyz', False),
    ('xyz.abc', True),
    ('abcxxyz', True),
    ('xyz', True),
    ('xy', False),
    ('x', False),
    ('', False),
    ('abc.xyzxyz', True),
    ('abc.xxyz', True),
    ('.xyz', False),
    ('12.xyz', False),
    ('12xyz', True),
    ('1.xyz.xyz2.xyz', False),
])
def test_xyz_there(input_str, expected):
    assert xyz_there(input_str) == expected
