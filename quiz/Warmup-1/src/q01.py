# sleep_in: 寝坊してもよいかを判定する関数
#  引数の weekday は、平日であればTrue で、引数の vacation は、
#  休暇中であればTrue です。平日ではないか、休暇中であれば寝坊します。
#  寝坊する場合はTrue を返します。
#  
#  weekday 平日であればTrue、土日はFalse
#  vacation 祝日はTrue、そうでなければFalse
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

if sleep_in(False,False):
    return True

if sleep_in(True,False):
    return False

if sleep_in(False,True):
    return True

if sleep_in(True,True):
    return True
