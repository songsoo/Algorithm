Arr = list(map(int, input().split()))
count = len(Arr)

for i in range(count-1,0,-1):
    for j in range(0,i):
        if Arr[j]>Arr[j+1]:
            Arr[j], Arr[j+1] = Arr[j+1], Arr[j]

print(Arr)