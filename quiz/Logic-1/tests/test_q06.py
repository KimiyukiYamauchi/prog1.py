import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import alarm_clock

@pytest.mark.parametrize("day, vacation, expected", [
    (1, False, "7:00"),
    (5, False, "7:00"),
    (0, False, "10:00"),
    (6, False, "10:00"),
    (0, True, "off"),
    (6, True, "off"),
    (1, True, "10:00"),
    (3, True, "10:00"),
    (5, True, "10:00"),
])
def test_alarm_clock(day, vacation, expected):
    assert alarm_clock(day, vacation) == expected
