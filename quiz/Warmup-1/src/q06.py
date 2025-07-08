# 2つの引数(整数)を受け取り以下の条件が成り立つならTrueを返す
# それ以外はFalseを返す
# 条件：
# 　2つの引き数の少なくともどちらかが10
# 　2つの引き数の合計が10
# 例：
# 　makes10(9, 10) → True
# 　makes10(9, 9) → False
# 　makes10(1, 9) → True
# 
# @param int a 整数
# @param int b 整数
# 
# @return 条件が成り立つならTrueを返す
#         それ以外はFalse
# 
def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif (a+b) == 10:
        return True
    else:
        return False
