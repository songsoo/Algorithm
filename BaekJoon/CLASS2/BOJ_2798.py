N, M = map(int, input().split())
import sys
card_list = list(map(int, sys.stdin.readline().split()))
ans = -M
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            diff = card_list[i]+card_list[j]+card_list[k] - M
            if diff > ans and diff<0:
                ans = diff
            if diff == 0:
                print(M)
                exit()
print(M+ans)