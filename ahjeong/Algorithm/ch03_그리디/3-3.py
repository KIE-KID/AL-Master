r, c = map(int, input().split())
data = []
min_list = []
for i in range(r):
    data.append(list(map(int, input().split())))
    min_list.append(min(data[i]))

result = max(min_list)

print(result)