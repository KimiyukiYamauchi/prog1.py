'''
int の配列が与えられたとき、配列のどこかに 2 の隣に 2 があればTrueを返す。

nums: 数字のリスト
return: 2 の隣に 2 がある場合は True、そうでなければ False
'''
def has22(nums):
    for i in range(len(nums) - 1):  # 0番目から順に最後の1つ前まで 
        if nums[i] == 2 and nums[i + 1] == 2:  #現在と次の要素が2の場合
            return True

    return False
