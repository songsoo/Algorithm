n = int(input())
import sys
arr = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
count = []
i = 1
for num in arr:

    while num>i:
        stack.append(i)
        count.append("+")
        i+=1

    if num<i:
        if stack[len(stack)-1]!=num:
            count = ["NO"]
        else:
            stack.pop()
            count.append("-")

    elif num==i:
        count.append("+")
        count.append("-")
        i+=1


    if count == ["NO"]:
        break

print(*count,sep='\n')