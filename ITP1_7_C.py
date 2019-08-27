# 表計算
#
# 表計算を行う簡単なプログラムを作成します。
#
# 表の行数rと列数c、r × c の要素を持つ表を読み込んで、各行と列の合計を挿入した新しい表を出力するプログラムを作成して下さい。
#
# Input
# 最初の行にrとcが空白区切りで与えられます。続くr行にそれぞれc個の整数が空白区切りで与えられます。
#
# Output
# (r+1) × (c+1) の新しい表を出力して下さい。各行の隣り合う整数は１つの空白で区切って下さい。各行の最後の列としてその行の合計値を、各列の最後の行としてその列の合計値を、最後の行・列に表全体の合計値を挿入して下さい。
#
# Constraints
# 1 ≤ r, c ≤ 100
# 0 ≤ 要素 ≤ 100
r, c = map(int, input().split())
_ = list()
__ = [0 for i in range(c + 1)]
for i in range(r):
    _.append(list(map(int, input().split())))
    _[i].append(sum(_[i]))
    __ = [(__[j] + _[i][j]) for j in range(c + 1)]
    print(" ".join(map(str, _[i])))
print(" ".join(map(str, __)))