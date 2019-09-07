# #1~N 3けた 組み合わせ
# _ = int(input())
# ans = 0
# for i in range(_):
#     for j in range(_):
#         for k in range(_):
#             ans += 1
# print(str(ans))

#buffe
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# pt = 0
# for i in range(N):
#     pt += B[A[i]-1]
#     if i > 0 and (A[i]-1) == A[i-1]:
#         pt += C[A[i-1]-1]
# print(str(pt))

#C - Maximal Value
# N = int(input())
# B = list(map(int, input().split()))
# asum = 0
# for i in range(0, N, 2):
#
# print(asum)

#D - Face Produces Unhappiness
n, k = map(int, input().split())
s = list(input())
lc = s.count('L')
rc = s.count('R')
while k > 0:
    for i in range(n):
        if i == n-1:
            break
        if lc > rc:
            _ = 'L'
        else:
            _ = 'R'
        if s[i] == _ and s[(n-1)-i] == _:
            continue
        s[i], s[(n-1)-i] = s[(n-1)-i], s[i]
        if s[i] == 'L':
            s[i] = 'R'
        else:
            s[i] = 'L'
        if s[(n-1)-i] == 'L':
            s[(n-1)-i] = 'R'
        else:
            s[(n-1)-i] = 'L'
        k -= 1
        if k == 0:
            break
pt = 0
for i in range(n):
    if i != n-1:
        if s[i] == s[i+1]:
            pt += 1
print(pt)