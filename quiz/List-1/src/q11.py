# 引数で与えられたint型配列の最初と最後の要素からなる
# 配列を返す関数
# 与えられる配列の要素数は1文字以上
# 例：
# 　make_ends([1, 2, 3]) → [1, 3]
# 　make_ends([1, 2, 3, 4]) → [1, 4]
# 　make_ends([7, 4, 6, 2]) → [7, 2]
# 
# @param int [] $nums int型配列
# 
# @return int [] 上記の処理を行った配列を返す

def make_ends(nums):
    a = nums[0]
    b = nums[-1]
    return [a,b]  

#要素をインデックスで指定してaとbに代入する。
