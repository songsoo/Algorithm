import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

chess = [False]*2 + [True]*999
prime = []

for i in range(2,1001):
    if chess[i]:
        prime.append(i)
        for j in range(i**2,1001,i):
            chess[j]=False
count = 0
for num in nums:
    if num in prime:
        count+=1
print(count)
