# 引数(文字列)の末尾の文字を引数の文字列の前後に追加した文字列を返す関数
# 引数の文字列は1文字以上
# 例：
# 　back_around("cat") → "tcatt"
# 　back_around("Hello") → "oHelloo"
# 　back_around("a") → "aaa"
# 
# @param string str 対象の文字列
# 
# @return 引数(文字列)の末尾の文字を引数(文字列)の前後に追加した文字列を返す
#

def back_around(s):
    last_char = s[-1]
    return last_char + s + last_char
