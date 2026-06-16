# 第1引数(文字列)から第2引数(整数)の文字位置の文字を削除した
# 文字列を返す関数
# 引数として空でない文字列(str)と整数(n)が与えられた場合、
# インデックス n にある文字が削除された新しい文字列を返します。
# n の値は、元の文字列の文字の有効なインデックスになります
# （つまり、n は 0 から len(str)-1 までの範囲に含まれます）。
# 例：
# 　missing_char("kitten", 1) → "ktten"
# 　missing_char("kitten", 0) → "itten"
# 　missing_char("kitten", 4) → "kittn"
# 
# @param string str 対象の文字列
# @param string n  削除位置(0からstrlen(str)-1の範囲)
# 
# @return 対象の文字列から削除位置の文字を削除した文字列を返す
# 

def missing_char(str, n):
    return str
