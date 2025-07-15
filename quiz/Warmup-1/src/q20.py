# 2つの引数(整数)のどちらか一方が13以上、19以下の範囲のときtrueを返す
# それ以外はfalseを返す関数
# 例：
# 　lone_teen(13, 99) → true
# 　lone_teen(21, 19) → true
# 　lone_teen(13, 13) → false
# 
# @param int $a 整数
# @param int $b 整数
# 
# @return 32つの引数(整数)のどちらか一方だけが13以上、19以下の範囲のときtrueを返す
# 　　　　それ以外はfalseを返す関数
# 

def lone_teen(a, b):
    in_range = lambda x: 13 <= x <= 19
    return in_range(a) ^ in_range(b)

#lambda(ラムダ式 無名関数)は、defと似たような使い方
#文法 lambda 引数:戻り値

#"どちらか一方だけ"のときはXOR演算子(^)（キャロット）を使う

#lambdaでin_rangeに関数を代入し、defの戻り値(return)でキャロットを使って片方が範囲内の数字か確認する
