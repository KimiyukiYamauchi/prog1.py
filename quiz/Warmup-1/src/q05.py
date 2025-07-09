# 飼っているオウムのおしゃべりがトラブルになるかを返す関数
# おしゃべりがうるさいオウムがいます。「$hour」引数は、0から23の
# 範囲での現在の時刻を表します。オウムがおしゃべりしていて、時刻が
# 7時より前または20時より後であれば、私たちは困ります。
# 困っている場合は True を返します。
# 
# @param bool talking オウムがおしゃべるしているときはTrue、そうでなければFalse
# @param int hour 時刻(0以上23以下)
# 
# @return talkingがTrueで、hourが7より小さいか20より大きければTrueを返す
#         それ以外はFalse
# 例：
# 　parrot_trouble(True, 6) → True
# 　parrot_trouble(True, 7) → False
# 　parrot_trouble(False, 6) → False
# 

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False
