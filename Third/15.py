N, U, D = input().split()
N = int(N)
U = int(U)
D = int(D)

i = N - 1
j = U - D
if N-1 <= U:
    k = 1
elif (i//j - 1)*2 + U >= N - 1:
    k = (i//j - 1) * 2 + 1
else:
    k = (i // j) * 2 + 1
print(k)