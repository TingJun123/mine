# 当x不超过15吨时，y=4x/3；超过后，y=2.5x−17.5。
x = int(input())
if x < 15:
    y = 4 * x / 3
else:
    y = 2.5 * x - 17.5
print('%.2f' % y)