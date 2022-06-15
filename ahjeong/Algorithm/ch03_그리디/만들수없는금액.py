N = input()
M = list(map(int, input().split(' ')))

M.sort()

target = 1

for i in M:
     if target < i:
         break
     target += i

print(target)