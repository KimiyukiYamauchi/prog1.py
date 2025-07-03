# monkey_trouble: 2匹のサルがトラブルを起こすかをチェックする関数
# ２匹のサルがトラブルを起こすかをチェックする関数
# 2匹のサル、a と b がおり、パラメーター a_smile と b_smile は
# それぞれが笑っているかどうかを示します。両方が笑っている場合、
# またはどちらも笑っていない場合、2匹のサルはトラブルを起こします。
# 困っている場合は True を返します。
# 
# a_smile aのサルが笑っていればTrue、そうでなければFalse
# b_smile bのサルが笑っていればTrue、そうでなければFalse
# 
# トラブルを起こす場合はTrue、そうでなければFalse
# 
# ２匹のサルが両方とも笑っているか、両方とも笑っていなければトラブルを起こす
# 例：
# 　monkeyTrouble(True, True) → True
# 　monkeyTrouble(False, False) → True
# 　monkeyTrouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
    if a_smile==b_smile:
        return True
    if a_smile!=b_smile:
        return False
