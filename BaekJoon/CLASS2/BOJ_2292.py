N = int(input())

i=7
count = 1
if N==1:
    print(count)
else:
    while True:
        if N <= i:
            print(count+1)
            break
        count += 1
        i += 6* (count)