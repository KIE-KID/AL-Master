'''
예제 4-2 시각
'''

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k) :
                count += 1

print(count)