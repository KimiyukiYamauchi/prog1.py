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
    if len(str) >= 1 and str[0] == "o":
        result += str[0]
    if len(str) >= 2 and str[1] == "z":
        result +=str[1]
    return result    

