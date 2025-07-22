import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import end_other

@pytest.mark.parametrize("a, b, expected", [
    ('Hiabc', 'abc', True),
    ('AbC', 'HiaBc', True),
    ('abc', 'abXabc', True),
    ('Hiabc', 'abcd', False),
    ('Hiabc', 'bc', True),
    ('Hiabcx', 'bc', False),
    ('abc', 'abc', True),
    ('xyz', '12xyz', True),
    ('yz', '12xz', False),
    ('Z', '12xz', True),
    ('12', '12', True),
    ('abcXYZ', 'abcDEF', False),
    ('ab', '12ab', True),
    ('ab', 'ab12', False),
])
def test_end_other(a, b, expected):
    assert end_other(a, b) == expected
