# 文字のカウント
#
# 与えられた英文に含まれる、各アルファベットの数を数えるプログラムを作成して下さい。 なお、小文字と大文字は区別しません。
#
# Input
# 複数の行にまたがる１つの英文が与えられます。
#
# Output
# 与えられた英文に含まれる各アルファベットの数を以下に示す形式で出力して下さい：
#
# a : aの個数
# b : bの個数
# c : cの個数
#   .
#   .
# z : zの個数
# Constraints
# 英文が含む文字の数 < 1200
import sys
alph = list("abcdefghijklmnopqrstuvwxyz")
sentence = list(sys.stdin.read().lower())
for i in alph:
    print("%s :" % i, sentence.count(i))