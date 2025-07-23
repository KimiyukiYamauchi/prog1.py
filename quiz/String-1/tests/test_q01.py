import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import hello_name

@pytest.mark.parametrize("name, expected", [
    ("Bob", "Hello Bob!"),
    ("Alice", "Hello Alice!"),
    ("X", "Hello X!"),
    ("Dolly", "Hello Dolly!"),
    ("Alpha", "Hello Alpha!"),
    ("Omega", "Hello Omega!"),
    ("Goodbye", "Hello Goodbye!"),
    ("ho ho ho", "Hello ho ho ho!"),
    ("xyz!", "Hello xyz!!"),
    ("Hello", "Hello Hello!"),
])
def test_hello_name(name, expected):
    assert hello_name(name) == expected
