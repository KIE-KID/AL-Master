# 팀 결성
# 학생 : 0 ~ N번까지
# 0 : 팀 합치기, 1 : 같은 팀 여부 확인
# M : 연산 개수

# 같은 팀 여부 확인 --> 부모 노드를 찾아가면 된다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split(' '))

# 부모 테이블 초기화
parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i

# 연산 시작
for i in range(M):
    func, t1, t2 = map(int, input().split(' '))
    if func == 0:
        union_parent(parent, t1, t2)
    else:
        if find_parent(parent, t1) == find_parent(parent, t2):
            print('Yes')
        else:
            print('No')
