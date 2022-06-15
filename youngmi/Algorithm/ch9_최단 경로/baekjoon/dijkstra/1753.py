'''
1753번 최단경로

문제설명
방향그래프가 주어지면, 시작점에서 다른 모든 정점까지의 최단 경로를 구하는 프로그램
단, 모든 간선의 가중치는 10 이하의 자연수

입력
첫째 줄 정점의 개수 V 간선의 개수 E  (1≤V≤20,000, 1≤E≤300,000)
둘째 줄에는 시작 정점 번호 K(1≤K≤V)
셋쨰 줄부터 E개 줄까지 세 개의 정수 (u, v, w)
* u에서 v로 가는 가중치 w인 간선
* u와 v는 서로 다르며 w는 10 이하의 자연수
* 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음

출력
첫째 줄부터 V개의 줄에 걸쳐,
i번째 줄에 i번 정점으로의 최단 경로값을 출력
시작점 자신은 0
경로가 존재하지 않으면 INF

문제 풀이 아이디어
한 정점 - 모든 정점의 최단 경로 = 다익스트라
heapq 자료구조 사용
'''
import sys
import heapq

input = sys.stdin.readline
INF = 1e9  # 무한 정의

V, E = map(int, input().split())  # 정점개수, 간선개수
K = int(input())  # 시작 정점
graph = [[] for i in range(V + 1)]  # 각 노드에 연결된 노드에 대한 정보를 담는 리스트
distance = [INF] * (V + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(E):
    u, v, w = map(int, input().split())  # 정점 u v , 가중치 간선 w
    graph[u].append((v, w))  # 그래프 정보에 v로 가는 간선 w를 튜플로 저장


def dijkstra(start):
    h = []  # 힙 자료구조
    distance[start] = 0  # 시작점 자기자신의 거리 0
    heapq.heappush(h, (0, start))
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드를 거쳐가는 비용 계산
            if cost < distance[i[0]]:  # 기존의 거리와 새로 계산한 비용을 비교
                distance[i[0]] = cost  # 새로 계산한 비용이 작으면 갱신해줌
                heapq.heappush(h, (cost, i[0]))  # heap에 새로 갱신한 거리와 노드번호 추가


dijkstra(K)

for i in distance[1:]:
    if i >= INF:
        print('INF')
    else:
        print(i)
