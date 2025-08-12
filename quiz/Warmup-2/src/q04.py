# "Code"の様な空でない文字列が与えられたら、"CCoCodCode"を返す処理
# 例：
# 　string_splosion("Code") → "CCoCodCode"
# 　string_splosion("abc") → "aababc"
# 　string_splosion("ab") → "aab"
# 
# @param bool str 文字列
# 
# @return 上記の条件で作られた文字列を返す
# 

def string_splosion(s: str) -> str:
    result = ""
    for i in range(1, len(s) + 1):
        result += s[:i]
    return result
