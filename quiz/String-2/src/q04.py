'''
文字列 「code 」が与えられた文字列のどこかに現れる回数を返す。
ただし、『d』にはどんな文字でも使えるので、「cope 」や 「cooe 」もカウントされる。

s: 文字列
return: 現れる回数

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(s):
    count= 0
    for i in range(len(s) - 3):
        if s[i:i+2] == 'co' and s[i+3] == 'e':
            count += 1
    return count


