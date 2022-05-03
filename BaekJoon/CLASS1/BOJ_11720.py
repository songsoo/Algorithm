count = int(input())
num = input()
sum = 0

for i in range(count):
    sum += int(num[i:i+1])
print(int(sum))

