# 範囲
# 
# ３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、満たさないならば"No"を出力するプログラムを作成して下さい。
# 
# Input
# ３つの整数が空白で区切られて与えられます。
# 
# Output
# YesまたはNoを１行に出力して下さい。
# 
# Constraints
# 0 ≤ a, b, c ≤ 100
abc = input().split(" ", 3)
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])
if 0 <= a and a <= 100 and 0 <= b and b <= 100 and 0 <= c and c <= 100:
    if a < b and b < c:
        print("Yes")
    else:
        print("No")