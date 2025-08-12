# それ以外はFalseを返す
# ２つの配列は1以上の要素を持つ
# 例：
# 　common_end([1, 2, 3], [7, 3]) → True
# 　common_end([1, 2, 3], [7, 3, 2]) → False
# 　common_end([1, 2, 3], [1, 3]) → True
# 
# @param int [] a int型の配列
# @param int [] b int型の配列
# 
# @return bool True or False

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

