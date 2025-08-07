'''
int の配列が与えられたとき、配列のどこかに 2 の隣に 2 があればTrueを返す。

nums: 数字のリスト
return: 2 の隣に 2 がある場合は True、そうでなければ False
'''
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

