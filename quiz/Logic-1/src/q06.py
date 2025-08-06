#'''
#0=日、1=月、2=火、...6=土としてエンコードされた曜日と、
#休暇中かどうかを示すブール値が与えられたら、
#目覚まし時計がいつ鳴るかを示す "7:00 "という形式の文字列を返す。
#平日は "7:00"、週末は "10:00 "である。
#休暇中の場合、平日は "10:00"、週末は "off"である。
#
#day 曜日(0=日、1=月、2=火、...6=土)
#vacation 休暇中かどうか
#
#return 上記の条件に従って、"7:00 "、"10:00"または"off"のいずれかを返す

#alarm_clock(1, False) → '7:00'
#alarm_clock(5, False) → '7:00'
#alarm_clock(0, False) → '10:00'
#'''
def alarm_clock(day, vacation):
    is_weekend = day == 0 or day == 6
    if vacation:
        if is_weekend:
            return "off"
        else:
            return "10:00"
    else:
        if is_weekend:
            return "10:00"
        else:
            return "7:00"
