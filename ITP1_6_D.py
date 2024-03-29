# ベクトルと行列の積
#
# n×m の行列 A と、m×1 の列ベクトルb を読み込み、A と b の積を出力するプログラムを作成してください。
#
# 次のように m 個の数を縦に並べたものを m×1の列ベクトルと呼びます。
#
# b=⎛⎝⎜⎜⎜b1b2:bm⎞⎠⎟⎟⎟
# 次のように n 個の数を含む列ベクトルを m 個横に並べたものを n×m の行列と呼びます。
#
# A=⎛⎝⎜⎜⎜a11a21:an1a12a22:an2......:...a1ma2m:anm⎞⎠⎟⎟⎟
# ベクトルまたは行列の中に含まれる数のことを要素と呼び、m×1 の列ベクトル b の上から i 番目の要素は bi(i=1,2,...,m)、n×m の行列 A には n×m 個の要素が含まれ、i 行 j 列目の要素は aij(i=1,2,...,n,j=1,2,...,m)で示されます。
#
# n×mの行列 A とm×1の列ベクトル b の積は、n×1の列ベクトル c となり、c の i 番目の要素 ci は次の式で得られます：
#
# ci=∑j=1maijbj=ai1b1+ai2b2+...+aimbm
# Input
# １行目に n と m が空白区切りで与えられます。続く n 行に行列 A の要素 aij が空白区切りで与えられます。続く m 行にベクトル b の要素 bi がそれぞれ１行に与えられます。
#
# Output
# 出力は n 行からなります。ベクトル c の要素 ci をそれぞれ１行に出力してください。
#
# Constraints
# 1≤n,m≤100
# 0≤bi,aij≤1000
n, m = map(int, input().split())
A = list()
b = list()
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(m):
    b.append(int(input()))
for i in range(n):
    _ = 0
    for j in range(m):
        _ += (A[i][j] * b[j])
    print(_)