# 引数(文字列)の先頭文字と末尾の文字を入れ替えた
# 文字列を返す関数
# 例：
# 　front_back("code") → "eodc"
# 　front_back("a") → "a"
# 　front_back("ab") → "ba"
# 
# @param string s 対象の文字列
# 
# @return 対象の先頭文字と末尾の文字を入れ替えた文字列を返す
# 
def front_back(s):
    if len(s) <= 1:
        return s
    elif len(s) >= 1:
        string = s[1:-1:]
        return s[-1] + string + s[:1]

#まず、文字列が1以上あるか確認。なかったらそのまま出力
#1文字以上あれば、stringに文字列の最初の文字と最後の文字を除いた文字列を入れておく
#stringとスライスで取得した文字列の最初の文字と最後の文字を結合する
