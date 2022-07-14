n = int(input())
m = int(input())

# 연결된 그래프 리스트 만들기
graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    f, s = map(int, input().split(' '))
    graph[f].append(s)
    graph[s].append(f)

visit = [False] * (n+1)

# dfs
def dfs(start, graph, visit):
    visit[start] = True
    for i in graph[start]:
        if visit[i] == False:
            dfs(i, graph, visit)
    return visit

visit = dfs(1, graph, visit)
result = visit.count(True) - 1
print(result)