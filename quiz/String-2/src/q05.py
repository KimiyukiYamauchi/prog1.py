#'''
#2つの文字列が与えられたとき、大文字と小文字の違いを無視して、どちらかの文字列がもう一方の文字列の末尾に現れる場合に、
#Trueを返す。

#a: 文字列
#b: 文字列
#return: 文字列が末尾に現れる場合はTrue、そうでない場合はFalse

#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True
#'''
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)
