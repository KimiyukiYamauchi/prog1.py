# 引数で与えられた文字列の最初の２文字を返す。文字列が２文字に満たない場合は
# 与えられた文字列をそのまま返す
# 例：
# 　first_two("Hello") → "He"
# 　first_two("abcdefg") → "ab"
# 　first_two("ab") → "ab"
# 
# @param string str 文字列
# 
# @return string 上記の条件で作られた文字列を返す

def first_two(str):
    if len(str) <= 2:
        return str
    else:
        return str[:2]
