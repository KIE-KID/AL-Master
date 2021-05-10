# DFS 메서드 정듸
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 인접한 노드가 방문되지 않은 상태라면 dfs 실행
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# 0번 노드는 비워둠
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
# 기본적으로 방문하지 않은 False로 초기화 0번 노드는 사용하지 않기때문에 하나더 큰 크기로 초기화
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

'''
실행결과: 1 2 7 6 8 3 4 5
'''