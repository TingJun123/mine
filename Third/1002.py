n = input()
Sum = 0
PinYin = []
for i in range(0, len(n)):
    Sum += int(n[i])
a = Sum // 100
b = (Sum // 10) % 10
c = Sum % 10
if a == 1:
    PinYin.append('yi')
elif a == 2:
    PinYin.append('er')
elif a == 3:
    PinYin.append('san')
elif a == 4:
    PinYin.append('si')
elif a == 5:
    PinYin.append('wu')
elif a == 6:
    PinYin.append('liu')
elif a == 7:
    PinYin.append('qi')
elif a == 8:
    PinYin.append('ba')
elif a == 9:
    PinYin.append('jiu')

if b == 0:
    PinYin.append('ling')
elif b == 1:
    PinYin.append('yi')
elif b == 2:
    PinYin.append('er')
elif b == 3:
    PinYin.append('san')
elif b == 4:
    PinYin.append('si')
elif b == 5:
    PinYin.append('wu')
elif b == 6:
    PinYin.append('liu')
elif b == 7:
    PinYin.append('qi')
elif b == 8:
    PinYin.append('ba')
elif b == 9:
    PinYin.append('jiu')


if c == 0:
    PinYin.append('ling')
if c == 1:
    PinYin.append('yi')
if c == 2:
    PinYin.append('er')
if c == 3:
    PinYin.append('san')
if c == 4:
    PinYin.append('si')
if c == 5:
    PinYin.append('wu')
if c == 6:
    PinYin.append('liu')
if c == 7:
    PinYin.append('qi')
if c == 8:
    PinYin.append('ba')
if c == 9:
    PinYin.append('jiu')


if a == 0:
    if b == 0:
        print(PinYin[1])
    else:
        print(PinYin[0], PinYin[1])
else:
    print(PinYin[0], PinYin[1], PinYin[2])