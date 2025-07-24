'''
文字列 「code 」が与えられた文字列のどこかに現れる回数を返す。
ただし、『d』にはどんな文字でも使えるので、「cope 」や 「cooe 」もカウントされる。

s: 文字列
return: 現れる回数

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
import re

def count_code(s):
    s = s.lower()
    pattern = r'co.e'
    return len(re.findall(pattern, s))
