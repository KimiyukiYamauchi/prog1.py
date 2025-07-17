# 引数(文字列)のindexが1の位置から"del"があればそれを削除して返す
# なければ引数(文字列)をそのまま返す関数
# 例：
# 　del_del("adelbc") → "abc"
# 　del_del("adelHello") → "aHello"
# 　del_del("adedbc") → "adedbc"
# 
# @param string str 文字列
# 
# @return 引数(文字列)のindexが1の位置から"del"があればそれを削除して返す
# 　　　　なければ引数(文字列)をそのまま返す
# 
#/

def del_del(str):
    if str[1:4] == "del":
        return str[0] + str[4:]
    return str

#if文の解説。
#str[1:4]は、インデックス1からdelがあるとき〜のやつ。
#インデックス1からdelがあれば、delの"l"はインデックス4になるため、[1:4]になる
#str[0]
#↑ これがないと、インデックス1から0の文字(1文字目)を取得できない。
#delを削除した後の文字列を取得するには、まず、インデックス1から0を取得して、
#スライスでdelから後の文字列を取得して、両方を結合させる。
