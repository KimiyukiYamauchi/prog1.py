# この関数では、2つのint型の配列を受け取り、2つの配列の最初または最後の要素が
# 等しい場合Trueを返す。
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
    if not a and b:
        return False

    c = a[0]
    d = a[-1]
    e = b[0]
    f = b[-1]

    if c == e or d == f:
        return True
    return False
