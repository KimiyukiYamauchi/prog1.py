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
    if a<b and 10<=b<=20:
        return b
    elif a>b and 10<=a<=20:
        return a
    elif a==b and 10<=a<=20:
        return a
    elif (a<10 or 20<a) and (b<10 or 20<b):
        return 0
    elif a<b and 10<=a<=20 and (b<10 or 20<b):
        return a
    elif a>b and 10<=b<=20 and (a<10 or 20<a):
        return b
