import itertools

if __name__ == '__main__':
    A = int(input())
    B = A + 1
    C = A + 2
    D = A + 3
    y = []
    z = []
    x = list(itertools.permutations([A, B, C, D], 3))
    for i in range(0, 24):
        y.append(list(x[i]))
    for j in range(0, 4):
        for k in range(0, 6):
            m = y[k+j*6][0]*100 + y[k+j*6][1]*10 + y[k+j*6][2]
            z.append(m)
    for n in range(0, 4):
        print(z[(0+n*6)], z[(1+n*6)], z[(2+n*6)], z[(3+n*6)], z[(4+n*6)], z[(5+n*6)])


