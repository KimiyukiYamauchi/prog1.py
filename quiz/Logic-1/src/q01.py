# リスが集まってパーティーをするとき、彼らは葉巻を好む。
# リスのパーティーが成功するのは、葉巻の本数が40本から60本の間である。
# 週末の場合は、葉巻の数に上限はありません。与えられた値でのパーティが
# 成功した場合はTrueを、そうでない場合はFalseを返します。
#
#  cigars 葉巻の本数
#  is_weekend 週末かどうか
#  
#  @return パーティが成功した場合はTrueを、そうでない場合はFalseを返します。
#
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
    if is_weekend == True:
        return cigars >= 40
    else:
        return 40 <= cigars <= 60
