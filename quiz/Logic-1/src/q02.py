# あなたとデートの相手はレストランでテーブルを取ろうとしている。
# パラメータ 「you 」はあなたの服装のおしゃれ度を0から10の範囲で表し、
# 「date 」はデートの相手の服装のおしゃれ度を表す。
# テーブルを取得した結果は、0=no、1=maybe、2=yesのint値としてエンコードされる。
# もしどちらかがとてもおしゃれで、8以上なら、結果は2（yes）になる。
# ただし、どちらかのスタイルが2以下なら、結果は0（no）。
# そうでなければ結果は1（maybe）。
# 
#  you あなたの服装のおしゃれ度、0から10の範囲
#  date デートの相手の服装のおしゃれ度、0から10の範囲
#  
#  @return 0=no、1=maybe、2=yesの整数値のいずれか
#
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
