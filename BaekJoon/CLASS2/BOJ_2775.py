case = int(input())
for _ in range(case):
    k = int(input())
    n = int(input())

    former = [i for i in range(1,n+1)]
    latter = [0] * n

    for _ in range(1,k+1):
        latter[0] = 1
        for j in range(1,n):
            latter[j] = former[j] + latter[j-1]
        former, latter = latter, former

    print(former[n-1])