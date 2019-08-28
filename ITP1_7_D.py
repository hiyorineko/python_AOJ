# 行列の積
#
# n×m の行列 A と m×l の行列 B を入力し、それらの積である n×l の行列 C を出力するプログラムを作成してください。行列 C の各要素 cij は次の式で得られます：
#
# cij=∑k=1maikbkj
# ここで、A、B、C の各要素をそれぞれ aij、bij、cij とします。
#
# Input
# １行目に n、m、l が空白区切りで与えられます。
#
# 続く行に n×m の行列 A と m×l の行列 B が与えられます。
#
# Output
# n×l の行列 C の要素 cij を出力してください。各行の隣り合う要素を１つの空白で区切ってください。
n, m, l = map(int, input().split())
A = list()
[A.append(list(map(int, input().split()))) for i in range(n)]
B = list()
[B.append(list(map(int, input().split()))) for i in range(m)]
C = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    for j in range(l):
        _ = 0
        for k in range(m):
            _ += A[i][k]*B[k][j]
        C[i][j] = _
    print(" ".join(map(str, C[i])))