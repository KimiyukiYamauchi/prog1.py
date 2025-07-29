'''
配列内の数字の和を返す。配列が空の場合は0を返す。
ただし、13は非常に不吉な数字なのでカウントされないし、
13の直後に来る数字もカウントされない。

nums: 数字のリスト
return: 数字の合計
'''
def sum13(nums):
    total = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            continue # 13 が見つからなければ次に進む

        if i > 0 and nums[i-1] == 13:
            continue # 直前が13だった場合、次の数字もスキップ

        total += nums[i] # 13 とその直後でなければ加算
    return total
