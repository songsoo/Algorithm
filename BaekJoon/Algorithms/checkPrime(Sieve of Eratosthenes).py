N = 10000

chess = [False, False]+[True]*(N-1) #0,1 제외
prime = []

for i in range(2,N):
    if chess[i]:
        prime.append(i)
        for j in range(2*i, N, i):
            chess[j] = False

print(prime)