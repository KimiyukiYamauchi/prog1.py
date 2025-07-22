# 引数(文字列)の後ろの3文字を大文字に変換して返す。
# 引数(文字列)が3文字に満たない場合はすべてを大文字に変換して返す
# 例：
# 　　end_up("Hello") → "HeLLO"
# 　　end_up("hi there") → "hi thERE"
# 　　end_up("hi") → "HI"
# 
# @param string str 文字列
# 
# @return 1つの引数(文字列)の後ろの3文字を大文字に変換して返す。
# 　　　　3文字に満たない場合はすべてを大文字に変換して返す

def end_up(str):
    if len(str) <= 3:
        return str.upper()
    else:
        return str[:-3] + str[-3:].upper()

#まず、len関数でstrが3文字以下か確認し、
#3文字以下であればstrをupperメソッドで大文字に変換
#次に、strが3文字以上の場合の処理
#スライスでstrの最初の位置から、後ろから3番目までを指定したものと、
#strの後ろから3番目までをupperで大文字変換したものを結合する
