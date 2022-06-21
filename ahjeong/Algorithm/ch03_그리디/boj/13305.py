import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split(' ')))
M = list(map(int, sys.stdin.readline().split(' ')))

dic = {}
min_m = min(M[0:-1])
result = 0
total = sum(L)

for d in range(len(L)):
    if M[d] == min_m:
        result += min_m * total
        break
    if M[d] != min_m:
        result += M[d] * L[d]
        total -= L[d]
    
print(result)