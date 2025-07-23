# 与えられた文字列の末尾の2文字が文字列中に現れる数を返す処理
# 例：
# 　last2("hixxhi") → 1
# 　last2("xaxxaxaxx") → 1
# 　last2("axxxaaxx") → 2
# 
# @param string str 文字列
# 
# @return 上記の条件での数を返す

def last2(str):
    s= str
   if len(s) < 2:
        return 0
    n = s[-2:]
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+2] == n:
            count += 1
        return count


#def last2(s):
#    if len(s) < 2:
#        return 0
#    n = s[-2:]
#    count = 0
#    for i in range(len(s) - 2):  # 後ろ2文字は除く範囲でループ
#        if s[i:i+2] == n:
#            count += 1
#    return count

