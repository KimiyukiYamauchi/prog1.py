# 引数(文字列)の先頭2文字を引数(文字列)の前後に付加してそれを返す関数
# 例：
# 　front22("kitten") → "kikittenki"
# 　front22("Ha") → "HaHaHa"
# 　front22("abc") → "ababcab"
# 
# @param string str 文字列
# 
# @return 引数(文字列)の先頭2文字を引数(文字列)の前後に付加してそれを返す
# 

def front22(str):
    front = str[:2]
    return front + str + front
    # 先頭2文字を取得（文字列が2文字未満でも対応）
    front = str[:2]
    # 先頭2文字を前後に付加して返す
    return front + str + front


