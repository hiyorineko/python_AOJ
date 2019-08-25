# 公舎の入居者数
#
# Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、各部屋の入居者数を出力するプログラムを作成して下さい。
#
# n件の情報が与えられます。各情報では、４つの整数b, f, r, vが与えられます。これは、b棟f階のr番目の部屋にv人が追加で入居したことを示します。vが負の値の場合、-v人退去したことを示します。
#
# 最初、全ての部屋には誰も入居していないものとします。
#
# Input
# 最初の行に情報の数 n が与えられます。
#
# 続いて n 件の情報が与えられます。各情報には４つの整数 b, f, r, v が空白区切りで１行に与えられます。
#
# Output
# ４棟について入居者数を出力して下さい。各棟について、１階、２階、３階の順に入居者数を出力します。各階については、１番目、２番目、・・・、１０番目の部屋の入居者数を順番に出力します。入居者数の前には１つの空白を出力して下さい。また、各棟の間には####################(20個の#)で区切って下さい。
#
# Constraints
# 間違った棟番号・階・部屋番号は与えられない。
# 管理の過程で１部屋の入居者数が０より少なくなることはない。
# 管理の過程で１部屋の入居者数が9より多くなることはない。
n = int(input())
b1 = list()
b2 = list()
b3 = list()
b4 = list()
_1 = list()
_2 = list()
_3 = list()
_4 = list()
for i in range(1,4):
    for j in range(1,11):
        _1.append(0)
        _2.append(0)
        _3.append(0)
        _4.append(0)
    b1.append(_1)
    b2.append(_2)
    b3.append(_3)
    b4.append(_4)
    _1 = list()
    _2 = list()
    _3 = list()
    _4 = list()

for i in range(n):
    b, f, r, v = map(int, input().split())
    if b == 1:
        b1[f-1][r-1] += v
    elif b == 2:
        b2[f-1][r-1] += v
    elif b == 3:
        b3[f-1][r-1] += v
    else:
        b4[f-1][r-1] += v

print(" " + " ".join(map(str, b1[0])))
print(" " + " ".join(map(str, b1[1])))
print(" " + " ".join(map(str, b1[2])))
print("#"*20)
print(" " + " ".join(map(str, b2[0])))
print(" " + " ".join(map(str, b2[1])))
print(" " + " ".join(map(str, b2[2])))
print("#"*20)
print(" " + " ".join(map(str, b3[0])))
print(" " + " ".join(map(str, b3[1])))
print(" " + " ".join(map(str, b3[2])))
print("#"*20)
print(" " + " ".join(map(str, b4[0])))
print(" " + " ".join(map(str, b4[1])))
print(" " + " ".join(map(str, b4[2])))