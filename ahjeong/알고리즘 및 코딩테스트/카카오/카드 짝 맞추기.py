## 다시 풀기 ##

from itertools import permutations
from collections import deque

size = 4
myboard = [[] for i in range(4)]
card_pos = {}
d = [[0,1], [1,0], [0,-1], [-1,0]]
INF = int(1e4)
answer = INF
orders = []

# 전역 변수를 이용한 보드(myboard), 카드 2장의 위치(card_pos) 초기화 
# 지우는 순서에 대한 순열(orders) 초기화
# card_pos 예시: card_pos[1] = [[0,0], [1,2]] // 카드 1은 보드의 [0,0], [1,2]에 존재 
def init(board):
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_pos.keys(): card_pos[card] = [[i,j]]
                else: card_pos[card].append([i,j])

            myboard[i].append(board[i][j])
    
    orders = [key for key in card_pos.keys()]
    orders = list(permutations(orders))
    
# 이동한 결과가 보드 범위내 있는지 판단하는 함수            
def isin(y,x):
    if -1<y<size:
        if -1<x<size: return True
        
    return False

# ctrl + 방향키
def move(y, x, mv):
    global myboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]
        if not isin(_ny, _nx): return ny, nx
        if myboard[_ny][_nx] != 0: return _ny, _nx
            
        ny = _ny
        nx = _nx

# 카드 1장을 찾을 때 나오는 거리를 반환하는 함수(목표 위치도 반환함)
# 시작 위치: myboard[sy, sx], 찾아야 할 위치: myboard[ey, ex] 
def bfs(sy, sx, ey, ex):
    if [sy, sx] == [ey, ex]: return sy, sx, 1
    global myboard
    q = []
    q = deque(q)
    table = [[0 for j in range(size)] for i in range(size)]
    print('table:', table)
    visit = [[False for j in range(size)] for i in range(size)]
    print('visit:', visit)
    q.append([sy, sx])  # 오른쪽에서 부터 값 삽입
    print('q: ', q)
    visit[sy][sx] = True

    while q:
        y, x = q.popleft()  # 왼쪽에서 부터 값 출력

        for i in range(4):
            ny = y + d[i][0]    # 이동한 y 좌표
            nx = x + d[i][1]    # 이동한 x 좌표

            if isin(ny, nx):    # 이동한 좌표가 보드 범위 안에 있으면 (True)
                if not visit[ny][nx]:   # 그 좌표를 방문안했으면,??
                    visit[ny][nx] = True    # 방문한 걸로 표시
                    table[ny][nx] = table[y][x] + 1
                    if [ny,nx] == [ey,ex]:  # 방문한 곳이 목표 지점이면,
                        return ny, nx, table[ny][nx] + 1    # 현재 좌표 (y, x) 와 이동거리(?) 

                    q.append([ny, nx])  # 큐에 삽입 -> 이제 (ny, nx) 로부터 이동한 좌표를 조사한다.

            ny, nx = move(y, x, d[i])   # 이동

            # 이동한 좌표가 범위 안에 없으면 (False)
            if not visit[ny][nx]:   # 그 좌표를 방문 안했으면
                visit[ny][nx] = True      
                table[ny][nx] = table[y][x] + 1
                if [ny,nx] == [ey,ex]:
                    return ny, nx, table[ny][nx] + 1

                q.append([ny, nx])

    return sy, sx, INF

# 찾은 2장의 카드를 myboard에서 지워주는 함수           
def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = 0

# 지워진 2장의 카드를 myboard에서 복원해주는 함수
def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = card

# backtracking
def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos

    if k == len(card_pos.keys()):
        if answer > count: answer = count
        return

    # 각 카드가 어느 좌표에 있는지 위치 저장
    card = orders[m][k]
    # 한 카드당 2개가 들어있으므로, left/right 각각 한개 씩
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1]
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1]

    # 출발점(sy, sx) -> 그 카드가 있는 첫번째 위치 (left_y, left_x)  를 찾을 때 거리, 좌표
    ry1, rx1, res1 = bfs(sy, sx, left_y, left_x)
    # 찾은 좌표 (ry1, rx1) -> 카드가 있는 두번째 위치 (right_y, right_x) 를 찾을 때 거리, 좌표
    ry2, rx2, res2 = bfs(ry1, rx1, right_y, right_x)
    
    # 그 카드 찾았으니까 삭제
    remove(card)
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    restore(card)

    ry1, rx1, res1 = bfs(sy, sx, right_y, right_x)
    ry2, rx2, res2 = bfs(ry1, rx1, left_y, left_x)

    remove(card)
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    restore(card)

def solution(board, r, c):
    global answer
    init(board)

    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)

    print(answer)

# board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
# r, c = 1, 0

# solution(board, r, c)