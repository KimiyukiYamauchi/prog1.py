# 与えられたint型の配列で、要素が9の数を返す関数
# 例：
# 　array_count9([1, 2, 9]) → 1
# 　array_count9([1, 9, 9]) → 2
# 　array_count9([1, 9, 9]) → 2
# 
# @param array nums int型の配列
# 
# @return 上記の条件での数を返す

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

