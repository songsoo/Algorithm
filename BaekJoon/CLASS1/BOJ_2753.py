A = int(input())

if((A%4==0 and A%100!=0) or A%400==0):
    print(int(1))
else:
    print(int(0))