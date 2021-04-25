'''
4장 구현 실전문제3 - 게임 개발
난이도: 중, 풀이시간: 40분, 시간제한: 1초, 메모리제한: 128MB

문제설명
게임 캐릭터가 맵 안에서 움직이는 시스템
캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이루어진 N x M 크기의 직사각형
각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A,B)로 나타낼 수 있다.
A는 북쪽으로부터 떨어진 칸의 개수
B는 서쪽으로부터 떨어진 칸의 개수
캐릭터는 상하좌우로 움직일 수 있다.
캐릭터는 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터의 움직임을 설정하기 위해 정해 놓은 메뉴얼
1) 현 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전)부터 차례대로 갈 곳을 정한다.
2) 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 있다면 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진하다.
   왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3) 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는 바라보는 방향을 유지한채로 한칸 뒤로 가고
   1단계로 돌아간다. 단, 이때 뒤쪽 방향이바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

아이디어

'''

n,m = map(int,input().split()) # 맵 크기 n, m 입력
row, column, direction = map(int,input().split())# 캐릭터 위치와 방향 초기 값 입력
#0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
game_map = []
for i in range(n):
    game_map.append(list(map(int,input().split()))) #0 육지,  1 바다

directions = [[-1,0],[0,1],[1,0],[0,-1]]
visit = [[row,column]]
count = 0

print(game_map)
while True:
    #처음에 이동할때 전체가 다 뚫려있는지 확인
    for i in range(4):
        temp_row = row + directions[direction][0]
        temp_column = column + directions[direction][1]
        if temp_row >= 0 and temp_row < n and temp_column >= 0 and temp_column < m:
            if game_map[temp_row][temp_column] == 0 and [temp_row, temp_column] not in visit:
                row = temp_row
                count = temp_column
                move = game_map[row][column]
                break
            else:
                direction = (direction + 1) % 4
        else:
            direction = (direction + 1) % 4
        if i == 3:
            row -= directions[direction][0]
            column -= directions[direction][1]
            move = game_map[row][column]
            if move == 1:
                break

    if move == 0:
       if move not in visit:
            row += directions[direction][0]
            column += directions[direction][1]
            count += 1
            visit.append([row, column])
            break
       elif move == 1:
            direction = (direction + 1) % 4
    else:
         break

print(count)

directions[direction][0]