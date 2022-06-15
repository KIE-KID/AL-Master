# 도시분할계획
# N개의 집, M개의 길
# 두 집사이의 경로는 항상 존재
# 경로 유지비의 합은?
# 크루스칼 + 2개의 최소신장 트리로!

# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split(' '))

# 부모 테이블 초기화
parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

edges = []
result = 0

# 길 비용 담기
for i in range(m):
    a, b, cost = map(int, input().split(' '))
    edges.append((cost, a, b))

# 비용 정렬
edges.sort()
# 2개의 최소신장 트리를 만들기 위해 가장 큰 비용의 간선을 제거하는 방식 (가장 간단한 방식)
last = 0

# 도시 분할 시작
for i in range(m):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

result = result - last

print(result)