#'''
#6という数は本当に偉大な数である。
#2 つの int 値 a と b が与えられたとき、どちらかが 6 であればTrueを返す。
#あるいは、それらの和または差が 6 であればTrueを返す。
#
#a 整数
#b 整数
#
#return 上の条件に従って、TrueまたはFalseを返す
#'''
def love6(a, b):
    return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6
