'''
ゴールの長さのレンガの列を作りたい。小さいレンガ (1インチずつ) 
と大きいレンガ (5インチずつ) がある。
与えられたレンガから選んでゴールを作ることが可能ならTrueを返す。
これは見た目より少し難しく、ループなしで実行できる。

small: 小さいレンガの数
big: 大きいレンガの数
goal: ゴールの長さ

return: ゴールを作ることが可能ならTrue、そうでなければFalse

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
def make_bricks(small, big, goal):
    max_big_use = min(goal // 5, big)
    rest = goal - (max_big_use * 5)
    return rest <= small
