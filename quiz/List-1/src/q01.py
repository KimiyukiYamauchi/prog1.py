# 引数として整数の配列を受け取り、要素の最初か、最後が6ならTrueを返す
# それ以外はFalseを返す
# 配列の要素数は1以上
# 例：
# 　first_last6([1, 2, 6]) → True
# 　first_last6([6, 1, 2, 3]) → True
# 　first_last6([13, 6, 1, 2, 3]) → False
# 
# @param 整数型の配列
# 
# @return True or False

def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False
