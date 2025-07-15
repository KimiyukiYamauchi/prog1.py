# 2つの引数(整数)ともに、30以上40以下、または40以上50以下にあるときtrueを返す。
# それ以外はfalseを返す
# 例：
# 　　in3050(30, 31) → true
# 　　in3050(30, 41) → false
# 　　in3050(40, 50) → true
# 
# @param int a 整数
# @param int b 整数
# 
# @return つの引数(整数)ともに、30以上40以下、または40以上50以下に
# 　　　　あるときtrueを返す。それ以外はfalseを返す

def in3050(a, b):
    if (30 <= a <= 40 and 30 <= b <= 40) or (40 <= a <= 50 and 40 <= b <= 50):
        return True
    return False
