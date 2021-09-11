# 경로 압축 : find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법
# 루트노드를 찾는 find 의 복잡도가 줄어들게 된다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]