# 引数で与えられた文字列を２文字分左ローテートシフトした文字列を返す
# 先頭の２文字を文字列の末尾に移動する
# 引数で与えられた文字列は２文字以上
# 例：
# 　left2("Hello") → "lloHe"
# 　left2("java") → "vaja"
# 　left2("Hi") → "Hi"
# 
# @param array string str
# 
# @return string 上記の処理を行った文字列を返す

def left2(str):
    return str[2:] + str[:2]


