from collections import deque

N, M = map(int, input().split(' '))

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0

def dfs(x, y):
    if x <= -1 and x >= N or y <= -1 and y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
        
print(result)
        
