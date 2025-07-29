'''
int の配列が与えられたとき、配列のどこかに 2 の隣に 2 があればTrueを返す。

nums: 数字のリスト
return: 2 の隣に 2 がある場合は True、そうでなければ False
'''
def has22(nums):
    has2 = 0
    for num in nums:
        if has2 == 1 and num == 2:
            return True
        elif has2 == 1 and num != 2:
            has2 = 0
        if num == 2 and has2 == 0:
            has2 = 1
    return False
