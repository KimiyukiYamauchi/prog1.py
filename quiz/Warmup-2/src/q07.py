# 与えられたint型の配列の4番目までの要素に9があればtrueを返す
# 但し、配列の要素数は4に満たない場合がある
# 例：
# 　array_front9([1, 2, 9, 3, 4]) → true
# 　array_front9([1, 2, 3, 4, 9]) → false
# 　array_front9([1, 2, 3, 4, 5]) → false
# 
# @param array nums int型の配列
# 
# @return 上記の条件での数を返す
# 

def array_front9(nums):
    return 9 in nums[:4]

#    str_nums = str(nums)
#    if str_nums.count("9",0,-4):
#        return True
#    elif len(str_nums) <= 4 and str_nums.count("9",0):
#        return True 
#    else:
#        return False

#numsという引数の4インデックスまでに"9"があるかin演算子で確認
