# パロアルトのリスは一日の大半を遊んで過ごす。
# 特に、気温が60度から90度の間であれば遊ぶ。夏でない限り、上限は 90 ではなく 
# 100 になる。int のtempと boolean の is_summer が与えられたとき、
# リスが遊んでいればTrueを、そうでなければFalseを返す。
# 
#  temp 気温
#  is_summer 夏かどうか
#  
#  @return リスが遊んでいればTrueを、そうでなければFalse
#
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
    if is_summer:
        if 60<=temp<=100:
            return True
    else:
        if 60<=temp<=90:
            return True
    return False
