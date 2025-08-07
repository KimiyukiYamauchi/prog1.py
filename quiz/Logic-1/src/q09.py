'''
非負の整数 「num 」が与えられたとき、numが10の倍数の2以内であれば真を返す。
例えばnumが38、39、40、41、42はTrueを37、43などはFalseを返す

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

num 非負の整数

return 上記条件に従って、TrueまたはFalseを返す

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
'''
def near_ten(num):
    numm = num % 10
    return numm <= 2 or numm >= 8 

#このコードでは、 10 で割った余りが 0, 1, 2 または 8, 9 であるかどうかを判定


