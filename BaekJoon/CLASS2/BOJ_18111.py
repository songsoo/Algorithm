N, M, B = map(int, input().split())
blocks = []
isSkip = False
import sys

min_time = sys.maxsize
ans_height = 0
max_height = 0
min_height = 500

for _ in range(N):
    temp_block = list(map(int, sys.stdin.readline().split()))
    if max_height < max(temp_block):
        max_height = max(temp_block)
    if min_height > min(temp_block):
        min_height = min(temp_block)
    blocks.append(temp_block)



#최대 높이부터 반복
for height in range(min_height,max_height+1):
    num = B
    temp_time = 0
    for i in range(N):
        for j in range(M):
            diff = height-blocks[i][j]
            if diff>0:
                temp_time += diff
                num -= diff
            elif diff<0:
                temp_time -= 2*diff
                num -= diff
    if num>=0:
        if min_time >= temp_time:
            min_time = temp_time
            ans_height = height

print(min_time, ans_height)
