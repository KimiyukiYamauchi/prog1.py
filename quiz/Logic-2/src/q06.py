'''
a b cの3つのintが与えられたとき、bまたはcの一方が 「近い」(aとの差が最大でも1)、
他方が 「遠い」(他の両方の値との差が2以上)ならTrueを返す。

a: 整数
b: 整数
c: 整数

return: 真偽値(True/False)

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''
def close_far(a, b, c):
    cond1 = abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2
    cond2 = abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2
    return cond1 or cond2

