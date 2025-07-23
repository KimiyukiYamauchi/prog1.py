# 要素数が3のint型の配列を引数で受け取り、その要素の合計を
# 返す関数
# 例：
# 　sum3([1, 2, 3]) → 6
# 　sum3([5, 11, 2]) → 18
# 　sum3([7, 0, 0]) → 7
# 
# @param int [] nums int型の配列
# 
# @return 要素の合計値

def sum3(nums):
    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
