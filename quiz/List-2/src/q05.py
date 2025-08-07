'''
配列中の数字の合計を返します。
ただし、6 で始まり次の 7 まで続く数字のセクションは無視します
（すべての 6 の後には少なくとも 1 つの 7 が続きます）。
数字がない場合は0を返す。

nums: 数字のリスト
return: 数字の合計
'''
def sum67(nums):
    total = 0 
    ignore = False

    for n in nums:
        if n == 6:
            ignore = True
        elif ignore:
            if n == 7:
                ignore = False

        else:
            total += n
    return total
