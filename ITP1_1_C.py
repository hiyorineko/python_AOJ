# 長方形の面積と周の長さ
# 
# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
# 
# input
# a と b が１つの空白で区切られて与えられます。
# 
# output
# 面積と周の長さを１つの空白で区切って１行に出力して下さい。
# 
# constraints
# 1 ≤ a, b ≤ 100
ab = input().split(" ", 2)
a = int(ab[0])
b = int(ab[1])
if 0 < a and a < 101 and 0 < b and b < 101:
  print(str(a * b) + " " + str((a + b) * 2))
