n = int(input())
a = []
t = 0           # t为P和T中间的A的数目
location = 0         # loc为p的位置
flag = 0        # 判断P是否已经达到
temp = 0        # temp用于获取k的数据
loc = 0         # loc是当前元素的下标
cop_P = cop_T = 0     # cop用于判断有无多余的P和T
error = False   # error用于输入错误时跳出循环不计算
for i in range(0, n):
    x = list(input())
    a.append(x)
for j in range(0, a.__len__()):
    loc = t = cop_T = cop_P = 0
    if len(a[j]) < 3:
        print('NO')
        continue
    for k in range(0, len(a[j])):
        if a[j][k] != 'P' and a[j][k] != "A" and a[j][k] != "T":
            print('NO')
            error = True
            break
        loc += 1
        if a[j][k] == 'P':
            flag = 1
            cop_P += 1
            temp = k+1
            location = loc
        if a[j][k] == 'T':
            cop_T += 1
        while flag == 1:
            if a[j][temp] == 'A':
                t += 1
                temp += 1
            else:
                flag = 0
    if error:
        error = False
        continue
    elif cop_P > 1 or cop_T > 1:
        print("NO")
        continue
    if (location-1) * t != len(a[j]) - (location + t + 1):
        print('NO')
    else:
        print('YES')