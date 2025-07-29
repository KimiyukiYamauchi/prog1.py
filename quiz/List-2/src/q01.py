'''
与えられた配列に含まれる偶数の int の数を返す。

nums: int[] - 整数のリスト
戻り値: int - 偶数の数
'''

def count_evens(nums):
    count = 0 
    for i in nums:
        if i % 2 == 0: #2で割って偶数なら
            count += 1 #カウントを1増やす
    return count
