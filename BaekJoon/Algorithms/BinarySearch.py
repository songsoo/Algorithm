#1654

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
answer = 15

def binarySearch(min, max):
    if(min>max):
        return None

    mid = (min+max)//2

    if answer>arr[mid]:
        return binarySearch(mid+1,max)
    elif answer==arr[mid]:
        return arr[mid]
    else:
        return binarySearch(min, mid-1)

print(binarySearch(0,len(arr)-1))


