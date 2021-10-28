# 커리큘럼
# N : 강의 수
# 강의, 강의시간, 선수강의번호, -1
# 순서가 있는 그래프, 선후관계를 지키는 순서를 계산
# 위상정렬 활용

from collections import deque
import copy

n = int(input())

# 진입 차수
indegree = [0]*(n+1)

# 각 노드에 연결된 간선 정보 담기위한 연결 리스트
graph = [[] for i in range(n+1)]
# 간선 weight? -> 강의 시간
time = [0] * (n+1)

# 강의시간, 선수 과목 정보 받기
for i in range(1, n+1):
    info = list(map(int, input().split(' ')))
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 1. 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 2. 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
            
    
    # 위상정렬을 수행한 결과 출력
    for i in range(1, n+1):
        print(result[i])

topology_sort()