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
    return str[:2] + str + str[:2] 
