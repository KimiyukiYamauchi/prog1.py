'''
配列中の数字の合計を返します。
ただし、6 で始まり次の 7 まで続く数字のセクションは無視します
（すべての 6 の後には少なくとも 1 つの 7 が続きます）。
数字がない場合は0を返す。

nums: 数字のリスト
return: 数字の合計
'''
def sum67(nums):
    sum = 0
    flag = False
    for i in nums:
        if flag:
            if i == 7:
                flag = False
        elif i == 6:
            flag = True
        else:
            sum += i
    return sum
