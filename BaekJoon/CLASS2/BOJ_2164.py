import sys
num = int(sys.stdin.readline())
queue = [i+1 for i in range(num)]

count = 0
num = len(queue)
while len(queue)>1:
    if count == 1:
        count = (count+(len(queue) % 2))%2
        queue = queue[0::2]
    else:
        count = (count+ (len(queue) % 2))%2
        queue = queue[1::2]
print(queue[0])

# 간과한 부분, count가 연속으로 홀수일 경우



"""
#시간초과
def next():
    if len(queue)>1:
        queue.append(queue[0])
        del queue[0]

def throw():
    if len(queue) > 1:
        del queue[0]

while True:
    throw()
    next()
    if len(queue) == 1:
        print(queue[0])
        break
"""
