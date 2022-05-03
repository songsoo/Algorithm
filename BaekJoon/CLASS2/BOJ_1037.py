numCount = int(input())
numString = input()
numArr = list(map(int,numString.split()))

biggest = max(numArr)
A = biggest

for i in numArr:
    if A%i != 0:
        for j in range(min(A,i),0,-1):
            if(A%j == 0 and i%j == 0):
                A = A * i/j
                break

if A==biggest:
    for k in range(2, A+1):
        if A%k == 0:
            A = A * k
            break

print(int(A))
