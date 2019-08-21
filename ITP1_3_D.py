# 約数の数
#
# ３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラムを作成してください。
#
# Input
# a、b、c が１つの空白区切りで１行に与えられます。
#
# Output
# 約数の数を１行に出力してください。
#
# Constraints
# 1≤a,b,c≤10000
# a≤b
a, b, c = map(int, input().split())
count = 0
for i in range(a, (b + 1)):
    if c % i == 0:
        count += 1
print(count)