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

    dist_a = abs(a - 10)
    dist_b = abs(b - 10)

    if dist_a < dist_b:

        return a

    elif dist_b < dist_a:

        return b

    else:

        return 0
