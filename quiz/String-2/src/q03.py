#'''
#文字列 「cat 」と 「dog 」が、与えられた文字列の中で同じ回数出現したらTrueを返す。

#s: 文字列

#return: True または False

#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True
#'''
def cat_dog(s):
    return s.count('cat') == s.count('dog')
