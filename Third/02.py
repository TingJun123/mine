a, b = map(int, input().split())
x = a // 100     # 当前小时
y = a % 100    # 当前分钟
z = b // 60     # 流逝小时
m = b % 60      # 流逝分钟
n = y + m
if ((n // 60) > 0):
    k = ((x + z + 1)*100 + (n % 60))
else:
    k = ((x + z) * 100 + n)
print(k)

