# 数列の反転
#
# 与えられた数列を逆順に出力するプログラムを作成して下さい。
#
# Input
# 入力は以下の形式で与えられます：
#
# n
# a1 a2 . . . an
# n は数列の長さを示し、ai は i 番目の数を表します。
#
# Output
# 逆順の数列を１行に出力して下さい。数列の要素の間に１つの空白を入れて下さい（最後の数の後に空白は入らないことに注意して下さい）。
#
# Constraints
# n ≤ 100
# 0 ≤ ai < 1000
n = int(input())
ai = list(map(int, input().split()))
for i in range(n // 2):
    ai[i], ai[n-(1+i)] = ai[n-(1+i)], ai[i]
print(" ".join(map(str, ai)))
