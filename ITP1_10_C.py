# 標準偏差
#
# n 人の学生を含むクラスでプログラミングの試験を行った。それぞれの得点をs1, s2 ... snとしたときの、標準偏差を求めるプログラムを作成せよ。
while True:
    n = int(input())
    if n == 0:
        break
    S = list(map(int, input().split()))
    avg = sum(S)/n
    ans = (sum([(avg-i)**2 for i in S])/n) ** 0.5
    print(str(ans))
