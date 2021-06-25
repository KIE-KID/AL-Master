# 직관적인 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 종료 조건, 원소가 한개인 경우
        return
    pivot = start  # 피벗 설정, 피벗은 첫 번째 값
    left = start + 1 # 왼쪽에서부터 큰 값
    right = end# 오른쪽에서부터 작은 값 찾기
    print("피벗:",array[pivot])
    print("왼쪽 index:",left,"왼쪽 값:",array[left],"오른쪽 index:",right,"오른쪽 값:",array[right])
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 둘이 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right] # 피벗과 작은 데이터의 위치를 swap
            print("작은 데이터와 피벗 교체:",array)
        else: # 엇갈리지 않았다면
            array[right], array[left] = array[left], array[right] # 작은 데이터와 큰 데이터를 swap
            print("작은 데이터와 큰 데이터 교체:",array)

    quick_sort(array,start,right-1)# 왼쪽 리스트 정렬
    quick_sort(array,right+1,end)# 오른쪽 리스트 정렬

quick_sort(array, 0, len(array)-1)
print(array)