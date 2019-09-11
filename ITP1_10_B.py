# 三角形
#
# 三角形の２辺 a, b とその間の角 C から、その三角形の面積 S、周の長さ L, a を底辺としたときの高さ h を求めるプログラムを作成して下さい。
#
# Input
# a の長さ, b の長さ, Cの大きさ（度）（整数）が空白区切りで与えられます。
#
# Output
# S, L, h をそれぞれ1行に出力して下さい。0.0001以下の誤差があってもよいものとします。
import math
a, b, c = map(float, input().split())
d = (a**2) + (b**2) - (2*(a*b * math.cos(math.radians(c))))
L = a + b + (d**0.5)
S = a * b * math.sin(math.radians(c)) / 2
h = 2 * S / a
print(str(S))
print(str(L))
print(str(h))