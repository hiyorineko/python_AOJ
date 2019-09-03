# 文字列変換
#
# 文字列 str に対して、与えられた命令の列を実行するプログラムを作成してください。命令は以下の操作のいずれかです：
#
# print a b: str の a 文字目から b 文字目までを出力する。
# reverse a b: str の a 文字目から b 文字目までを逆順にする。
# replace a b p: str の a 文字目から b 文字目までを p に置き換える。
# ここでは、文字列 str の最初の文字を 0 文字目とします。
#
# Input
# 1 行目に文字列 str が与えられます。str は英小文字のみ含みます。2 行目に命令の数 q が与えられます。続く q 行に各命令が上記の形式で与えられます。
#
# Output
# 各 print 命令ごとに文字列を１行に出力してください。
#
# Constraints
# 1≤strの長さ≤1000
# 1≤q≤100
# 0≤a≤b<strの長さ
# replace 命令では b−a+1=pの長さ
s = list(map(str, input()))
for i in range(int(input())):
    command = input().split()
    if command[0] == 'print':
        tmp = list()
        for j in range(int(command[1]), int(command[2])+1):
            tmp.append(s[j])
        print("".join(tmp))
    elif command[0] == 'reverse':
        head = list()
        tale = list()
        c = 0
        for j in range(len(s)):
            if j < int(command[1]):
                head.append(s.pop(j-c))
                c += 1
            elif int(command[2]) < j:
                tale.append(s.pop(j-c))
                c += 1
        s.reverse()
        s = list("".join(head) + "".join(s) + "".join(tale))
    elif command[0] == 'replace':
        param = list(command[3])
        for j in range(len(s)):
            if int(command[1]) <= j <= int(command[2]):
                s[j] = param.pop(0)
