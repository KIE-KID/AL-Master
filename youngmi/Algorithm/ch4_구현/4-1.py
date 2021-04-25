'''
예제4-1 상하좌우
'''
n = int(input())
d = list(map(str,input().split()))
start = [1,1]
print(start[0],start[1])
for i in d:
    if i == 'R' and start[1] < n:
        start[1] += 1
    elif i == 'L' and start[1] > 1:
        start[1] -= 1
    elif i == 'D' and start[0] < n:
        start[0] +=1
    elif i == 'U' and start[0] > 1:
        start[0] -=1

print(' '.join(map(str,start)))
