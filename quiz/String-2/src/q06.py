'''
与えられた文字列が 「xyz 」を含んでおり、そのxyzの前にピリオド(.)がない場合にTrueを返す。
つまり、「xxyz」 はカウントされるが、「x.xyz」 はカウントされない。

s: 文字列

return: True または False

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
import re

def xyz_there(s):
    return bool(re.search(r'(?<!\.)xyz', s))

