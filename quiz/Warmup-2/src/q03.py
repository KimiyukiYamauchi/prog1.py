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
    return ''.join(str[i] for i in range(0, len(str), 2))
    
