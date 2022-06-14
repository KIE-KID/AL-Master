# 개선된 다익스트라 알고리즘
import sys
import heapq

input = sys.stdin.readline
INF = 1e9  # 무한 값

# 출발 노드를 설정하여 우선순위 큐에 삽입
# 현재의 최단 거리와 노드 번호를 튜플로 묶어 넣어준다.

n, m = map(int, input().split())  # 노드 개수, 간선 개수 입력
start = int(input())  # 시작 노드 입력받기
graph = [[] for i in range(n + 1)]  # 각 노드에 연결된 노드에 대한 정보를 담는 리스트
# 노드 방문 여부를 확인 하는 리스트가 없음
distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

# 간선 정보 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b노드까지 비용c
    graph[a].append((b, c))  # 9-1의 방식과 달리 반대로 넣어줌

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 삽입, 삭제가 logN을 보장
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면 = 큐가 빌 때 까지
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            continue
        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1] # 현재 노드까지의 거리와, 현재 노드에서 인접노드까지의 거리값
            if cost < distance[i[0]]:  # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush((q, (cost, i[0])))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])
