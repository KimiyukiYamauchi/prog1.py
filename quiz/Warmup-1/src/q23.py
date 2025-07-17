# 引数として、文字列が与えられた場合、最初の2文字から成る文字列を返します（存在する場合）。
# ただし、最初の文字が 'o' の場合のみ含め、2番目の文字が 'z' の場合のみ含めます。
# したがって、"ozymandias" は "oz" を返します。
# 
# 例：start_oz("ozymandias") → "oz"
# 　　start_oz("bzoo") → "z"
# 　　start_oz("oxx") → "o"
# 
# @param string str 文字列
# 
# @return 上のルールにしたがって文字列を返す
# 

def start_oz(str):
    result = ""
    if len(str) >= 1 and str[0] == 'o':
        result += 'o'
    if len(str) >= 2 and str[1] == 'z':
        result += 'z'
    return result

#resultとは　文字を代入し、結果として表示するための引数
#
#最初のif文
#strが1文字以上あるか確認&文字列がoから始まるかどうか
#上記のif文に該当するなら、resultにoを代入
#2つ目のif文
#strが2文字以上あるか確認&文字列の2番目(インデックス1:2)がzかどうか
#上記のif文に該当するなら、resultにzを代入
#最後に、代入された文字を返すresultを設定。



#if文を複数使用するときは、そのif文全部が実行される
#例えば、今回の問題だと"o","z","oz"のどれかかどうか確認される
#oのチェック→ zのチェック→ ozのチェック

