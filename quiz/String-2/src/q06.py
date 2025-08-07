'''
与えられた文字列が 「xyz 」を含んでおり、そのxyzの前にピリオド(.)がない場合にTrueを返す。
つまり、「xxyz」 はカウントされるが、「x.xyz」 はカウントされない。

s: 文字列

return: True または False

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
def xyz_there(s):
   for i in range(len(s) - 2):
      if s[i:i+3] == "xyz":
          if i == 0 or s[i-1] != '.':
              return True
   return False

