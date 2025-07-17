'''
2つのint、aとbが与えられたら、それらの和を返す。
ただし、10～19の範囲の和は禁止されているので、
その場合は20を返せばよい。

a 整数
b 整数

@return 上記の条件で、aとbの和を返す
'''
def sorta_sum(a, b):
    total = a + b
    if total >= 10 and total <= 19:
        return 20
    else:
        return total
