'''
文字列 「hi」 が与えられた文字列のどこかに現れる回数を返す。

s: 文字列

return: 「hi」の出現回数

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''
def count_hi(s):
    a=0
    for i in range(len(s) - 1):
        if s[i:i+2] == "hi":    
            a += 1
    return a
