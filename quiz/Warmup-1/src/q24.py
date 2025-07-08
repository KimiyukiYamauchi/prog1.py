# 3つの引数(整数)の最大値を返す。
# 例：
# 　int_max(1, 2, 3) → 3
# 　int_max(1, 3, 2) → 3
# 　int_max(3, 2, 1) → 3
# 
# @param int a 整数
# @param int b 整数
# @param int c 整数
# 
# @return 3つの引数(整数)の最大値
# 

def int_max(a, b, c):
    if a<=b<c or b<=a<c:
        return c
    elif a<=c<b or c<=a<b:
        return b
    elif b<=c<a or c<=b<a:
        return a
