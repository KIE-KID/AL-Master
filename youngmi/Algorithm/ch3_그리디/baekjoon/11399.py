'''
11399
메모리:28776KB  시간:68ms  코드길이: 131B
'''

n = int(input())
p = list(map(int,input().split()))
p.sort()
time = 0

for i in range(n):
    time += (n-i) * p[i]    #  total += sum(time[:i+1])
print(time)