# 文字列と非負の整数を受け取り、文字列を非負の整数回繰り返した文字列を返す
# 例：
# 　string_timess("Hi", 2) → "HiHi"
# 　string_timess("Hi", 3) → "HiHiHi"
# 　string_timess("Hi", 1) → "Hi"
# 
# @param string str 繰り返す文字列
# @param int n 繰り返し回数
# 
# @return 文字列と非負の整数を受け取り、文字列を非負の整数回繰り返した文字列
# 

def string_times(str, n):
    return str * n 

#strにnかけるだけ
