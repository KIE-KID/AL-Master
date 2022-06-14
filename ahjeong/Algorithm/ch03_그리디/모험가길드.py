num = int(input())
scared = list(map(int, input().split(' ')))

scared.sort()

groups = []
count = 0
result = 0

for i in scared:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)


# for i in range(len(scared)):
#     if i < num:
#         tmp = scared[i:scared[i]]
#         groups.append(tmp)
#         num -= scared[i]
#         i = i + scared[i]
#     else:
#         print('0')
    
# print(groups)

