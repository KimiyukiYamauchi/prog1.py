# 引数(文字列)が"mix"で始まっていればtrueを返す
# 但し、mの位置の文字は任意の文字でOK
# 例："pix","9ix"など
# 　mix_start("mix snacks") → true
# 　mix_start("pix snacks") → true
# 　mix_start("piz snacks") → false
# 
# @param string str 文字列
# 
# @return 引数(文字列)が"mix"で始まっていればtrueを返す
# 　　　　但し、mの位置の文字は任意の文字でOK
# 

def mix_start(s):
    return len(s) >= 3 and s[1:3] == "ix"

