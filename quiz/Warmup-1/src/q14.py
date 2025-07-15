# 引数(整数)が3または5の倍数ならtrue、それ以外はfalseを返す関数
# 例：
# 　or35(3) → true
# 　or35(10) → true
# 　or35(8) → false
# 
# @param int n 整数
# 
# @return 引数(整数)が3または5の倍数ならtrue、それ以外はfalseを返す
# 

def or35(n):
    if n % 3 ==0 or n % 5 ==0:
        return True
    else:
        return False
