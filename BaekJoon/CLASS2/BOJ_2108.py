import sys
count = int(input())
nums = list(int(sys.stdin.readline()) for _ in range(count))

def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2

    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr= []
    l = h = 0

    while l<len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def getMode():
    modeCount = []
    modeNumber = []
    modeMax = []

    for num in nums:
        if num not in modeNumber:
            modeNumber.append(num)
            modeCount.append(1)
        else:
            modeCount[modeNumber.index(num)]+=1

    maxNum = max(modeCount)

    for a,b in zip(modeCount,modeNumber):
        if a == maxNum:
            modeMax.append(b)

    if modeCount.count(maxNum)>1:
        return modeMax[1]
    else:
        return modeMax[0]

nums = merge_sort(nums)

#평균
print(round(sum(nums)/len(nums)))
#중앙값
print(nums[len(nums)//2])
#최빈값
print(getMode())
#범위
print(nums[len(nums)-1]-nums[0])

