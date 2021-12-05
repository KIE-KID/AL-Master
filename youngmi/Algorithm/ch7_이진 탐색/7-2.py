# 재귀 함수로 구현한 이진 탐색 소스 코드
# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None # 값을 찾지 못하면 None 반환
    mid = (start + end) // 2 # 중간점 인덱스, 몫 연산자
    if mid == target:
        return mid # 찾은 경우 중간점 인덱스 반환
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인한다.
    if array[mid] < target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽은 확인한다.
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)