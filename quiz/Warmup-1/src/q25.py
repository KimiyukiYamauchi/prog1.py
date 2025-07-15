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
    c = abs(a - 10)
    d = abs(b - 10)
    if c < d:
        return a
    if d < c:
        return b
    else:
        return 0
