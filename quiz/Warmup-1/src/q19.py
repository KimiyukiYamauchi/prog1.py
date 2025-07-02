# 3つの引数(整数)の少なくとも1つが13以上、19以下の範囲のときtrueを返す
# それ以外はfalseを返す関数
# 例：
# 　has_teen(13, 20, 10) → true
# 　has_teen(20, 19, 10) → true
# 　has_teen(20, 10, 13) → true
# 
# @param int a 整数
# @param int b 整数
# @param int c 整数
# 
# @return 3つの引数(整数)の少なくとも1つが13以上、19以下の範囲のときtrueを返す
# 　　　　それ以外はfalseを返す関数
# 

def has_teen(a, b, c):
    if a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19:   
        return True
    else:
        return False
