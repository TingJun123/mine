# N 名玩家中有 2 人扮演狼人角色，有 2 人说的不是实话，有狼人撒谎但并不是所有狼人都在撒谎
# 用正号表示好人，负号表示狼人
n = int(input())
a = []      # 列表a记录各玩家的发言
b = []      # 列表b记录各玩家判断目标玩家是否为狼人
c = []      # 列表c记录各玩家判断的对象
wolf = 0
wolf_man = []
lie = 1
lie_man = []
for i in range(0, n):
    a.append(input())
    b.append(a[i][0])
    c.append(a[i][1])
for j in range(0, n):
    if b[j] == '-':
        if lie == 1:
            wolf += 1
            wolf_man.append(c[j])
        else:
            lie_man.append(b[j])

print(wolf_man[0], wolf_man[1])





