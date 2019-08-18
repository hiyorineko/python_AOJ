# 3 つの数の整列
# 
# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
# 
# Input
# ３つの整数が空白で区切られて与えられます。
# 
# Output
# 小さい順に並べ替えた３つの整数を１行に出力して下さい。整数の間に１つの空白を入れて下さい。
# 
# Constraints
# 1 ≤ ３つの整数 ≤ 10,000
# Sample Input
# 3 8 1
# Sample Output
# 1 3 8
a,b,c = map(int,input().split())
if 1 <= a and a <= 10000 and 1 <= b and b <= 10000 and 1 <= c and c <= 10000:
    if a <= b and b <= c: # a<b<c
        d = a
        e = b
        f = c
    elif a <= c and c <= b: # a<c<b
        d = a
        e = c
        f = b
    elif b <= a and a <= c: # b<a<c
        d = b
        e = a
        f = c
    elif b <= c and c <= a: # b<c<a
        d = b
        e = c
        f = a
    elif c <= a and a <= b: # c<a<b
        d = c
        e = a
        f = b
    elif c <= b and b <= a: # c<b<a
        d = c
        e = b
        f = a
    print(str(d) + " " + str(e) + " " + str(f))