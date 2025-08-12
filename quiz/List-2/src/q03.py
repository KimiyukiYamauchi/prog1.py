'''
int の配列の「中央揃え」の平均を返します。
これは、配列中の最大値と最小値を無視した場合の平均とします。
最小の値が複数ある場合はそのうちの1つを無視し、 最大の値も同様に無視します。
int 除算を使用して、最終的な平均を求めます。配列の長さは3以上と仮定してよい。

nums: int[] - 整数のリスト
戻り値: int - 中央揃えの平均
'''
def centered_average(nums):
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1]  
    total = sum(trimmed)
    average = total // len(trimmed)  
    return average

