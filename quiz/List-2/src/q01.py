'''
与えられた配列に含まれる偶数の int の数を返す。

nums: int[] - 整数のリスト
戻り値: int - 偶数の数
'''

def count_evens(nums):
    return sum(1 for n in nums if n % 2 == 0)
