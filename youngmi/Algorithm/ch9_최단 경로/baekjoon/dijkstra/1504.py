'''
1504번 특정한 최단 경로

문제설명
방향성이 없는 그래프
1번 정점에서 N번 정점으로의 최단거리
단, 임의의 두 정점을 반드시 통과해야함.
한번 이동했던 정점, 간선 모두 다시 이동 가능

입력
첫째 줄에 정점 개수 N과 간선 개수 E(2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어짐.
a번 정점에서 b번 정점까지 양방향 길이 존재 거리가 c이다. (1 ≤ c ≤ 1,000)
다음 줄에는 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2 주어짐(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다.
그러한 경로가 없을 때에는 -1을 출력한다.

문제 풀이 아이디어
다익스트라 2번 수행(heapq 필요)
1번 정점 → v1 → v2 → N번 정점
1번 정점 → v2 → v2 → N번 정점

1번에서 다익스트라
v1에서 다익스트라
v2에서 다익스트라

'''
import sys
import heapq

input = sys.stdin.readline
INF = 1e9

N, E = map(int, input().split())  # 정점개수, 간선개수
graph = [[] for _ in range(N + 1)]  # 연결정보
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향 그래프 이므로 양 정점에 연결정보 모두 추가

v1, v2 = map(int, input().split())  # 거쳐야하는 정점 번호


def dijkstra(start):
    h = []  # 힙 자료구조
    distance = [INF] * (N + 1)  # 최단거리 정보
    distance[start] = 0  # 자기자신
    heapq.heappush(h, (0, start))
    while h:  # 힙에 데이터가 있는 동안 수행
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 갱신해줌
                heapq.heappush(h, (cost, i[0]))  # 힙 자료구조에 추가
    return distance


route1 = dijkstra(1)
route2 = dijkstra(v1)
route3 = dijkstra(v2)
result = min(route1[v1] + route2[v2] + route3[N], route1[v2] + route3[v1] + route2[N])
if result >= INF:
    print(-1)
else:
    print(result)