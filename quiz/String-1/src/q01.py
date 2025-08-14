# 引数として文字列nameを受け取り、"Hello [name]!"という形式の挨拶文を返す
# 例：
# 　hello_name("Bob") → "Hello Bob!"
# 　hello_name("Alice") → "Hello Alice!"
# 　hello_name("X") → "Hello X!"
# 
# @param string name 文字列(名前)
# 
# @return "Hello [name]!"という形式の挨拶文
# 
#/

def hello_name(name):
    return f"Hello {name}!"
