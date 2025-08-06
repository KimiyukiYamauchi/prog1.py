'''
3 つの int 値 a b c が与えられたとき、それらの合計を返す。
ただし、値の1つが別の値と同じ場合は、合計にカウントされません。

a: 整数値
b: 整数値
c: 整数値

return: 合計値

one_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''
from collections import Counter

def lone_sum(a, b, c):
    counts = Counter([a,b,c])
    return sum(num for num, cnt in counts.items() if cnt == 1)


