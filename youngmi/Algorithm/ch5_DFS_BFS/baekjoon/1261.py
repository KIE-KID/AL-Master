'''
1261번 알고스팟

문제설명
미로는 N*M 크기, 1*1크기의 방으로 이루어져 있다
벽을 부수어야만 이동 가능하다.
이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
(x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
단, 미로의 밖으로 이동 할 수는 없다.
현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는가?

입력
첫째 줄 미로의 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)
다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다.
* 0은 빈 방을 의미하고, 1은 벽을 의미
(1, 1)과 (N, M)은 항상 뚫려있다.

출력
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해
벽을 최소 몇 개 부수어야 하는지 출력

문제 풀이 아이디어
0인 곳으로 이동해야함.
사방이 1이라면
최단거리, bfs, 큐, deque
비용이 0과 1로 나뉘어져있을때에는 deque를 사용해서 매 노드를 탐색할 때마다
갈 수 있는 노드에 대한 비용이 0이면 앞에, 1이면 뒤에 추가해주며 탐색한다.

그렇게 하면 비용이 적은 경로부터 우선적으로 탐색하고, 가장 적은 비용에 대한
탐색이 끝나고 나서야 비로소 더 큰 비용의 경로를 탐색하기 시작하기 때문에
벽을 최소한으로 부수고 이동하는 경로를 찾을 수 있게 된다.
'''
from collections import deque

M, N = map(int, input().split())  # 가로M 세로N
graph = [list(map(int, input())) for i in range(N)]  # 띄어쓰기가 없는 경우 .split() 생략
dist = [[-1] * M for _ in range(N)]
dist[0][0]= 0
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우


def bfs(graph, dist, x, y):
    q = deque()  # 큐 자료구조 구현을 위해 deque 라이브러리 사용
    q.append([x, y])
    # 큐가 빌때까지 반복
    while q:
        x, y = q.popleft()
        for i in direction:
            temp_x, temp_y = x + i[0], y + i[1]
            if 0 <= temp_x < N and 0 <= temp_y < M and dist[temp_x][temp_y] == -1: # 범위내에 있고 아직 방문하지 않은 칸
                if graph[temp_x][temp_y] == 0:
                    dist[temp_x][temp_y] = dist[x][y]
                    q.appendleft([temp_x, temp_y]) # 0인 경우를 먼저 탐색, 우선순위가 높음
                elif graph[temp_x][temp_y] == 1:
                    dist[temp_x][temp_y] = dist[x][y] + 1
                    q.append([temp_x, temp_y])

    return dist[-1][-1]

print(bfs(graph, dist, 0, 0))