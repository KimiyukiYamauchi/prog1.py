# 与えられた偶数長の文字列の前半部分の文字列を返す処理
# 例：
# 　first_half("WooHoo") → "Woo"
# 　first_half("HelloThere") → "Hello"
# 　first_half("abcdef") → "abc"
# 
# @param string str 文字列
# 
# @return string　上記の処理を行った文字列

def first_half(str):
    return str[:len(str)//2]
