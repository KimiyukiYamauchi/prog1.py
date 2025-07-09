# 2つの引数(整数)のうち10に近いほうを返す、2つの引数(整数)と10の距離が等しい場合は0を返す。
# 例：
# 　　close10(8, 13) → 8
# 　　close10(13, 8) → 8
# 　　close10(13, 7) → 0
# 
# @param int a 整数
# @param int b 整数
# 
# @return 2つの引数(整数)のうち10に近いほうを返す、2つの引数(整数)と
# 　　　　10の距離が等しい場合は0を返す。
# 

def close10(a, b):
    a_close = abs(a - 10)
    b_close = abs(b - 10)
    if a_close < b_close:
        return a
    elif b_close < a_close:
        return b
    else:
        return 0
