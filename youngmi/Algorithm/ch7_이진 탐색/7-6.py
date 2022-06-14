'''
7장 이진탐색 실전문제2 - 부품 찾기
계수정렬로 풀기
counting sort
각 숫자가 몇번 등장했는지 세어준다.
'''
n = int(input())
array = [0] * 1000001 # 최대값 + 1 만큼의 크기만큼 정의해준다.

# 부품번호를 입력받음
for i in input().split():
    array[int(i)] = 1 # 1 대입

m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    if array[i] == 1: # 부품이 있으면
        print("yes", end=' ')
    else:
        print("no", end=' ')