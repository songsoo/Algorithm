M,N= map(int, input().split())
N += 1
chess = [False, False]+[True]*(N-1) #0,1 제외
prime = []

for i in range(2,N):
    if chess[i]:
        if i >= M:
            prime.append(i)
        for j in range(2*i, N, i):
            chess[j] = False

for i in prime:
    print(i)