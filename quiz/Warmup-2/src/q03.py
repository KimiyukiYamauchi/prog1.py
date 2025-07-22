# 引数の文字列から奇数番目の文字で作った文字列を返す
# 例：
# 　string_bits("Hello") → "Hlo"
# 　string_bits("Hi") → "H"
# 　string_bits("Heeololeo") → "Hello"
# 
# @param bool str 文字列
# 
# @return 上記の条件で作られた文字列を返す
# 

def string_bits(str):
    return str[::2] 

#奇数番目って書いてるけど1,3,5..ではないらしい
#例では偶数番目0,2,4...になってるからそっちらしい
