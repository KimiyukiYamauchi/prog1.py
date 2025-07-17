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
    int_a = abs(10 - a)
    int_b = abs(10 - b) 

    if int_a < int_b:
        return a
    elif int_b < int_a:
        return b
    elif int_a == int_b:
        return 0

#abs関数とは：引数の絶対値を返す関数(絶対値は、-+関係ない数字の距離)
#absで得られた絶対値をint_a,int_bに代入する
#
#最初のif文は、int_aがint_bより小さいかどうか確認→ int_aのほうが小さければ、aを返す
#次のif文は、int_bがint_aより小さいかどうか確認→ int_bのほうが小さければ、bを返す
#int_aとint_bの値が同じであれば、0を返す
