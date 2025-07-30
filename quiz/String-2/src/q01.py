'''
文字列が与えられた場合、元の文字列の各文字が
2回繰り返される文字列を返す。

s: 入力文字列

return: 各文字が2回繰り返される文字列

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result
    
