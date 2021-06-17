'''
1260번 DFS와 BFS

문제설명
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

문제 풀이 아이디어
입력받은 n,m,v 저장
bfs, dfs를 구현하고
리스트에 연결정보 저장, 양방향이기 때문에 인덱스를 서로 바꿔서 한번 더 저장해야함
'''
from collections import deque
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 인접한 노드가 방문되지 않은 상태라면 dfs 실행
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 메서드 정의
def bfs(graph, v, visited):
    queue = deque([v])     # 큐 자료구조 구현을 위해 deque 라이브러리 사용
    visited[v] = True     # 현재 노드 방문 처리
    while queue:     # 큐가 빌때까지 반복
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:   # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False for i in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()

dfs(graph,v,visited)
print()
visited = [False for i in range(n+1)]
bfs(graph,v,visited)

