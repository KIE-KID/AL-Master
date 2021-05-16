'''
5장 DFS/BFS 실전문제3 - 음료수 얼려 먹기
난이도: 중하, 풀이시간: 40분, 시간제한: 1초, 메모리제한: 128MB

문제설명
N x M 크기의 얼음틀에서 뚫려 있는 부분은 0 칸막이가 있는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이대 얼름 들의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 장성하시오.

입력조건
첫번째 줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다.(1<=N,M<=1000)
두번째 줄부터 N+1번쨰 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

출력조건
한번에 만들수 있는 아이스크림의 개수를 출력한다.

문제 풀이 아이디어
그래프로 간주하고 풀이하면 dfs로 풀수있는 문제이다.
한 칸이 노드라고 생각했을 때, 그래프를 표현할 수 있다.
노드가 0이면 상하좌우의 값을 확인하고 0인지 1인지 판단한 다음 0이라면 같은 작업을 반복하면된다.
만일 1이라면 탐색을 멈추고 다음 노드로 넘어가면 된다.

dfs는 스택으로 구현한다. (python의 list를 자주 사용)
노드를 방문하면 스택에 넣었다가 자식노드 중에 방문안한 노드가 있으면 그중 하나를 또 스택에 넣는다.(없을 때까지 반복)
자식노드들을 모두 방문하면 스택에서 제거
'''
n, m = map(int,input().split())
graph = []
graph.append(list(map(int,input().split()) for _ in range(n)))

# 노드를 방문했는지 표시하는 N x M 크기의 2차원 리스트
visited = [[False] * n for _ in range(m)]

def dfs(g, x, y, v): # graph, start, visited
    visited[x][y]


    #다시 dfs 호출
    dfs(g, x, y, v)


dfs(graph, 0, 0, visited)


