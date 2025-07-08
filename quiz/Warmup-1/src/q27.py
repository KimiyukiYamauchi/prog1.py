# 2つの引数(整数)で、10以上20以下の範囲の大きいほうを返す。
# 2つの引数(整数)が、どちらも10以上20以下でない場合は0を返す
# 例：
# 　　max1020(11, 19) → 19
# 　　max1020(19, 11) → 19
# 　　max1020(11, 9) → 11
# 
# @param int $a 整数
# @param int $b 整数
# 
# @return 2つの引数(整数)で、10以上20以下の範囲の大きいほうを返す。
# 　　　　2つの引数(整数)が、どちらも10以上20以下でない場合は0を返す

def max1020(a, b):
    if a >= 10 and a <= 20 and b >= 10 and b <= 20:
        if a > b:
            return a
        else: 
            return b
    elif a >= 10 and a <= 20:
        return a
    elif b >= 10 and b <= 20:
        return b 
    else:
        return 0
