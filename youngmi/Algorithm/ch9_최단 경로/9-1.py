# 다익스트라 - 간단한 다익스트라 알고리즘
# 인접노드 확인
# 현재 값과 거쳐갈 때 값을 확인해서 갱신
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 10억 설정

n, m = map(int, input().split())  # 노드 개수, 간선의 개수 입력받기
start = int(input())  # 시작 노드번호를 입력받기
graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)   # 방문 여부 확인 리스트
distance = [INF] * (n+1)# 최단 거리 기록 테이블, 무한으로 초기화

# 간선 정보 입력받기
for i in range(m):
    a, b, c = map(int, input().split())# a번 노드에서 b번 노드로 가는 비용이 c 이다.
    graph[a].append((b,c)) # 하나의 튜플로 넣어줌

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
# 시간 복잡도 O(V)
def get_smallest_node():
    min_value = INF
    index = 0 # 최단 거리가 짧은 노드(인덱스)
    for i in range(n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 출발 노드 초기화 거리=0
    visited[start] = True # 출발 노드 방문 처리
    for j in graph[start]: # 출발 노드에서 연결된 노드들
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개에 대해서 반복
    for i in range(n-1):
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        visited[now] = True
        for j in graph[now]: # 현재 노드와 연결된 다른 노드들 확인
            cost = distance[now] + j[1] # 현대 선택된 노드까지의 거리 + 현재 노드와 연결된 다른 노드까지의 거리
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF: # 도달할 수 없는 경우
        print("infinity")
    else: # 도달할 수 있는 경우 거리 출력
        print(distance[i])