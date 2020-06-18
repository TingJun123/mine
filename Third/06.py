time = input()
a = []
count = 0
for i in str(time):
    a.append(str(i))
    count += 1
if a[1] == ':':
    print(time, 'AM')
elif int(a[0])*10 + int(a[1]) < 12:
    print(time, 'AM')
elif int(a[0])*10 + int(a[1]) == 12:
    print(time, 'PM')
else:
    if count == 4:
        x = str(int(a[0]) * 10 + int(a[1]) - 12) + a[2] + a[3]
    elif count == 5:
        x = str(int(a[0]) * 10 + int(a[1]) - 12) + a[2] + a[3] + a[4]
    print(x, 'PM')