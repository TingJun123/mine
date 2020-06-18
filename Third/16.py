n = int(input())
y = (98 - n) / 3
f = 2 * y + 1
if y != int(y):
    print('No Solution')
else:
    if f > 10:
        t = y + 0.01*f
    else:
        t = y + 0.1*f
    print(t)