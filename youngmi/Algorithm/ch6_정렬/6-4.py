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

'''
피벗: 5
왼쪽 index: 1 왼쪽 값: 7 오른쪽 index: 9 오른쪽 값: 8
작은 데이터와 큰 데이터 교체: [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
작은 데이터와 큰 데이터 교체: [5, 4, 2, 0, 3, 1, 6, 9, 7, 8]
작은 데이터와 피벗 교체: [1, 4, 2, 0, 3, 5, 6, 9, 7, 8]
피벗: 1
왼쪽 index: 1 왼쪽 값: 4 오른쪽 index: 4 오른쪽 값: 3
작은 데이터와 큰 데이터 교체: [1, 0, 2, 4, 3, 5, 6, 9, 7, 8]
작은 데이터와 피벗 교체: [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
피벗: 2
왼쪽 index: 3 왼쪽 값: 4 오른쪽 index: 4 오른쪽 값: 3
작은 데이터와 피벗 교체: [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
피벗: 4
왼쪽 index: 4 왼쪽 값: 3 오른쪽 index: 4 오른쪽 값: 3
작은 데이터와 피벗 교체: [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
피벗: 6
왼쪽 index: 7 왼쪽 값: 9 오른쪽 index: 9 오른쪽 값: 8
작은 데이터와 피벗 교체: [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
피벗: 9
왼쪽 index: 8 왼쪽 값: 7 오른쪽 index: 9 오른쪽 값: 8
작은 데이터와 피벗 교체: [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
피벗: 8
왼쪽 index: 8 왼쪽 값: 7 오른쪽 index: 8 오른쪽 값: 7
작은 데이터와 피벗 교체: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''