H, M = map(int, input().split())

if M - 45 < 0:
    if H - 1 < 0:
        H += 24
    M += 60
    H -= 1
M -= 45

print(H,M)