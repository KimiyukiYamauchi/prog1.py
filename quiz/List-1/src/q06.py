# 引数で与えられた要素数3のint型の配列の要素を１要素分
# 左ローテートシフトした結果の配列を返す
# 例：
# 　rotate_left3([1, 2, 3]) → [2, 3, 1]
# 　rotate_left3([5, 11, 9]) → [11, 9, 5]
# 　rotate_left3([7, 0, 0]) → [0, 0, 7]
# 
# @param int [] nums 要素数3のint型の配列
# 
# @return int [] １要素分左ローテートシフトした配列
# 

def rotate_left3(nums):
    return [nums[1],nums[2],nums[0]]
