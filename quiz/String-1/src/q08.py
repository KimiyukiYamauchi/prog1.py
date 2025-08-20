# 与えられた文字列の先頭と末尾の文字を除いた文字列を返す
# 与えれれる文字列は２文字以上
# 例：
# 　without_end("Hello") → "ell"
# 　without_end("java") → "av"
# 　without_end("coding") → "odin"
# 
# @param string str 文字列
# 
# @return string 上記の条件で作られた文字列

def without_end(str):
    return str[1:-1] 
