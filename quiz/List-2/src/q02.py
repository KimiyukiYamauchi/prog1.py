'''
長さ 1 以上の int 配列が指定された場合、その配列内の最大値と最小値の差を返します。

nums: int[] - 整数のリスト
戻り値: int - 最大値と最小値の差
'''
def max_min_diff(nums):
    return max(nums) - min(nums)
    
