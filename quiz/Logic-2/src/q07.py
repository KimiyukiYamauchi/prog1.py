'''
ゴール・キロのチョコレートのパッケージを作りたい。
小さい棒（1本1キロ）と大きい棒（1本5キロ）がある。
小さい棒の前に必ず大きい棒を使うと仮定して、使用する小さい棒の数を返す。
できなければ -1 を返せ。

small: 小さい棒の数
big: 大きい棒の数
goal: ゴール・キロのチョコレート

return: 使用する小さい棒の数、または -1

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''
def make_chocolate(small, big, goal):
    max_big = min(goal // 5, big)
    remaining = goal - max_big * 5
    return remaining if remaining <= small else -1
