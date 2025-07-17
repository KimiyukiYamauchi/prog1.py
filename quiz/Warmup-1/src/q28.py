# 1つの引数(文字列)に文字'e'が1つまたは3つ含まれている場合はtrueを返す。
# それ以外ははfalseを返す
# 例：
# 　　string_e("Hello") → true
# 　　string_e("Heelle") → true
# 　　string_e("Heelele") → false
# 
# @param int $str 文字列
# 
# @return 1つの引数(文字列)に文字'e'が1つまたは3つ含まれている場合はtrueを返す。
# 　　　　それ以外ははfalseを返す
# 

def string_e(str):
    return str.count('e') == 1 or str.count('e') == 3
