# この関数では、４文字のout文字列を2つの文字列に分割して、
# 最初の2つの文字列と最後の2つの文字列を取得します。
# そして、wordを最初の2つの文字列の後に、最後の2つの文字列の前に追加することで、
# 新しい文字列を生成します。
# 例：
# 　make_out_word("<<>>", "Yay") → "<<Yay>>"
# 　make_out_word("<<>>", "WooHoo") → "<<WooHoo>>"
# 　make_out_word("[[]]", "word") → "[[word]]"
# 
# @param string out 囲む方の４文字の文字列
# @param string word 囲まれる方の文字列
# 
# @return string 上記の条件で生成した文字列

def make_out_word(out, word):
    return out[:2] + word + out[2:]
