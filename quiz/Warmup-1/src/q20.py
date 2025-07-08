# 2つの引数(整数)のどちらか一方が13以上、19以下の範囲のときtrueを返す
# それ以外はfalseを返す関数
# 例：
# 　lone_teen(13, 99) → true
# 　lone_teen(21, 19) → true
# 　lone_teen(13, 13) → false
# 
# @param int $a 整数
# @param int $b 整数
# 
# @return 32つの引数(整数)のどちらか一方だけが13以上、19以下の範囲のときtrueを返す
# 　　　　それ以外はfalseを返す関数
# 

def lone_teen(a, b):
    a_teen = 13 <= a <= 19
    b_teen = 13 <= b <= 19
    return (a_teen and not b_teen) or (not a_teen and b_teen)
