# 2つの引数(整数)の一方が0より小さく、もう一方が100より大きいときtrueを返す
# それ以外はfalseを返す関数
# 例：
# 　icy_hot(120, -1) → true
# 　icy_hot(-1, 120) → true
# 　icy_hot(2, 120) → false
# 
# @param int temp1 整数
# @param int temp2 整数
# 
# @return 2つの引数(整数)の一方が0より小さく、もう一方が100より大きいときtrue
# 　　　　を返す。それ以外はfalseを返す
# 

def icy_hot(temp1, temp2):
    return (temp1 < 0 and temp2 > 100) or (temp2 < 0 and temp1 > 100)
