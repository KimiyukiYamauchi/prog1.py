# 引数で与えられた要素数3のint型の配列の要素の最初と最後の要素の
# 大きいほうの値で、他の要素を上書きした配列を返す
# 例：
# 　max_end3([1, 2, 3]) → [3, 3, 3]
# 　max_end3([11, 5, 9]) → [11, 11, 11]
# 　max_end3([2, 11, 3]) → [3, 3, 3]
# 
# @param int [] nums 要素数3のint型の配列
# 
# @return int []　上の処理を行った配列

def max_end3(nums):
    if nums[0] > nums[2]:
        return [nums[0]] * 3
    else:
        return [nums[2]] * 3
