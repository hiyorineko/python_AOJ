# 数字の和
#
# 与えられた数の各桁の和を計算するプログラムを作成して下さい。
#
# Input
# 複数のデータセットが入力として与えられます。各データセットは１つの整数 x を含む１行で与えられます。
#
# x は 1000 桁以下の整数です。
#
# x が 0 のとき入力の終わりとします。このデータセットに対する出力を行ってはいけません。
#
# Output
# 各データセットに対して、x の各桁の和を１行に出力して下さい。
from functools import reduce
while True:
    x = input()
    if x == "0":
        break
    print(reduce(lambda a, b : a + b, map(int, list(x))))