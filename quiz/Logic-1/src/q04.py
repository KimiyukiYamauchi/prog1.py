'''
あなたは少しスピードを出しすぎていて、警察官に止められた。
0=違反切符なし、1=小さな違反切符、2=大きな違反切符。
速度が60以下であれば結果は0、61から80の間であれば結果は1、
81以上であれば結果は2である。
ただし、誕生日であれば速度を-5する

speed スピード
is_birthday 誕生日かどうか

@return 上記の条件に従って、0、1、2のどれかを返す

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

'''
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
#2つ目の判定のコードはelifでなくifを使う...らしい
#理由：🧠 なぜ elif ではなく if を使うべきか？
#elif は「前の条件が False のときだけ評価される」
#elif は英語の “else if” の略で、前の if（または elif）が偽だった場合にのみ評価されます
#つまり、一番上の条件が真なら、elif 以降はすべてスキップされます。
    
#↓ このコードは間違いですー
#if is_birthday == True:
#        return speed - 5
#    elif speed <= 60:
#        return 0
#    elif 61 <= speed <= 80:
#        return 1
#    elif speed >= 81:
#        return 2

#if is_birthday == True:
#これはそもそもTrueとかないらしい。is_birthdayになってるかどうか？みたいな
#return speed - 5 これだと「これから使うspeedを-5する」という処理にはできない
#(「speedから-5を引いた値を返すよ！」になる）
#elif 61 <= speed <= 80:
#前のelif speed <= 60を通っている時点で61以上ではあるのでここで判定しなくて良い









