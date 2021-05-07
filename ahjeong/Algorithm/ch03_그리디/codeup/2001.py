# 코드업 문제 그리디 - https://www.codeup.kr/problem.php?id=2001&rid=0

cost = []
for i in range(5):
    cost.append(int(input()))

pasta_min = min(cost[0:3])
juice_min = min(cost[3:5])

result = round((pasta_min + juice_min) * 1.1, 1)

print(result)