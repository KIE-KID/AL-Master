import heapq    # 우선수위 큐 를 위해 힙 사용

# 다익스트라 알고리즘 구현
def dijkstra(graph, s):
    d = {}
    for node in graph:
        d[node] = float('inf')   # 처음에 (출발점~노드) 까지 비용을 무한대로 설정
    d[s] = 0    # 출발점의 최소 비용은 0
    queue = []
    heapq.heappush(queue, [d[s], s])    # 먼저 s 부터 시작

    while queue:
        # 현재 큐 안에 들어있는 노드를 가져온다. -> 현재 탐색할 노드
        # 제일 처음은 출발점 부터 시작
        current_distance, current_destination = heapq.heappop(queue)    # heappop 은 가장 작은 원소 삭제

        # 현재 탐색하는 노드가 기존의 저장된 거리보다 비용이 크다면 패스
        if d[current_destination] < current_distance:
            continue
        # 현재 탐색하고 있는 노드에 연결되어 있는 노드 : graph[current_dstination].items()

        for new_destination, new_distance in graph[current_destination].items():

            distance = current_distance + new_distance
            if distance < d[new_destination] :  # 제일 처음에는 d[] = 무한대에서 distance 로 바뀜
                d[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return d        # 최단 거리가 담겨있음
    
def solution(n, s, a, b, fares):
    answer = 0
    graph = {}
    
    # 다익스트라 그래프 만들기
    for i in range(n):
        graph[i+1] = {}

    for i in fares:     # fares 의 나온 간선의 요금을 딕셔너리에 저장
        if i[0] in graph: 
            graph[i[0]][i[1]] = i[2]
        if i[1] in graph:
            graph[i[1]][i[0]] = i[2]
            
    
    # 모든 노드에 대해 dijkstra 수행
    min_graph = {}  # 각 지점에서 모든 노드까지 걸리는 최단 비용
    for i in range(n):
        min_graph[i+1] = dijkstra(graph, i+1)
    
    min_list = []
    # s->k, k->a, k->b 비용 구하기
    print(min_graph[s])
    for node in min_graph[s]:
        s_k = min_graph[s].get(node)  # s->k 비용
        s_a = min_graph[node].get(a)    # k->a 비용
        s_b = min_graph[node].get(b)    # k->a 비용
        min_list.append(s_k + s_a + s_b)     # s->k + k->a + k>b
        
    answer = min(min_list)
    return answer