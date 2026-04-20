'''
与えられた配列に含まれる偶数の int の数を返す。

nums: int[] - 整数のリスト
戻り値: int - 偶数の数
'''

def count_evens(nums):
    count = 0
    for i in nums:
        if 1 % 2 == 0:
            count += 1
    return count        
