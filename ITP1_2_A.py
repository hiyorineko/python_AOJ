# 大小関係
# 
# ２つの整数 a, b を読み込んで、a と b の大小関係を出力するプログラムを作成して下さい。
# 
# Input
# 入力は空白で区切られた２つの整数 a, b から構成されています。
# 
# Output
# a より b の方が大きければ
# 
# a < b
# a より b の方が小さければ、
# 
# a > b
# a と b が等しければ、
# 
# a == b
# と出力して下さい。
# Constraints
# -1,000 ≤ a, b ≤ 1,000
ab = input().split(" ", 2)
a = int(ab[0])
b = int(ab[1])
if -1000 <= a and a <= 1000 and -1000 <= b and b <= 1000:
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b")
    else:
        print("a == b")