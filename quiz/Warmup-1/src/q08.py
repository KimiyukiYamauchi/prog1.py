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
    if (negative==False and ((a<=-1 and b>=1) or (a>=1 and b<=-1))) or (negative==True and a<=-1 and b<=-1):
        return True
    else:
        return False
