'''
配列内の数字の和を返す。配列が空の場合は0を返す。
ただし、13は非常に不吉な数字なのでカウントされないし、
13の直後に来る数字もカウントされない。

nums: 数字のリスト
return: 数字の合計
'''
def sum13(nums):
    flag = False
    ret = 0
    for i in nums:
        if i == 13 or flag:
            if i == 13:
                flag = True
            else:
                flag = False
            continue
        else:
            ret += i
    return ret
