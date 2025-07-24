# "Code"の様な空でない文字列が与えられたら、"CCoCodCode"を返す処理
# 例：
# 　string_splosion("Code") → "CCoCodCode"
# 　string_splosion("abc") → "aababc"
# 　string_splosion("ab") → "aab"
# 
# @param bool str 文字列
# 
# @return 上記の条件で作られた文字列を返す
# 

def string_splosion(str):
     result = ""
     for i in range(1, len(str) + 1):
         result += str[:i]
     return result

#len(str) + 1
#strのrと次の文字の間のインデックスまで
#result = result + str[:i]

#1回目は1文字まで、2回目は2文字目まで、3回目は3文字目まで、みたいな感じで
#文字を取得してそれを結合させる

