a, b, c = input().split()
a = int(a)
c = int(c)
flag = 0        # 标志位
op = ['+', '-', '*', '/', '%']
for i in range(0, 5):
    if b == op[i]:
        flag = 1
        break
if flag == 1:
    if i == 0:
        x = a + c
    if i == 1:
        x = a - c
    if i == 2:
        x = a * c
    if i == 3:
        x = a / c
    if i == 4:
        x = a % c
    print(int(x))
else:
    print('ERROR')
