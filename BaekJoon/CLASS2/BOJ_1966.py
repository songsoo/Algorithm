# 문서의 개수, queue에서 몇번째
# 문서의 중요도
import sys
N = int(input())

def dequeue(arr, num):
    del arr[0]
    return arr, num-1

def next(arr,locat):
    arr.append(arr[0])
    del arr[0]
    locat -= 1
    if(locat<0):
        locat = len(arr)-1
    return arr, locat

for _ in range(N):
    count = 0
    num ,locat= map(int,input().split())
    queue = list(map(int, sys.stdin.readline().split()))

    while True:
        if queue[0] == max(queue):
            count += 1
            if locat==0:
                print(count)
                break
            else:
                queue, num = dequeue(queue,num)
                locat -= 1
        else:
            queue, locat = next(queue,locat)
