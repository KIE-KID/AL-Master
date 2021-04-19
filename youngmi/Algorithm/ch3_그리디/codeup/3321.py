k

n = int(input())# 토핑의 종류 수 n
a, b = map(int, input().split())# 도우의 가격 a, 토핑의 가격 b
c = int(input())# 도우의 칼로리 c
d = []
for i in range(n):
    d.append(int(input()))  # 토핑 칼로리 수 di

result = 0
d.sort(reverse=True)
for j in range(n):
    k = d[:j+1]# 선택한 토핑
    price = a + len(k) * b
    all_kcal = c + sum(k)
    temp_result = all_kcal/price
    result = max(result, temp_result)

print(int(result))
