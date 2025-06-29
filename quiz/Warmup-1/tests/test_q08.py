import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q08 import pos_neg

@pytest.mark.parametrize("a, b, negative, expected", [
    (1, -1, False, True),
    (-1, 1, False, True),
    (-4, -5, True, True),
    (-4, -5, False, False),
    (-4, 5, False, True),
    (-4, 5, True, False),
    (1, 1, False, False),
    (1, 1, True, False),
    (-1, -1, False, False),
    (-1, -1, True, True),
    (1, -1, True, False),
    (5, -5, False, True),
    (-6, 6, False, True),
    (-5, 6, False, True),
    (-2, -1, False, False),
    (1, 2, False, False),
    (5, 6, False, False),
    (-5, -5, True, True),
])
def test_pos_neg(a, b, negative, expected):
    assert pos_neg(a, b, negative) == expected
# このテストは、pos_neg 関数が正しく動作するかどうかを確認するためのものです。
# 各テストケースは、引数 a, b, negative と期待される結果 expected を持っています。
# pytest を使用して、これらのテストを実行することができます。