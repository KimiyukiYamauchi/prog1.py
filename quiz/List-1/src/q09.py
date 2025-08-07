# 引数としてint型の配列が与えられたとき、その最初の2つの要素の合計を
# 返す関数。要素数が0の場合は0を返す
# 例：
# 　sum2([1, 2, 3]) → 3
# 　sum2([1, 1]) → 2
# 　sum2([1, 1, 1, 1]) → 2
# 
# @param int [] nums int型の配列
# 
# @return int 最初の2つの要素の合計

def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0] 
    elif len(nums) == 0:
        return 0

#numsが2つ以上(2も含む)だった場合の処理
#numsが1つだった場合の処理(これはそのまま要素を返すだけらしい)
#numsが０(そもそも要素がない)場合の処理
