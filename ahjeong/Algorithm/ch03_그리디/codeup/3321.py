import math
n = int(input())
dou, top = map(int, input().split())
kcal = int(input())
kcal_list = []
for i in range(n):
    kcal_list.append(int(input()))
kcal_list.sort(reverse = True)

max = 0
for i in range(n):
    kcal_sum = sum(kcal_list[0:i+1])
    print(kcal_sum)
    result = (kcal + kcal_sum) // (dou + (top * (i+1)))
    print(result)
    if (max < result):
        max = result
    else :
        continue

print(max)
