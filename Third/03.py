n = int(input())
a = (n // 10) % 10         # a 是十位
b = n // 100               # b 是百位
c = n % 10                 # c 是个位
k = c*100 + a * 10 + b
print(k)