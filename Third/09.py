year, hour = input().split()
year = int(year)
hour = int(hour)
if year < 5:
    if hour > 40:
        x = 40 * 30 + (hour - 40) * 30 * 1.5
    else:
        x = hour * 30
else:
    if hour > 40:
        x = 40 * 50 + (hour - 40) * 50 * 1.5
    else:
        x = hour * 50
print('%.2f'%x)