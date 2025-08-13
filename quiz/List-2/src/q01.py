'''
与えられた配列に含まれる偶数の int の数を返す。

nums: int[] - 整数のリスト
戻り値: int - 偶数の数
'''

def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)
 
