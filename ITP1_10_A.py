# 距離
#
# ２点 P1(x1, y1), P2(x2, y2) の距離を求めるプログラムを作成せよ。
#
# Input
# x1, y1, x2, y2 （実数）が空白区切りで与えられます。
#
# Output
# P1とP2の距離を実数で１行に出力して下さい。0.0001以下の誤差があってもよいものとします。
x1, y1, x2, y2 = map(float, input().split())
print((((x2-x1)**2)+((y2-y1)**2))**0.5)