# 文字列と非負の整数を受け取り、文字列の最初3文字を非負の整数回繰り返した文字列を返す
# 但し、文字列は3文字より少ないことがある
# 例：
# 　front_times("Chocolate", 2) → "ChoCho"
# 　front_times("Chocolate", 3) → "ChoChoCho"
# 　front_times("Abc", 3) → "AbcAbcAbc"
# 
# @param bool str 先頭3文字を繰り返す
# @param bool n 繰り返し回数
# 
# @return 文字列の最初3文字を非負の整数回繰り返した文字列
# 

def front_times(str, n):
    if len(str) >= 3:
        return str[:3] * n
    else:
        return str[::] * n

#最初のif文
#lenでstrが3文字以上確認。3文字以上であれば、最初の位置から3文字スライスしてn回かける
#else
#それ以外。つまりstrが3文字以下のとき、
#スライスで最初から最後までを指定([::])→ ある文字数分かける
