# 2つの引数(文字列と整数)を受け取り、文字列から整数の倍数番目の文字のみの
# 文字列を返す。整数として3を受け取った場合、文字列の0,3,6,9...番目
# の文字を結合した文字列を返す。引数の文字列は空文字ではない
# 例：
# 　　every_nth("Miracle", 2) → "Mrce"
# 　　every_nth("abcdefg", 2) → "aceg"
# 　　every_nth("abcdefg", 3) → "adg"
# 
# @param string str 文字列
# @param string n 整数
# 
# @return 2つの引数(文字列と整数)を受け取り、文字列から整数の倍数番目の文字のみの
# 　　　　文字列を返す。整数として3を受け取った場合、文字列の0,3,6,9...番目
# 　　　　の文字を結合した文字列を返す。

def every_nth(str, n):
    result = str[::n]
    return result

