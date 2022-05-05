K, N = map(int, input().split())
import sys
lans = [int(sys.stdin.readline()) for _ in range(K)]


def binarySearch(min,max):
    avg = (min + max) // 2
    if min>max:
        return max
    num = 0
    for i in range(K):
        num += lans[i]//(avg)
    if num>=N:
        return binarySearch(avg+1,max)
    else:
        return binarySearch(min,avg-1)

print(binarySearch(1,max(lans)))



