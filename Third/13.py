A, B = input().split()
A = int(A)
B = int(B)
count = 0
Sum = 0
a = []
for i in range(A, B+1):
    Sum += i
    a.append(i)
    count += 1
    if count == 5:
        print('%+5s%+5s%+5s%+5s%+5s' % (a[0], a[1], a[2], a[3], a[4]))
        a.clear()
        count = 0
if count == 1:
    print('%+5s' % a[0])
if count == 2:
    print('%+5s%+5s' % (a[0], a[1]))
if count == 3:
    print('%+5s%+5s%+5s' % (a[0], a[1], a[2]))
if count == 4:
    print('%+5s%+5s%+5s%+5s' % (a[0], a[1], a[2], a[3]))
print('Sum = %d' % Sum)
