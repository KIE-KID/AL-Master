import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# 모든 노드를 한번씩 확인해봐야 함 --> O(V)
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):    # O(V^2)
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # 방문한 노드의 순간에서 distance 를 갱신한다.
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복 --> start를 하고 다음단계 시작하는 것
    for i in range(n-1):    # O(V-1)
        now = get_smallest_node()   # O(V)
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('무한')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])
