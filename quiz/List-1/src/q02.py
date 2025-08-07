# 引数として整数の配列を受け取り、配列の要素数が1以上でかつ、
# 要素の最初と最後が等しいならTrueを返す
# それ以外はFalseを返す
# 例：
# 　same_first_last([1, 2, 3]) → False
# 　same_first_last([1, 2, 3, 1]) → True
# 　same_first_last([1, 2, 1]) → True
# 
# @param 整数型の配列
# 
# @return True or False

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1] 

