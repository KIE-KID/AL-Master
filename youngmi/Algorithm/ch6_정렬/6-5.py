# 파이썬의 장점을 살려 짧게 작성한 퀵 정렬 소스 코드
# 일반적인 퀵 정렬의 분할 방식과는 조금 다른데 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적이다.
# 하지만 더 직관적이고 기억하기 쉽다는 장점이 있다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료, 종료 조건
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 리스트의 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))