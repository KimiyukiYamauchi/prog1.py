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

def string_splosion(str):
    if len(str) == 2:
        return str[0] + str[:2]
    elif len(str) == 3:
        return str[0] + str[:2] + str[:3]
    elif len(str) == 4:
        return str[0] + str[:2] + str[:3] + str[:4]
    elif len(str) == 5:
        return str[0] + str[:2] + str[:3] + str[:4] + str[:5]
    elif len(str) == 6:
        return str[0] + str[:2] + str[:3] + str[:4] + str[:5] + str[:6]
    else:
        return str

