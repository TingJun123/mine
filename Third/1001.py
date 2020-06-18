n = int(input())
count = 0
while n != 1:
    flag = n % 2
    if flag == 0:
        n = n / 2
        count += 1
    else:
        n = (3 * n + 1) / 2
        count += 1
print(count)