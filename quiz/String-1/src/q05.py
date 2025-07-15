# 引数で与えられた文字列の後ろ２文字を３回繰り返した文字列を返す
# 与えられる文字列は２文字以上
# 例：
# 　extra_end("Hello") → "lololo"
# 　extra_end("ab") → "ababab"
# 　extra_end("Hi") → "HiHiHi"
# 
# @param string str 文字列
# 
# @return string 上記の条件で作られた文字列を返す

def extra_end(str):
    return str[-2:] * 3
