# 2つの引数(0以上の整数)の1の位の数値が等しい場合はtrueを返す。
# それ以外はfalseを返す
# 例：
# 　　last_digit(7, 17) → true
# 　　last_digit(6, 17) → false
# 　　last_digit(3, 113) → true
# 
# @param int a 整数
# @param int b 整数
# 
# @return 2つの引数(0以上の整数)の1の位の数値が等しい場合はtrueを返す。
# 　　　　それ以外はfalseを返す
# 

def last_digit(a, b):
    if a%10 == b%10:
        return True
    return False
