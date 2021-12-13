'''
11403번 경로 찾기

문제설명
가중치 없는 방향 그래프 G
모든 정점 (i, j)에 대해서,
i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램

입력
첫째 줄 정점의 개수 N (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그래프의 인접 행렬
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고,
0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄
정답을 인접행렬 형식으로 출력
정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

문제 풀이 아이디어
모든 정점에서 모든 정점으로의 최단거리, 플로이드 워셜
가중치가 없고 경로의 유무만 표시
경로가 있으면 1로 간주하면 됨.
'''
import sys

input = sys.stdin.readline
N = int(input())  # 정점 개수
graph = []

# 코드 줄여보기~!
# 그래프 경로 정보 입력받기
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][i] == 1 and graph[i][b] == 1:  # 경로가 있다면
                graph[a][b] = 1

for i in range(N):
    print(' '.join(map(str, graph[i])))

# INF = 1e9

# graph = [[INF] * N for _ in range(N)]  # 무한으로 최단 거리 정보 초기화
# for i in range(N):  # 그래프 경로 정보 입력받기
#     node_list = list(map(int, input().split()))
#     for j in range(N):
#         node = node_list[j]
#         if node == 0:
#             continue
#         else:
#             graph[i][j] = node
# 플로이드 워셜
# for i in range(N):
#     for a in range(N):
#         for b in range(N):
#             result = min(graph[a][b], graph[a][i] + graph[i][b])
#             graph[a][b] = result

# 값이 있으면 1로 치환
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] >= INF:
#             graph[i][j] = 0
#         else:
#             graph[i][j] = 1
