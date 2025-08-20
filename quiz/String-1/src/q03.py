# この関数は、指定されたタグと単語を受け取り、
# それらをHTMLタグで囲んだ文字列を返します。
# 例：
# 　make_tags("i", "Yay") → "<i>Yay</i>"
# 　make_tags("i", "Hello") → "<i>Hello</i>"
# 　make_tags("cite", "Yay") → "<cite>Yay</cite>"
# 
# @param string tag タグ
# @param string word 単語
# 
# @return string HTMLタグで囲んだ文字列

def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
      
#    return "<" + tag + ">" + word + "</" + tag + ">" 

#f文字列を使うと、波括弧{}で囲まれているところは引数を入れられる。それ以外はstrになる
