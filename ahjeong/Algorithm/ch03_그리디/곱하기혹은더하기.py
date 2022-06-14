s = input()

result1 = 0
tmp = 1

print(s)

for i in range(len(s)):
    if int(s[i]) == 0:
        result1 += int(s[i])
        tmp += result1
    else:
        tmp *= int(s[i])
        result1 = tmp

print(result1)