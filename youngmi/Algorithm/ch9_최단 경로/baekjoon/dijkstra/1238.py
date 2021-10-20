'''
1238번 파티

문제설명
N개의 마을, 각각 한명의 학생
N명의 학생이 X(1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
마을 사이에는 총 M개의 단방향 도로가 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다(최단시간)
* 도로가 단방향이기 때문에 오고 가는 길이 다를 수도 있다.
N명의 학생들 중 오가는데 가장 많은 시간을 소비하는 학생은 누구인가

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력
둘째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 도로를 지나는데 필요한 소요시간 Ti
* 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중
오고 가는데 가장 오래 걸리는 학생의 소요시간 출력

문제 풀이 아이디어
다익스트라 2번 수행(heapq 필요)
1. N개 마을 → X마을
2. X마을 → N개 마을
두개의 합이 가장 큰 것을 고르면 된다.
'''
import heapq
import sys

input = sys.stdin.readline
INF = 1e9

N, M, X = map(int, input().split()) # 마을&학생, 단방향 도로 개수, 파티하는 마을
graph = [[] for _ in range(N+1)] # 연결정보 저장
for _ in range(M): # 도로 개수 만큼
    a, b, t = map(int, input().split()) # a마을 b마을 t소요시간
    graph[a].append((b, t))

def dijkstra(start):
    h = []
    distance = [INF] * (N + 1)  # 최단 거리정보 표시
    distance[start] = 0 # 자기마을까지의 거리 0
    heapq.heappush(h,(0, start))
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드를 거쳐서 갈 때 비용
            if cost < distance[i[0]]:  # 비용이 원래 거리보다 작으면
                distance[i[0]] = cost # 갱신해줌
                heapq.heappush(h, (cost, i[0])) # 힙에 거리비용과 마을 추가

    return distance # x에 대한 거리정보 반환

result = 0
for i in range(1, N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X]+back[i])

print(result)
