import sys
count = int(input())
num_list = list(int(sys.stdin.readline()) for _ in range(count))

num_list.sort()

for num in num_list:
    print(num)