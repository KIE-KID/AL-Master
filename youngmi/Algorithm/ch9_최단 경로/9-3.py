# 플로이드 워셜
import sys
input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 10억
n, m = map(int, input().split())  # 노드 개수 및 간선의 개수 입력받기
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 리스트(그래프)를 만들고 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c  # a에서 b로 가는 비용은 C

# 점화식에 따라 플로이드 워션 알고리즘 수행
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 수행결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
