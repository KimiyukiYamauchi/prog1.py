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
    a= min(big, goal // 5)
    b= goal - (a * 5)
    if small >= b:
        return True
    else:
        return False
