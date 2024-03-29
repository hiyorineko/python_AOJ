# 長方形の描画
#
# たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。
#
# 1 cm × 1cm の長方形を '#'で表します。
#
# Input
# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：
#
# H W
#
# H, W がともに 0 のとき、入力の終わりとします。
#
# Output
# 各データセットについて、H × W 個の '#' で描かれた長方形を出力して下さい。
#
# 各データセットの後に、１つの空行を入れて下さい。
#
# Constraints
# 1 ≤ H ≤ 300
# 1 ≤ W ≤ 300
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        print("#"*w)
    print()
