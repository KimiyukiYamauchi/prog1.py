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
    pairs_a = {a[i:i+2] for i in range(len(a) -1)}
    pairs_b = {b[i:i+2] for i in range(len(b) -1)}

    comman_pairs = pairs_a.intersection(pairs_b)

    return len(comman_pairs) >=3
return False
