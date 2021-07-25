# 난이도 (하)
# 풀이 시간 : 3분
# 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수

r, c = map(int, input().split())
data = []
min_list = []
for i in range(r):
    data.append(list(map(int, input().split())))
    min_list.append(min(data[i]))

result = max(min_list)
