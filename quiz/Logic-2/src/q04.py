'''
3 つの int 値 a b c が与えられたとき、それらの合計を返す。
ただし、いずれかの値がティーン(13..19を含む範囲)である場合、
その値は0としてカウントされる。
ただし、15と16はティーンとしてカウントされない。
別のヘルパー 「def fix_teen(n): 」を書いて、int型の値を受け取り、
その値をteenルールに固定して返す。
こうすることで、teenのコードを3回繰り返さずにすむ（つまり「分解」）。
このヘルパーをメインのno_teen_sum()の下に、同じインデント・レベルで定義する。

a: 整数値
b: 整数値
c: 整数値

return: 合計値

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in[13, 14, 17, 18, 19]:
        return 0
    return n
