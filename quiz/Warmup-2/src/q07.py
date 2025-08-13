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
    end = min(4,len(nums))
    for i in range(end):
        if nums[i] == 9:
            return True
    return False
