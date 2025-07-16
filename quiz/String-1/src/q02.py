# 与えられた2つの文字列aとbを、abbaの順序で結合した結果を返す
# 例：
# 　make_abba("Hi", "Bye") → "HiByeByeHi"
# 　make_abba("Yo", "Alice") → "YoAliceAliceYo"
# 　make_abba("What", "Up") → "WhatUpUpWhat"
# 
# @param bool a 文字列
# @param bool b 文字列
# 
# @return 与えられた2つの文字列aとbを、abbaの順序で結合した文字列

def make_abba(a, b):
    return ""+a+b+b+a
