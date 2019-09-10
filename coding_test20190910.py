n = list(input().split())
for i in n:
    for j in n:
        for k in n:
            print(i+j+k)

#wip
# N = int(input())
# x = list(input().split())
# a = ""
#
#
# def mixChar(N, a):
#     if N > 0:
#         for i in x:
#             a = a + i
#             mixChar(N-1, a)
#
#
# mixChar(N, a)
#
# re = [a[i: i+N] for i in range(0, len(a), N)]
# print(re)

import calendar
import datetime
y, m = map(int, input().split("/"))
firstDay = 1
lastDay = calendar.monthrange(y,m)[1]
print(str(y) + "/" + str(m).zfill(2))
week = ["" for i in range(7)]
for i in range(firstDay,lastDay+1):
    stry = str(y)
    strm = str(m)
    strd = str(i).zfill(2)
    day = "%s/%s/%s"%(stry,strm,strd)
    a = datetime.datetime.strptime(day, '%Y/%m/%d')
    weekday = a.weekday()
    for j in range(7):
        if weekday == j:
            if weekday == 5:
                week[j] = "[" + str(i).rjust(2) + "]"
            elif weekday == 6:
                week[j] = "(" + str(i).rjust(2) + ")"
                print(" ".join(week))
                week = ["" for i in range(7)]
            else:
                week[j] = str(i).rjust(2)
        else:
            if not week[j]:
                week[j] = "  "
    if i == lastDay:
        print(" ".join(week))