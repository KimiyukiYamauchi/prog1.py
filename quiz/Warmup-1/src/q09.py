# 受け取った引数(文字列)の前に"not "を付加して返す。
# 但し、すでにnotから文字列が始まっている場合は
# 受け取った文字列をそのまま返す関数
# 例：
# 　not_string("candy") → "not candy"
# 　not_string("x") → "not x"
# 　not_string("not bad") → "not bad"
# 
# @param string $str
# 
# @return notから始まる文字列を返す
# 

def not_string(s):
    if s[:3] == "not":
        return s
    
    else:
        return "not " + s

# Example usage:
# print(not_string("candy"))  # Output: "not candy"
