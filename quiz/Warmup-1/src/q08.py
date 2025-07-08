# 受け取った引数で以下の条件が成り立つならTrueを返す
# それ以外はFalseを返す
# 条件：
# 　第3引数の$negativeがFalseなら第1、第2引数のいずれかが正の数で、もう一方が負の数
# 　第3引数の$negativeがTrueなら第1、第2引数のどちらも負の数
# 例：
# 　pos_neg(1, -1, False) → True
# 　pos_neg(-1, 1, False) → True
# 　pos_neg(-4, -5, True) → True
# 
# @param int a 整数
# @param int b 整数
# @param bool negative 論理値(TrueまたはFalse)
# 
# @return 条件が成り立つならTrueを返す
#         それ以外はFalse
# 

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)
