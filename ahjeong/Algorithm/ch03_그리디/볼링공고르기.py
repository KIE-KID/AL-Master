N, M = input().split(' ')
W = list(map(int, input().split(' ')))

count = 0

for i in range(len(W)):
    tmp = W[i+1:]
    for j in range(len(tmp)):
        if W[i] != tmp[j]:
            count += 1

print(count)