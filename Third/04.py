n = int(input())
count1 = 0
count2 = 0
a = []
while(n != 0):
    k = n % 2
    a.append(k)
    n = n // 2
while(a.__len__() < 8):
    a.append(0)
for i in range(1,4):
    count1 += a[i]*(2**i)
    i -= 1
if(a[0] == 1):
    count1 += 1
for i in range(5,8):
    count2 += a[i] * (2 ** (i-4))
    i -= 1
if(a[4] == 1):
    count2 += 1
x = count2*10 + count1
print(x)