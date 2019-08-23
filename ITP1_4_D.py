# 最小値、最大値、合計値
#
# n 個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。
#
# Input
# １行目に整数の数 n が与えられます。２行目に n 個の整数 ai が空白区切りで与えられます。
#
# Output
# 最小値、最大値、合計値を空白区切りで１行に出力してください。
#
# Constraints
# 0<n≤10000
# −1000000≤ai≤1000000
n = int(input())
ai = list(map(int, input().split()))
min = 1000000
max = -1000000
sum = 0
for i in range(n):
    if ai[i] >= max:
        max = ai[i]
    if min >= ai[i]:
        min = ai[i]
    sum += ai[i]
print("%d %d %d" % (min, max, sum))
