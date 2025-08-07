'''
この問題では、int値の右端の桁が5以上の場合、次の10の倍数に丸めるので、15は20に丸められる。
また、右端の桁が5未満の場合は10の倍数に切り捨てる。
3つのint、a b cが与えられたら、それらの丸めた値の和を返す。
コードの繰り返しを避けるため、別のヘルパー 「def round10(num): 」を書き、それを3回呼び出す。
このヘルパーは、完全に round_sum() の下に、同じインデント・レベルで書く。

a: 整数
b: 整数
c: 整数

return: 合計値

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
'''
def round_sum(a, b, c):
    def round10(num):
        if num % 10 >= 5:
            return (num // 10) * 10 + 10
        else:
            return (num // 10) * 10
    return round10(a) + round10(b) + round10(c)
