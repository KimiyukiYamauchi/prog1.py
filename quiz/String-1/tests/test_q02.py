import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import make_abba

@pytest.mark.parametrize("a, b, expected", [
    ("Hi", "Bye", "HiByeByeHi"),
    ("Yo", "Alice", "YoAliceAliceYo"),
    ("What", "Up", "WhatUpUpWhat"),
    ("aaa", "bbb", "aaabbbbbbaaa"),
    ("x", "y", "xyyx"),
    ("x", "", "xx"),
    ("", "y", "yy"),
    ("Bo", "Ya", "BoYaYaBo"),
    ("Ya", "Ya", "YaYaYaYa"),
])
def test_make_abba(a, b, expected):
    assert make_abba(a, b) == expected
