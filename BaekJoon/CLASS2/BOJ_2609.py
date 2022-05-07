N,M = map(int,input().split())

def Euclid(high, low):
    if high%low == 0:
        return low
    else:
        return Euclid(low,high%low)

if N<M:
    N,M = M,N

GCD = Euclid(N,M)
LCM = GCD * N//GCD * M//GCD

print(GCD)
print(LCM)