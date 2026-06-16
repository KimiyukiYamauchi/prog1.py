import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import cat_dog

@pytest.mark.parametrize("input_str, expected", [
    ('catdog', True),
    ('catcat', False),
    ('1cat1cadodog', True),
    ('catxdogxxxdog', False),
    ('catxdogxdogxcat', True),
    ('catxdogxdogxca', False),
    ('dogdogcat', False),
    ('dog', False),
    ('cat', False),
    ('ca', True),
    ('c', True),
    ('', True),
])
def test_cat_dog(input_str, expected):
    assert cat_dog(input_str) == expected
