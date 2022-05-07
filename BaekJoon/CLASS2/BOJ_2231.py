M = int(input())

def getDivSum(num):
    result = num
    index = 10
    while num>10:
        result += num%index
        num = num//10
    result += num
    return result

if M >= 54:
    count = 54
else:
    count = M

for i in range(M-count,M):
    if getDivSum(i)==M:
        print(i)
        exit()
print(0)

