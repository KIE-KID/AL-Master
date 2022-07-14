from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split(' '))

graph = [[] for i in range(n+1)]

for _ in range(m):
    f, s = map(int, input().split(' '))
    graph[f].append(s)
    graph[s].append(f)

visited = [False]*(n+1)
visited2 = [False]*(n+1)

dfs_result = []
bfs_result = []

# dfs
def dfs(v, graph, visited):
    visited[v] = True
    dfs_result.append(str(v))
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == False:
            dfs(i, graph, visited)


# bfs
def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        bfs_result.append(str(now))
        graph[now].sort()
        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(v, graph, visited)
bfs(v, graph, visited2)

print(' '.join(dfs_result))
print(' '.join(bfs_result))