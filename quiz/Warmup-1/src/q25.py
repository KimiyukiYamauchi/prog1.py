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
    if a <= 10 and b <= 10:
        if 10 - a > 10 - b:
            return b
        elif 10 - a < 10 - b:
            return a
        elif 10 - a == 10 - b:
            return 0
    elif a <= 10 and b >= 10:
        if 10 - a > b - 10:
            return b
        elif 10 - a < b - 10:
            return a
        elif 10 - a == b - 10:
            return 0
    elif a >= 10 and b <= 10:
        if a - 10 > 10 - b:
            return b
        elif a - 10 < 10 - b:
            return a
        elif 1 - 10 == 10 - b:
            return 0
    elif a >= 10 and b >= 10:
        if a - 10 > b - 10:
            return b
        elif a - 10 < b - 10:
            return a
        elif a - 10 == b - 10:
            return 0
    return 0
