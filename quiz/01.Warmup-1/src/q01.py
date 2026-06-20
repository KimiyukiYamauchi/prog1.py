# sleep_in: 寝坊してもよいかを判定する関数
# 引数の weekday は、平日であればTrue で、週末でのあればFalse が設定されます。
# 引数の vacation は、休暇中であればTrueで、 そうでなければFalse が設定されます。
# 平日ではないか、休暇中であれば寝坊してもOKです。
# 寝坊してもOKの場合はTrue を返します。
#  
#  weekday 平日であればTrue、土日はFalse
#  vacation休暇中はTrue、そうでなければFalse
#  
#  weekdayがFalseまたはvacationがTrueなら遅起きしてよい
#  
#  @return 寝坊してもよければTrue、そうでなければFalse
#  
#  
#  例：
#  　sleep_in(False, False) → True
#  　sleep_in(True, False) → False
#  　sleep_in(False,True) → True

def sleep_in(weekday, vacation):
    return False
