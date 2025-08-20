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
    half = len(str) // 2
    return str[:half]

#strを割る２して、それをhalfに代入する
#halfには文字列のうち、真ん中に値する文字？スライス？が入ってる
#strの最初からhalfの位置まで返す
