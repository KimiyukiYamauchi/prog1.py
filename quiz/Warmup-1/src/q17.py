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
    if 0 >= temp1 and 100 < temp2 or 100 < temp1 and 0 >= temp2:
        return True
    else:
        return False
