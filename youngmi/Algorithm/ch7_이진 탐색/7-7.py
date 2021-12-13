'''
7장 이진탐색 실전문제2 - 부품 찾기
단순히 특정한 수가 한번이라도 등장했는지만 확인하면 된다.
집합 자료형으로도 풀이가능
set()함수, 집합 자료형을 초기화할 때 사용
해당 코드가 간결한 측면에서는 가장 우수하다.
'''
n = int(input())
array = set(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')