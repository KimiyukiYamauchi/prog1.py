'''
配列内の数字の和を返す。配列が空の場合は0を返す。
ただし、13は非常に不吉な数字なのでカウントされないし、
13の直後に来る数字もカウントされない。

nums: 数字のリスト
return: 数字の合計
'''
def sum13(nums):
    total = 0
    i = 0
    while i <len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total
