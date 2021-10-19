'''
1916번 최소비용 구하기

문제설명
N개의 도시, 한 도시에서 출발해 다른 도시에 도착하는 M개의 버스.
A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화하자.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력
도시의 번호는 1부터 N까지

입력
첫째 줄 도시의 개수 N(1 ≤ N ≤ 1,000)
둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)
셋째 줄부터 M+2줄까지 (버스 출발 도시 번호, 버스 도착 도시 번호, 버스 비용) 버스의 정보가 주어짐
* 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수
M+3째 줄에는 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어짐.
* 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

문제 풀이 아이디어
한 정점 - 한 정점 = 다익스트라
heapq 자료구조 사용
'''
import sys
import heapq

input = sys.stdin.readline
INF = 1e9  # 무한

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수
graph = [[] for _ in range(N + 1)]  # 그래프 연결정보 저장
distance = [INF] * (N + 1)  # 최단 거리 그래프
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a 도시에서 b도시로 가는 비용 c
A, B = map(int, input().split())  # 출발도시, 도착도시


def dijkstra(start):
    h = []  # 큐 정의
    distance[start] = 0  # 자기자신까지의 거리 0
    heapq.heappush(h, (0, start))  # 거리와 정점 튜플로 힙에 추가
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드를 거쳐가는 비용 계산
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 계산한 비용이 작으면 갱신
                heapq.heappush(h, (cost, i[0])) # 힙에 거리정보와 정점을 튜플로 추가


dijkstra(A)

print(distance[B])