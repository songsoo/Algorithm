
import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
ANS = list(map(int,sys.stdin.readline().split()))

def merge(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2


    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])
    merged_arr = []

    l = h = 0
    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l] > high_arr[h]:
            merged_arr.append(high_arr[h])
            h+=1
        else:
            merged_arr.append(low_arr[l])
            l+=1
    merged_arr += (low_arr[l:])
    merged_arr += (high_arr[h:])

    return merged_arr

def binarySearch(arr,ans,min,max):
    if min>max:
        return None

    mid = (min+max)//2
    if ans==arr[mid]:
        return arr[mid]
    elif ans<arr[mid]:
        return binarySearch(arr,ans,min,mid-1)
    else:
        return binarySearch(arr, ans, mid + 1, max)

A = merge(A)

for ans in ANS:

    if binarySearch(A,ans,0,len(A)-1)==ans:
        print(1)
    else:
        print(0)

