'''
9장 최단 경로 실전문제3 - 전보
난이도: 상, 풀이시간: 60분, 시간제한: 1초, 메모리제한: 128MB, 기출 유명 알고리즘 대회

문제설명
N개 도시
X→Y, Y→X 도로가 있어야만 전보를 주고 받을 수 있다. (단방향 간선)
각 도시의 번호와 통로가 설치되어있는 정보가 주어질 때
메시지를 받게되는 도시의 개수는 총 몇개이고, 도시들이 모두 메시지를 받는 데 까지 걸리는 시간은 얼마인가?

입력조건
첫째 줄에 도시의 개수 N, 통로 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
(1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N )
둘쨰 줄 부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
특정 도시 X에서 Y로 이어지는 통로가 있고 메시지가 전달되는 시간은 Z
(1 <= X, Y <= N, 1 <= Z <= 1,000)

출력조건
C에서 보낸 메시지를 받는 도시 개수와 총 거리는 시간을 공백으로 구분하여 출력

문제 풀이 아이디어
C에서 모든 도시로의 최단 경로이므로, 다익스트라 알고리즘을 이용하면 된다.
'''
import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)  # 무한
n, m, c = map(int, input().split())  # 도시개수, 통로개수, 메시지를 보내는 도시
graph = [[] for _ in range(n + 1)]  # 도시끼리의 통로 표시
distance = [INF] * (n + 1)  # 최단 거리 테이블

for _ in range(m):
    x, y, z  = map(int, input().split())
    graph[x].append((y, z))  # 거리, 도시 순서로 튜플로 만들어서 넣음


# 매 단계마다 우선순위 큐에서 노드를 꺼내서 해당노드까지의 거리를 확인 한 뒤
# 그 노드를 거쳐가는(연결된) 각각의 경우도 모두 살펴본다.
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))  # 힙으로 넣어줌, 최소힙
    distance[start] = 0  # 시작지점의 거리는 0
    while h:  # 힙에 항목이 있는 동안
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드까지의 거리와, 현재 노드에서 인접노드까지의 거리값
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 더 작은 값으로 갱신
                heapq.heappush(h, (cost, i[0]))  # 힙에 추가


dijkstra(c)

count = 0  # 도시개수
max_dist = 0
for i in range(len(distance)):
    if distance[i] != INF:
        count += 1
        max_dist = max(max_dist, distance[i])

print(count-1, max_dist)

#3 2 1
#1 2 4
#1 3 2
#2 4