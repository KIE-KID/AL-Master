'''
2178번 미로탐색

문제설명
N×M크기의 배열로 표현되는 미로가 있다.
1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
(1,1)에서 출발 (N, M)으로 이동할 때 지나야하는 최소의 칸 수
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

문제 풀이 아이디어
최소칸수 이기때문에 bfs로 탐색해야한다. 큐 이용
0이 아니면 이동가능하기 때문에 방문했는지 확인하고, 그 값이 1인지 확인,
이동하면 값을 더해서 이동한 칸 수를 표시한다.
'''
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]  # 한줄에 띄어쓰기 없이 정수를 여러개 입력받았을 때는 .split()을 제외한다.

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
#visit 표시할 필요가 궅이 없음.

def bfs(graph, startx, starty):
    queue = deque()
    queue.append([startx, starty])

    while queue: #queue안에 노드가 있는 동안
        x, y = queue.popleft()
        for i in direction:
            temp_x, temp_y = x + i[1], y + i[0]
            if 0 <= temp_x < n and 0 <= temp_y < m and graph[temp_x][temp_y] == 1:
                graph[temp_x][temp_y] = graph[x][y] + 1
                queue.append([temp_x, temp_y])
            else:
                continue
    return graph[n-1][m-1]

print(bfs(graph, 0, 0))

#

# for i in direction:
#     temp_x, temp_y = x + i[1], y + i[0]
#     if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:  # 범위를 벗어나면 무시
#         continue
#     if graph[temp_x][temp_y] == 0:  # 벽인 경우 무시
#         continue
#     if graph[temp_x][temp_y] == 1:  # 벽이 아니고, 처음 방문 하는 경우 최단 경로 표시
#         graph[temp_x][temp_y] = graph[x][y] + 1
#         queue.append([temp_x, temp_y])