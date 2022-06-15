'''
5장 DFS/BFS 실전문제4 - 미로탈출
난이도: 중하, 풀이시간: 40분, 시간제한: 1초, 메모리제한: 128MB

문제설명
N x M 크기의 직사각형 형태의 미로에 갇혀있따.
현재 위치는 (1, 1)이고 미로의 출구는 (N, M)이다.
한번에 한칸 씩 이동할 수 있고 괴물이 있는 부분은 0, 없는 부분은 1이다.
탈출 하기위해 움직여야하는 최소칸 개수는? (시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력조건
4 <= N, M <= 200
N x M 미로정보 (시작칸과 마지막칸은 항상 1)

출력조건
첫째 줄에 최소 이동 칸의 개수를 출력

문제 풀이 아이디어
최소 칸 개수 = 최소 이동 거리
bfs로 풀수 있다. bfs 구현은 큐로 한다. collections deque 사용
큐에넣고 방문처리, 큐에서 꺼내서 방문하지 않은 인접노드들을 모두 큐에 넣고 방문 처리 한다.
다시 큐에서 노드를 꺼내고 방문하지 않은 인접노드들을 모두 큐에 넣고 방문 처리 한다.

1만 지나가야하는데 최단 경로를 찾아야한다.

5 6
101010
111111
000001
111111
111111
'''
from collections import deque

n, m = map(int, input().split())  # 한줄에 띄어쓰기 없이 정수를 여러개 입력받았을 때는 .split()을 제외한다.
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

direction = [[-1, 0],[1, 0],[0, -1],[0, 1]]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x+direction[i][0], y+direction[i][1]
            if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:
                continue
            if graph[temp_x][temp_y] == 0:
                continue
            if graph[temp_x][temp_y] == 1:
                graph[temp_x][temp_y] = graph[x][y] + 1
                queue.append((temp_x,temp_y))
    return graph[n-1][m-1]

print(bfs(0,0))
