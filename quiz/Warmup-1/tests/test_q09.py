import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import not_string

@pytest.mark.parametrize("s, expected", [
    ("candy", "not candy"),
    ("x", "not x"),
    ("not bad", "not bad"),
    ("bad", "not bad"),
    ("not", "not"),
    ("is not", "not is not"),
    ("no", "not no"),
])
def test_not_string(s, expected):
    assert not_string(s) == expected
# このテストは、not_string 関数が正しく動作するかどうかを確認するためのものです。
# 各テストケースは、引数 s と期待される結果 expected を持っています。
# pytest を使用して、これらのテストを実行することができます。