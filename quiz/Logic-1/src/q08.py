'''
数値 n が与えられたとき、n が 1 から 10 までの範囲にあれば真を返す。
ただし、outside_modeがTrueの場合は、数値が1以下または10以上の場合にTrueを返す。

n 整数
outside_mode TrueまたはFalse

return 上記の条件に従ってTrueまたはFalseを返す
'''
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10
