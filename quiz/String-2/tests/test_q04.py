import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import count_code

@pytest.mark.parametrize("input_str, expected", [
    ('aaacodebbb', 1),
    ('codexxcode', 2),
    ('cozexxcope', 2),
    ('cozfxcope', 1),
    ('xxcozeyycop', 1),
    ('cozcop', 0),
    ('abcxyz', 0),
    ('code', 1),
    ('ode', 0),
    ('c', 0),
    ('', 0),
    ('AAcodeBBcoleCCcoreDD', 3),
    ('AAcodeBBcoleCCcorrDD', 2),
    ('coAcodeBcoleccoreDD', 3),
])
def test_count_code(input_str, expected):
    assert count_code(input_str) == expected
