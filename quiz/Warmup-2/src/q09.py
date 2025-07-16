# 与えられた2つの文字列(string型)で共通する2文字の文字列の個数を返す関数
# 共通する文字列は文字位置も一致しなければいけない
# 例えば"xxcaazz"と"xxbaaz"が与えられた場合、"xx"(文字位置0)、"aa"(文字位置3)、
# "az"(文字位置4)が共通なので、3を返す
# 例：
# 　string_match("xxcaazz", "xxbaaz") → 3 ("xx", "aa", "az")
# 　string_match("abc", "abc") → 2 ("ab", "bc")
# 　string_match("abc", "axc") → 0
# 
# @param array string a string b
# 
# @return 上記の条件が成り立つ個数を返す

def string_match(a, b):
    count = 0
    
    # 短い方の文字列の長さ - 1 までループ(2文字ペアを見るため)
    length = min(len(a), len(b)) - 1

    for i in range(length):
        
        # 同じ位置の2文字が一致しているかチェック
        if a[i:i+2] == b[i:i+2]:
            count += 1

    return count
