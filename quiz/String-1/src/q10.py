# 与えられた2つの文字列aとbの先頭1文字を除いた残りの部分を連結して
# その結果を返します。
# 例：
# 　non_start("Hello", "There") → "ellohere"
# 　non_start("java", "code") → "avaode"
# 　non_start("shotl", "java") → "hotlava"
# 
# @param string a 文字列
# @param string b 文字列
# 
# @return string 上記の処理を行った文字列を返す

def non_start(a, b):
    return a[1:] + b[1:]

